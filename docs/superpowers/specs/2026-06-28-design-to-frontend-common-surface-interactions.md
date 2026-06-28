# design-to-frontend-delivery 公共面与交互可用性优化

## 背景

用户反馈：设计转前端时，Agent 容易只还原设计图中显式画出的业务内容区。设计图没有画侧边栏、顶栏、面包屑、公共弹框、toast 或统一反馈面时，Agent 常常默认忽略；页面上的按钮、卡片、菜单和弹框也可能缺少 cursor、hover、focus、disabled、关闭路径和失败反馈，直到用户指出后才补。

用户期望：前端交付应默认具备产品面和可用性判断，不应只做“看起来像”的静态图。Agent 应主动判断交付表面、复用现有公共壳层和共享交互系统，并把可点击性、反馈态和返回路径纳入演示级验收。

## RED 压力场景

```text
用户给出一个业务页面设计稿，目标是落到已有 React/Vue/Admin 工程。
设计稿只画了右侧内容区，没有画应用侧边栏、顶栏、面包屑或统一弹框。
Agent 直接新建一个孤立页面：
- 不接现有 AppShell/Sidebar/Header
- 自己写一个局部弹框或 toast
- 卡片和行操作用 div onClick
- 按钮没有 hover/focus/disabled/loading
- 弹框能打开但关闭/失败/返回路径不完整
最终截图接近设计稿，但产品经理验收时认为“不是系统里的页面，也不好用”。
```

失败模式：

- 把设计稿未画公共区域误读为公共区域不在交付质量内。
- 不先识别交付表面：`content-only`、`inside-existing-shell`、`full-page-with-shell`。
- 忽略现有项目的 shell、导航、面包屑、工具栏、modal/drawer/toast/confirm roots。
- 只补视觉，不补语义控件、cursor、hover、focus-visible、disabled/loading、键盘/触控路径和弹层关闭。
- 为了让交互“完整”又提前实现 mock 阶段不该承担的业务裁定。

说明：本轮 RED 来自用户明确反馈和当前 skill 缺口，未额外启动子代理 baseline。

## 设计变更

- 在 `SKILL.md` 增加 `Common Surface Contract` 与 `Interaction Affordance Contract`。
- 在 Gate 1 增加最小执行合同：交付表面、公共面复用、主交互和状态、最小闭环、非目标、唯一阻塞问题。
- 在 `convert-and-polish.md` 增加公共面接入规则与交互可用性步骤。
- 在 `polish-existing-project.md` 增加公共面健康度、交互可用性审计、最小精修合同和最小闭环扩围触发条件。
- 在 `delivery-checklists.md` 增加公共面、cursor、语义控件、hover/active/focus-visible、disabled/loading、弹层关闭、键盘/触控和返回路径验收项。
- 在 `source-priority.md` 将 accepted host shell、navigation frame、overlay/feedback roots 和 reusable UI patterns 纳入强项目事实。
- 在 README smoke case 中增加“设计稿只画内容区”和“页面像但不知道哪里能点”的判断场景。

## 边界口径

默认先做：

- 判断本轮交付是 `content-only`、`inside-existing-shell` 还是 `full-page-with-shell`。
- 目标是现有工程时，先审计并复用 app layout、Header/Topbar、Sidebar/Nav、breadcrumbs、tabs、toolbar、modal/drawer/confirm/toast roots、loading/empty/error 模式。
- 所有可交互元素使用语义控件或项目可访问组件，补齐 cursor、hover、active/pressed、focus-visible、disabled、loading/submitting、selected/current 等状态。
- 弹框、抽屉、popover、confirm、toast 必须有打开、关闭、取消/确认、失败反馈和返回主任务路径。
- 移动端和窄屏不能依赖 hover-only 发现，触控目标和弹层不应遮挡、溢出或不可关闭。

禁止默认做：

- 因为设计图没有公共区域就忽略现有项目 shell。
- 在已有统一 modal/toast/drawer 系统时新建平行反馈系统。
- 用不可聚焦 `div`/`span` 当主要按钮、链接或菜单项。
- 让 disabled/non-clickable 元素表现得像能点。
- 为了补交互而提前实现真实权限、资格、生命周期、业务流转或 API 状态机。

例外：

- 用户明确只要 `content-only` 静态片段时，可以不接公共壳层，但最终必须把公共面列为非目标，不能声称完整产品页完成。
- 极高密度后台表格可遵循项目设计系统的紧凑尺寸，但仍要保证焦点、禁用、反馈和不遮挡。

## 钢人反论

### 反论 1：公共面规则会不会让内容区设计任务膨胀成整站改造？

回应：规则要求先分类交付表面。`content-only` 可以只做内容区，但必须明示非目标；`inside-existing-shell` 只复用现有壳层，不重做整站；只有 `full-page-with-shell` 才补必要公共面。

### 反论 2：设计稿没画的公共区域，Agent 会不会凭空发明？

回应：规则要求从仓库现有 shell、项目文档、已接受实现或组件系统推断；推断不了才问一个会改变范围的问题。禁止视觉猜测式发明。

### 反论 3：cursor、hover、focus 等细节会不会太琐碎？

回应：这些是用户判断“哪里能点”和“点了有没有反馈”的基础。它们不要求复杂业务逻辑，只要求演示级 UI affordance 和反馈闭环。

### 反论 4：移动端触控尺寸会不会和高密度后台设计冲突？

回应：规则不写死单一像素值，要求遵循目标设计系统密度，同时保证可触达、不遮挡、可关闭和不依赖 hover-only。

### 反论 5：补交互会不会诱导 Agent 写过多前端业务状态？

回应：规则明确交互只闭合 UI/demo 范围；mock 阶段仍受 Mock/BFF Boundary Contract 约束，不提前实现领域裁定或 API 状态机。

## 验收标准

- `design-to-frontend-delivery` quick_validate 通过。
- 全量 skills quick_validate 通过。
- README smoke case 覆盖“设计稿只画业务内容区”和“页面像但不知道哪里能点”。
- 安装版包含 `Common Surface Contract`、`Interaction Affordance Contract`、最小执行合同、公共面健康度和交互 affordance 审计。
