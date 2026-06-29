# Polish Existing Project

## 1. 现状审计

先审计当前工程，但不要默认它已经是“已接受实现基线”：

- 页面与路由覆盖：哪些页面已存在、哪些流程未串通
- 八层覆盖度：结构、布局、内容、交互、数据边界、校验、状态、表现
- UI 层级归属：app shell、page frame、content sections、collection items、local controls、overlay/feedback、decoration/media、data/state 的 owner 是否清晰
- 工程目录健康度：页面入口、feature/module、components、mock/fixtures、selectors/formatters、styles/assets、tests/stories 是否按当前框架和项目约定归位
- 布局健康度：普通页面、卡片、列表、表单、仪表盘和内容布局是否使用 Flex/Grid/flow、tokens 和响应式约束
- 绝对定位审计：主布局区域、重复卡片/行、响应式列、表单、仪表盘或内容流是否由 `position:absolute`、`left/top`、固定像素坐标或截图叠层驱动；若存在，判断是合理例外还是需要结构修复
- 字体与资源健康度：关键字体 family/weight/style 是否真实加载，图片/图标/媒体是否来自项目资源或批准来源，是否存在 404、placeholder、缺失字重、截图替代 UI 或仅依赖本机字体
- 图标与细节 token 健康度：图标是否复用项目图标系统/导出 SVG/组件映射，边框、内边距、圆角、阴影、hover/active/focus/disabled/loading/error/success 和动效是否来自项目 token/组件 variant，而不是手写自造
- mock/API 边界：当前数据是静态 fixture、BFF-shaped mock、已接 API，还是混杂不清；业务裁定是否被写进页面/组件
- 已有壳层约束：Header/Footer/Layout/Router 是否必须保留
- 公共面健康度：app layout、顶部栏、侧边栏/导航、面包屑、页签、页面工具栏、全局 modal/drawer/confirm/toast roots、loading/empty/error 模式是否复用现有项目范式
- 交互可用性：可点击对象是否语义化，cursor、hover、active/pressed、focus-visible、disabled、loading/submitting、selected/current、移动端触控和键盘路径是否成立
- 当前阻塞项：缺失弹框、缺失禁用态、缺失错误反馈、不可回退路径、点击目标不明显、弹层不可关闭、公共反馈面未接入

输出一份“现状覆盖快照”，作为后续精修依据。
该快照也是本模式 Gate 2 的输入之一。

审计后还必须输出最小精修合同：

```md
Minimum polish contract:
- Accepted baseline: <current implementation evidence>
- Deliverable surface: <content-only | inside-existing-shell | full-page-with-shell>
- UI layer map: <owners and boundary risks for shell / page frame / content / repeated items / local controls / overlays / decoration / data-state>
- Common surfaces: <reuse / repair / out of scope>
- Asset/detail source: <icons, tokens, borders, padding, radii, shadows, motion and state variants source>
- Interaction gaps: <click targets, overlays, forms, navigation, feedback states>
- Browser acceptance path: <existing real-browser command/harness or minimum real-browser acceptance path; smoke only as health check>
- Minimum closure: <smallest set that makes the named scope demo-ready>
- Non-goals: <shell redesign, real API, domain decisions, etc.>
- Blocking question: <none or one question that changes scope/acceptance>
```

## 1.5 基线身份判定（必须）

审计后，必须判断“当前工程”是否已具备 accepted baseline 身份。可接受信号与 `source-priority.md` 一致：

- 用户明确确认“当前实现就是本轮保留/精修基线”
- 当前实现已在目标项目分支被采纳（已合入/已正式采用）
- 项目文档、规格或计划明确标注其为本轮 accepted baseline

若以上信号都不成立，不得直接把当前工程当作 polish 基线。
必须先提问确认，再决定是否继续走 `polish-existing-project`，或改走其他路径。

## 2. 差距分析：点名范围 vs 目标结果

对比两件事：

- 用户点名范围（例如“只补交互”）
- 目标结果（可演示静态页面）

若两者存在断层，必须明确列出：

