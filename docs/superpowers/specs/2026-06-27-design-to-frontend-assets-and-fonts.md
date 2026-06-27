# Design to Frontend Assets and Fonts

状态：current
Owner：skills-lab maintainers
Update trigger：`design-to-frontend-delivery` 的高保真、字体、资源或浏览器验收规则继续变化时更新。

## 背景

`design-to-frontend-delivery` 已覆盖结构化源优先、专业布局保真、工程目录边界和 mock/BFF 边界，但真实高保真还原还有一个高频失效点：字体和资源没有进入项目，Agent 却继续微调间距、颜色、坐标或组件尺寸。典型结果是“怎么调都不像”，最后发现本机没有设计字体、缺少字重、图片/图标是 placeholder，或浏览器实际 fallback 到默认字体。

## 资料结论

- Figma 缺失字体常见原因包括本机没有对应字体样式、协作者字体版本不一致、浏览器没有安装 font helper，或 MCP/Agent 无法访问本机字体；Figma 要求相关字体文件/样式可被设计环境访问，并在上传时确认使用权利。
- Web 交付不能依赖某台机器的已安装字体。CSS `@font-face` 用于定义并加载自定义字体，`src` 是必需资源引用；Web 场景优先使用 WOFF2。
- Web 字体加载会影响首屏文本可见性和布局稳定性。关键字体可使用 preload、`font-display` 或 Font Loading API 管理加载和渲染策略。
- `document.fonts` / `FontFaceSet.ready` 可用于确认文档字体加载状态，截图或视觉比对应在字体与关键资源加载后执行。
- Playwright 支持截图视觉比对，但官方明确浏览器截图会受 OS、浏览器、硬件、headless 等环境影响；基线与实际比对应尽量在相同环境中执行。

参考来源：

- Figma Help: [Missing font alert in Figma Design](https://help.figma.com/hc/en-us/articles/360039956994-Missing-font-alert-in-Figma-Design)
- MDN: [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face), [`Document.fonts`](https://developer.mozilla.org/en-US/docs/Web/API/Document/fonts), [`FontFaceSet.ready`](https://developer.mozilla.org/en-US/docs/Web/API/FontFaceSet/ready)
- web.dev: [Optimize WebFont loading and rendering](https://web.dev/articles/optimize-webfont-loading)
- Playwright: [Visual comparisons](https://playwright.dev/docs/test-snapshots)

## 决策

将“字体与资源真实性”加入 `design-to-frontend-delivery` 的核心高保真门禁：

1. 高保真调样式前必须盘点字体 family、weight/style、变量轴、图片、图标、媒体、tokens、资源来源和 fallback/blocked 决策。
2. 字体、字重、图片、图标、视频、SVG、Lottie、背景图和品牌媒体都视为项目资源，不允许默认依赖本机是否安装。
3. 缺少关键字体或资源时，先补授权资源、接入项目已有 provider/package/CDN，或明确 fallback/blocked；不得继续通过 CSS 微调掩盖缺失字体。
4. 浏览器验收必须检查关键字体和资源实际加载，截图或视觉比对应等待字体加载完成。
5. 关键字体/资源缺失时，不能声称高保真通过，只能标为条件通过或 blocked pending asset；无论资源是否完整，都不得把交付结论写成 pixel-perfect 或像素级 100%。

## Skill 变更范围

- `SKILL.md` 增加 Typography and Asset Fidelity Contract，并要求高保真/资源相关任务读取 `assets-and-visual-fidelity.md`。
- 新增 `references/assets-and-visual-fidelity.md`，集中承载字体、资源、浏览器验证和失败响应规则。
- `convert-and-polish.md` 在 Gate 1/2/3 加入字体与资源清单、浏览器加载验证和缺失项处理。
- `polish-existing-project.md` 将现有工程字体/资源健康度纳入审计和最小闭环扩围条件。
- `delivery-checklists.md` 将字体实际加载和资源可用性加入八层模型、三道闸门和收尾输出。
- `README.md` 与 `docs/README.md` 只保留摘要和入口，不复制完整规则。

## 验收

- `design-to-frontend-delivery` 通过 `quick_validate.py`。
- 仓库内全部 skills 通过 `quick_validate.py`。
- `git diff --check` 通过。
- `npx skills add . --list --full-depth` 可发现该 skill。
- 从 GitHub 远端安装后，安装版 `design-to-frontend-delivery` 包含字体/资源门禁规则。

## 风险

- 本规则不能自动判断商业字体授权是否允许提交到项目；遇到不明确来源时仍必须询问用户或使用批准 provider。
- 截图视觉比对仍受环境影响；规则要求等待字体与关键资源加载，但验收目标仍是高保真视觉关系，不是跨 OS、浏览器、响应式断点和动态内容状态的像素级完全一致。
