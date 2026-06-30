# Polish Existing Project

## 1. 现状审计

先审计当前工程，但不要默认它已经是“已接受实现基线”：

- 页面与路由覆盖：哪些页面已存在、哪些流程未串通
- 八层覆盖度：结构、布局、内容、交互、数据边界、校验、状态、表现
- 项目交付画像一致性：当前实现是否符合目标 stack/runtime、route/shell owner、component system、token/theme、styling policy、copy/i18n、assets、mock/API、directory/test/story 和 browser acceptance 约定；是否混入生成代码或一次性实现带来的并行工程体系
- 设计语义图健康度：当前实现是否能追溯到 semantic regions、source components/variants、重复组、交互状态和数据角色；是否只是把生成代码或截图结构硬塞进页面
- 框架布局一致性：当前页面是否复用项目/框架已有 app shell、route layout、page wrapper、content slot、scroll container、page title/breadcrumbs/tabs、toolbar/action area、filter/search region、overlay roots、grid/spacing/breakpoints 和 loading/empty/error surfaces
- 页面范式一致性：当前实现属于 list、detail、create/edit、dashboard/workbench、wizard、settings/configuration、approval/workflow、graph/canvas、monitoring/logs、report/analytics、search/selection 或其他项目已有 page archetype；是否复用同类 pattern 或形成了未经记录的 page-local variant
- 组件体系一致性：button/card/tabs/table/list/modal/drawer/popover/tooltip/toast/confirm/form/field/menu/filter/search/status/chart/icon 是否复用项目组件、组件 variant、headless primitive 或已记录 exception；是否页面级自造通用组件
- token/theme 一致性：颜色、字体、间距、圆角、阴影、密度、动效、断点、component variants 是否来自项目 theme、CSS variables、design tokens、utility config 或 approved fallback；是否存在 page-local spacing/radius/color scale
- responsive foundation 一致性：当前实现是否有项目级 viewport/container/canvas/layout primitive/query/token/arbitrary-value/exception/acceptance 规则，还是每页散写断点、固定列宽、固定高度补丁、任意像素 utility、缩放或 spacing scale
- 路由/菜单/权限/面包屑一致性：page title、breadcrumbs、menu active、return path、route guard、permission-driven actions、hidden/disabled behavior 是否接入项目体系，还是硬编码在页面里
- 表格/列表 pattern 健康度：筛选区、工具栏、列设置、分页、排序、批量操作、行操作、详情入口、loading/empty/error 和窄屏策略是否复用项目 pattern
- 表单/校验 pattern 健康度：form state、field binding、schema/validation、错误提示、提交中、禁用态、接口错误映射、成功/失败反馈和返回/重置路径是否复用项目 pattern
- 状态/数据/性能健康度：loading、empty、error、permission denied、disabled、submitting、success、failure、长文本、空值、长列表、真实格式化字段、数据量、分页/虚拟列表/懒加载、图表/canvas 渲染成本是否已有处理
- UI 层级归属：app shell、page frame、content sections、collection items、local controls、overlay/feedback、decoration/media、data/state 的 owner 是否清晰
- 工程目录健康度：页面入口、feature/module、components、mock/fixtures、selectors/formatters、styles/assets、tests/stories 是否按当前框架和项目约定归位
- 布局健康度：普通页面、卡片、列表、表单、仪表盘和内容布局是否使用 Flex/Grid/flow、tokens 和响应式约束
- 绝对定位审计：主布局区域、重复卡片/行、响应式列、表单、仪表盘或内容流是否由 `position:absolute`、`left/top`、固定像素坐标或截图叠层驱动；若存在，判断是合理例外还是需要结构修复
- 字体与资源健康度：关键字体 family/weight/style 是否真实加载，图片/图标/媒体是否来自项目资源或批准来源，是否存在 404、placeholder、缺失字重、截图替代 UI 或仅依赖本机字体
- 图标与细节 token 健康度：图标是否复用项目图标系统/导出 SVG/组件映射，边框、内边距、圆角、阴影、hover/active/focus/disabled/loading/error/success 和动效是否来自项目 token/组件 variant，而不是手写自造
- 可见元素差距：当前实现相对设计/accepted baseline 是否漏掉图标、按钮、链接、tabs、chips、badges、进度条、列表/表格行、分割线、边框容器、关键文案/数字/状态标签或状态 variants
- mock/API 边界：当前数据是静态 fixture、BFF-shaped mock、已接 API，还是混杂不清；业务裁定是否被写进页面/组件
- 已有壳层约束：Header/Footer/Layout/Router 是否必须保留
- 公共面健康度：app layout、顶部栏、侧边栏/导航、面包屑、页签、页面工具栏、全局 modal/drawer/confirm/toast roots、loading/empty/error 模式是否复用现有项目范式
- page-local layout 健康度：是否每页自造 shell/container/grid/spacing scale/scroll root/toolbar/tabs/breadcrumb/table/list/form shell/overlay root，或把框架已有布局 primitive 复制成局部变体
- 交互可用性：可点击对象是否语义化，cursor、hover、active/pressed、focus-visible、disabled、loading/submitting、selected/current、移动端触控和键盘路径是否成立
- 当前阻塞项：缺失弹框、缺失禁用态、缺失错误反馈、不可回退路径、点击目标不明显、弹层不可关闭、公共反馈面未接入