- 缺失层级是什么
- 这些缺失会导致什么演示问题
- 只做点名范围后的预计完成度
- 若存在所有内容堆在一个文件或一个目录，说明页面入口、feature-private 组件、fixtures、展示选择器、样式/assets、测试应如何按当前框架约定拆开
- 若存在 UI 层级归属错误，说明哪些组件放错层：shell/page frame/content section/repeated item/local control/overlay/decoration/data-state；谁应拥有渲染、状态、布局、overlay root 和 stacking context
- 若存在坐标式布局，说明它对响应式、内容伸缩、可维护性和后续高保真精修的影响
- 若存在字体或资源缺失，说明继续视觉微调会产生什么误判：文本宽度、换行、层级、密度、图标大小、图片裁切或截图对比都可能在真实资源补齐后改变
- 若存在图标或细节 token 缺失，说明哪些远端/项目已有图标被替换、自绘或截图化，哪些 hover、边框、padding、圆角、阴影、动效和状态样式脱离了设计源或项目范式
- 若存在 mock/API 混杂，说明哪些逻辑应退回 fixture/BFF 返回字段，哪些轻量 UI 状态可以留在前端
- 若设计或现状只覆盖内容区，说明是否需要接入现有 shell、导航、面包屑、页面工具栏、modal/drawer/toast/confirm roots，或把它们明确列为本轮非目标
- 若交互看得见但不好用，说明哪些点击对象缺少语义、cursor、hover/active/focus、disabled/loading、关闭/返回路径、移动端触控或反馈态

当以上差距清单与最小闭环建议被确认后，视为本模式 Gate 2 通过，再进入具体实现。

## 3. 何时建议扩到最小闭环

满足任一条件时，建议最小闭环扩围：

- 点名范围无法闭合主流程（例如能点但无法提交或无法回退）
- 点名范围只要求补页面/补设计还原，但当前工程结构会继续把页面入口、组件、mock、展示选择器、样式或测试混堆到同一文件/目录
- 页面标题、面包屑、页签、页面工具栏、筛选、卡片、列表项、弹框、toast、装饰层或数据状态放错 owner 层，导致视觉接近但结构和维护边界错误
- 点名范围只要求“调得更像设计稿”，但当前布局依赖大量绝对定位或固定坐标，继续微调会扩大响应式和维护风险
- 点名范围只要求“继续调像一点”，但关键字体、字重、图片、图标或媒体尚未作为项目资源加载，继续调样式会掩盖真正原因
- 点名范围只要求“看起来再像一点”，但图标、边框、内边距、圆角、阴影、hover/focus/disabled/loading 等状态细节没有来源，或已经偏离项目 token/组件 variant
- 点名范围只要求静态展示或视觉精修，但当前页面已经把 BFF/API 的领域状态、授权/资格、可执行动作裁定、生命周期/状态流转或集成状态归一化写成前端推导
- 点名范围只要求内容区还原，但 demo-ready 结果需要接入已有公共 shell、导航、页面工具栏、面包屑或统一 overlay/feedback 系统
- 可点击对象没有明确手势、语义、键盘焦点、禁用/加载态、失败反馈或返回路径，导致用户不知道哪里能点或点完卡住
- 没有端到端或真实浏览器自测路径，导致改完后只能凭代码和截图猜测是否可演示
- 缺少基础校验与错误反馈，导致演示不可用
- 缺少关键状态（加载/失败/空态）导致流程断裂

扩围建议应是“最小必要组合”，例如：  
`交互 + 校验 + 对应反馈态`，或 `内容区 + 既有 shell 接入 + 统一 toast/confirm`，而不是默认全量精修。

## 4. 不擅自扩做，但必须提示差距

规则：

- 未获确认前，不扩大实现范围。
- 即便用户坚持只做点名项，也必须在阶段输出里写清剩余差距和风险。
- 输出时标注“已完成项 / 未覆盖项 / 建议下一步最小闭环”。

## 5. 完成前自测

实施后必须以真实浏览器验收作为主自测路径。优先运行项目已有 E2E、agent-browser、Playwright、Cypress、browser、screenshot 或 Storybook-in-browser 流程；smoke 只作为健康检查。没有现成路径时，执行最小真实浏览器自测：

- 打开被精修页面和关键入口。
- 验证 UI layer ownership：shell、page frame、content、repeated item、local control、overlay/feedback、decoration/media、data/state 没有明显错层。
- 覆盖点名范围和最小闭环中的主操作、弹层开合、提交/取消、返回路径、禁用/加载/失败反馈。
- 验证图标和细节状态：远端/项目已有图标未被替换或手绘，hover/active/focus-visible/disabled/loading、border/padding/radius/shadow/motion 与设计源或项目组件范式一致。
- 检查桌面与窄屏/移动视口、console errors、failed requests、资源加载、文本溢出、遮挡、重复滚动条和 z-index/portal/overflow 问题。

无法完成真实浏览器自测或浏览器调试时，必须提醒用户缺少 console/network/runtime/layout/screenshot 证据，并说明需要的环境、工具或访问方式。不得声称 demo-ready 完成；只能输出 self-reviewed/conditional 或代码级候选结果，并列出未验收路径。smoke-only 结果不能替代前端质量验收。
