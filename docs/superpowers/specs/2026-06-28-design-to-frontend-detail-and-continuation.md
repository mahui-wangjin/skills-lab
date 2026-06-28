# design-to-frontend-delivery 图标细节与后续开发优化

状态：current
Owner：skills-lab maintainers
Update trigger：`design-to-frontend-delivery` 的图标/资源/设计 token、状态细节、API 对接、功能修改或回归保护规则继续变化时更新。

## 背景

用户反馈：远端设计明明有对应图标，Agent 却会自己造一个图标；hover、边框、内边距、尖角/圆角等细节也经常不认真按设计处理。设计转代码是精细活，不能脱离设计图和项目事实源随便发挥。找不到资产或细节来源时，应反馈并对齐，而不是静默自造。

用户进一步提出：这个 skill 不应只覆盖首次设计转代码，也应覆盖后续前端页面开发和精修。后续 API 对接、功能修改、bugfix 或回归修复必须有资深前端门禁，尤其不能影响其他页面。

## RED 压力场景

```text
设计源中存在一个远端 SVG 图标、按钮 hover variant、8px radius、12px horizontal padding、1px border 和特定 shadow。
Agent 为了快：
- 手写了一个“差不多”的 SVG
- 换成 lucide/其他图标库里的相似图标
- 用组件库默认 hover 色和默认圆角
- 把边框、padding、shadow 调成个人感觉好看的值
- 后续接 API 时顺手重构共享按钮和 hook，导致其他页面样式和行为变化
最终页面看着可运行，但已经脱离设计事实源，用户验收时需要返工。
```

失败模式：

- 把图标、radius、padding、border、shadow 和 hover 当成可自由发挥的装饰。
- 没有检查设计平台、导出 assets、项目图标库、组件映射、tokens 和 accepted implementation。
- 找不到资源时不反馈，直接自绘或替换。
- API/bugfix 任务没有确认 accepted baseline、影响面、共享消费者和回归面。
- 修一个页面时误伤共享组件、token、hook、API client、store/cache 或其他页面。

## 设计变更

- 在 `SKILL.md` 增加 `Source-Locked Asset and Detail Contract`。
- 在 `SKILL.md` 增加 `Continuation Development and Regression Contract`。
- 将模式从 `Single Entry, Two Modes` 扩为 `Single Entry, Three Modes`，新增 `frontend-continuation`。
- 新增 `references/frontend-continuation.md`，承接 API/BFF 对接、功能修改、bugfix、回归修复和增量需求。
- 扩展 `assets-and-visual-fidelity.md`，将图标身份、detail tokens、状态 variants 和浏览器验证纳入资源保真。
- 扩展 `convert-and-polish.md` 与 `polish-existing-project.md`，要求 Gate 1/2/3 记录图标、tokens、border/padding/radius/shadow/motion/state details。
- 扩展 `delivery-checklists.md`，把 `frontend-continuation` 的影响面、回归面、共享消费者和 API/行为契约加入三道闸门。
- 扩展 README smoke cases，覆盖“远端有图标却自绘”“hover/边框/圆角不像设计”“接 API/修 bug 不影响其他页面”。

## 边界口径

图标与细节：

- 远端/设计源、导出包、组件映射或项目资产中已有图标、SVG、插画、logo 和装饰形状时，必须复用。
- 不得手绘相似图标、换另一套图标库、截图裁切或用泛化符号替换已有 source asset。
- hover、active、pressed、focus-visible、selected、disabled、loading、error、success 都是状态 variants。
- border、padding、radius、shadow、outline、opacity、transition/easing、hit area 和 cursor 必须来自设计源、项目 token、组件 variant 或已记录 fallback。
- 找不到来源时，先反馈缺失并对齐资产或 fallback，不能静默自造。

后续开发：

- API/BFF 对接、功能修改、bugfix、回归修复或增量需求进入 `frontend-continuation`。
- 开工前确认 accepted baseline、API/行为契约来源、影响面、回归面、共享消费者和自测路径。
- 复用项目已有 API client、query/cache、form、validation、loading/empty/error、toast/confirm、权限和 overlay 模式。
- 组件不承担 BFF/domain-owned 生命周期、权限、资格、重试策略或跨记录 workflow 决策。
- 修改共享组件、token、hook、API client、store/cache 或 route guard 时，必须覆盖其他已知消费者回归。
- 修 bug 或接 API 不等于允许重设计壳层、替换图标、改视觉 token 或影响其他页面。

## 钢人反论

### 反论 1：图标找不到就让 Agent 自绘，交付更快。

回应：这会把事实缺口伪装成实现完成。已有远端图标或项目图标系统是 source asset，不是审美建议。自绘只能用于明确 prototype fallback，并且必须披露；高保真交付不能静默替代。

### 反论 2：hover、圆角、padding 这些细节很小，不值得进门禁。

回应：这些正是设计还原里最容易“差点意思”的地方。按钮、卡片和表单的密度、状态和手感由这些细节决定。规则要求映射到 token/variant，不要求写长文档。

### 反论 3：新增 `frontend-continuation` 会不会和普通工程开发 skill 重叠？

回应：这里的边界是“已接受前端设计实现后的继续开发”。它不是通用前端工程总纲，而是保护既有设计事实、共享消费者和回归面的专用模式。

### 反论 4：每次 bugfix 都做影响面会不会过重？

回应：影响面可以很轻量。局部 bugfix 只需列出被改页面和相关共享依赖；触碰共享组件、token、hook、API client 或 store/cache 时才扩大回归。

### 反论 5：API 对接是否会逼前端承担 BFF/domain 逻辑？

回应：不会。规则明确组件只接 display-ready props 或薄 view model；生命周期、权限、资格、重试策略和跨记录 workflow 仍属于 BFF/domain。

## 验收标准

- `design-to-frontend-delivery` quick_validate 通过。
- 全量 skills quick_validate 通过。
- README smoke case 覆盖图标自造、细节 token、API/bugfix 回归场景。
- 安装版包含 `Source-Locked Asset and Detail Contract`、`Continuation Development and Regression Contract`、`frontend-continuation`、`Asset/detail source`、`后续变更影响面`。