输出一份“现状覆盖快照”，作为后续精修依据。
该快照也是本模式 Gate 2 的输入之一。

审计后还必须输出最小精修合同：

```md
Minimum polish contract:
- Accepted baseline: <current implementation evidence>
- Deliverable surface: <content-only | inside-existing-shell | full-page-with-shell>
- Project delivery profile gap: <target stack/runtime/shell/components/tokens/i18n/assets/data/directory/tests/browser conventions expected vs current implementation>
- Design intent map gap: <semantic regions/source components/repeated groups/interactions/data roles expected vs current implementation>
- Framework layout gap: <existing layout primitives/page archetype expected vs current implementation; reuse/variant/new primitive/exception decision>
- Component/token gap: <project component mapping + token/theme mapping + missing/parallel local systems>
- Responsive foundation gap: <project-level responsive contract vs page-local breakpoints/fixed tracks/fixed height patches/arbitrary pixel utilities/scale/spacing exceptions>
- Route/list/form/state-data gap: <route/menu/permission + table/list + form/validation + state matrix + data/performance risks>
- UI layer map: <owners and boundary risks for shell / page frame / content / repeated items / local controls / overlays / decoration / data-state>
- Common surfaces: <reuse / repair / out of scope>
- Asset/detail source: <icons, tokens, borders, padding, radii, shadows, motion and state variants source>
- Fidelity inventory gap: <missing or mismapped icons/buttons/tabs/chips/progress/list rows/borders/dividers/status details>
- Interaction gaps: <click targets, overlays, forms, navigation, feedback states>
- Browser acceptance path: <existing real-browser command/harness or minimum real-browser acceptance path; smoke only as health check; high-cost AI exploratory E2E budget/stop condition if needed>
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
- 若当前实现来自生成代码、导出 HTML 或一次性原型，说明哪些架构性选择必须丢弃或重映射到项目交付画像：UI library、route shell、token scale、locale shape、fixture/API client、directory/test/story 体系
- 若存在所有内容堆在一个文件或一个目录，说明页面入口、feature-private 组件、fixtures、展示选择器、样式/assets、测试应如何按当前框架约定拆开
- 若存在布局体系未复用，说明当前实现偏离了哪些项目/框架 layout primitives 或 page archetypes，以及继续保留 page-local shell/container/grid/scroll/toolbar/tabs/table/list/form shell 会带来的迁移、复用、响应式、测试和后续多页面一致性成本
- 若存在组件体系未复用，说明哪些通用组件、表格/列表、表单/校验、弹层/反馈或图表控件被页面级自造，以及继续保留会造成的交互、状态、a11y、测试和视觉一致性成本
- 若存在 token/theme 未锁定，说明哪些颜色、间距、圆角、阴影、密度、动效或断点脱离项目 token/theme，后续跨页面统一会如何变难
- 若存在路由/菜单/权限/面包屑硬编码，说明它与项目 route meta、menu schema、permission gates、return paths 和 disabled/hidden actions 的冲突成本
- 若状态/数据/性能矩阵缺失，说明 loading/empty/error/permission denied/submitting/failure、长文本、空值、长列表、格式化字段、数据规模或图表/canvas 性能会怎样破坏演示和真实接入
- 若存在 UI 层级归属错误，说明哪些组件放错层：shell/page frame/content section/repeated item/local control/overlay/decoration/data-state；谁应拥有渲染、状态、布局、overlay root 和 stacking context
- 若存在坐标式布局，说明它对响应式、内容伸缩、可维护性和后续高保真精修的影响
- 若存在字体或资源缺失，说明继续视觉微调会产生什么误判：文本宽度、换行、层级、密度、图标大小、图片裁切或截图对比都可能在真实资源补齐后改变
- 若存在图标或细节 token 缺失，说明哪些远端/项目已有图标被替换、自绘或截图化，哪些 hover、边框、padding、圆角、阴影、动效和状态样式脱离了设计源或项目范式
- 若存在可见元素清单差距，说明哪些图标、按钮、tabs、chips、badges、进度条、列表/表格行、分割线、边框容器、关键文案/数字/状态标签、状态 variants 被遗漏、数量不一致、不可见或映射到错误组件/资源
- 若存在 mock/API 混杂，说明哪些逻辑应退回 fixture/BFF 返回字段，哪些轻量 UI 状态可以留在前端
- 若设计或现状只覆盖内容区，说明是否需要接入现有 shell、导航、面包屑、页面工具栏、modal/drawer/toast/confirm roots，或把它们明确列为本轮非目标
- 若交互看得见但不好用，说明哪些点击对象缺少语义、cursor、hover/active/focus、disabled/loading、关闭/返回路径、移动端触控或反馈态

当以上差距清单与最小闭环建议被确认后，视为本模式 Gate 2 通过，再进入具体实现。

## 3. 何时建议扩到最小闭环

满足任一条件时，建议最小闭环扩围：

- 点名范围无法闭合主流程（例如能点但无法提交或无法回退）
- 点名范围只要求补页面/补设计还原，但当前工程结构会继续把页面入口、组件、mock、展示选择器、样式或测试混堆到同一文件/目录
- 点名范围只要求补视觉或交互，但当前页面未接入项目/框架已有 route layout、page wrapper、content slot、scroll container、toolbar/tabs/breadcrumb pattern、overlay root 或同类 page archetype，继续局部修会扩大后续重构/迁移成本
- 点名范围只要求还原设计，但当前页面自造 button/card/tabs/table/list/modal/form/toast/confirm/tooltip 或 validation pattern，继续精修会固化并行组件体系
- 点名范围只要求调样式，但当前页面自造 token/theme/spacing/radius/color/breakpoint scale，继续调样式会固化不可维护的局部视觉语言
- 点名范围只要求补交互，但 route/menu/permission/breadcrumb、table/list、form/validation、state matrix 或真实数据压力未对齐项目 pattern，补交互会变成局部状态机
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

实施后必须以真实浏览器验收作为主自测路径。优先运行项目已有 E2E、agent-browser、Playwright、Cypress、browser automation、浏览器驱动截图/trace 或 Storybook-in-browser 流程；smoke 只作为健康检查。AI 浏览器验收应以可复核证据为准：断言结果、trace、截图、console/network 日志和明确交互步骤，不以“模型觉得可以”作为结论。没有现成路径时，执行最小真实浏览器自测：

- 打开被精修页面和关键入口。
- 确认页面在选定 shell/route layout/page wrapper/content slot/scroll container 中运行，desktop 与窄屏/移动 viewport 下 page toolbar、tabs、breadcrumbs、filters、overlay roots、grid/spacing/breakpoints 与项目页面范式一致。
- 确认通用组件、表格/列表、表单/校验、route/menu/permission/breadcrumb、token/theme 和 overlay/feedback 复用项目 pattern；无 page-local 并行体系。
- 用长文本、空值、长列表、格式化字段和关键状态矩阵 spot-check 当前修复；数据量或图表/canvas 明显影响体验时，确认分页、虚拟列表、懒加载或渲染成本策略。
- 按可见元素差距清单对账，确认已修复的图标、按钮、tabs、chips、badges、进度条、列表/表格行、分割线、边框容器、状态标签和关键文案真实出现在浏览器中，且数量、可见性、资源加载和交互状态与设计/accepted baseline 对齐。
- 验证 UI layer ownership：shell、page frame、content、repeated item、local control、overlay/feedback、decoration/media、data/state 没有明显错层。
- 覆盖点名范围和最小闭环中的主操作、弹层开合、提交/取消、返回路径、禁用/加载/失败反馈。
- 验证图标和细节状态：远端/项目已有图标未被替换或手绘，hover/active/focus-visible/disabled/loading、border/padding/radius/shadow/motion 与设计源或项目组件范式一致。
- 检查桌面与窄屏/移动视口、console errors、failed requests、资源加载、文本溢出、遮挡、重复滚动条和 z-index/portal/overflow 问题。

最小真实浏览器自测可以由 agent 直接执行；但跨多页面/多角色/多视口的大范围回归、多轮视觉 diff 与反复精修、登录或第三方系统流程、慢速远端环境，或预计会明显增加时间/token 的 AI 探索式 E2E，必须先向用户确认目标流程、视口、证据、预计成本/时间、停止条件和人工复核项。

无法完成真实浏览器自测或浏览器调试时，必须提醒用户缺少 console/network/runtime/layout/screenshot 证据，并说明需要的环境、工具或访问方式。不得声称 demo-ready 完成；只能输出 self-reviewed/conditional 或代码级候选结果，并列出未验收路径。smoke-only 结果不能替代前端质量验收。
