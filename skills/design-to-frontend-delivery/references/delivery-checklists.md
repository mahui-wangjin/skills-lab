# Delivery Checklists

## 1. 八层精修模型

所有页面按八层检查，不得只修样式：

1. 结构层：页面分区、DOM 层级、UI layer ownership、框架布局发现、页面范式选择、组件体系映射、壳层接入、公共面复用、路由串联
2. 布局层：app shell/route layout/page wrapper/content slot/scroll container 复用、Flex/Grid/正常文档流、响应式约束、间距节奏、对齐关系、绝对定位例外、无 parallel page-local layout、无 page-local token scale
3. 内容层：文案、图片、图标、媒体、按钮归属、标题标签、可见元素清单、资源来源、长文本/空值/格式化字段、不得自造已有远端/项目资产
4. 交互层：语义控件、cursor/hover/active/focus-visible、点击反馈、展开收起、弹框/抽屉/toast/confirm 开合、表格/列表 pattern、表单/校验 pattern、键盘/触控、联动与返回路径、状态细节来源
5. 数据边界层：静态 fixture、BFF-shaped mock、真实 API 集成、前端 UI 状态、BFF/domain-owned 状态、route/menu/permission ownership、数据规模与性能策略、后续 API/功能变更影响面
6. 校验层：必填/格式、错误提示、禁用态、提交与失败重试
7. 状态层：加载/空态/成功/失败/不可操作/角色差异
8. 表现层：字体实际加载、颜色、border、divider、padding、圆角、阴影、动效节奏、过渡一致性、反馈清晰度、设计 token 映射和可见元素浏览器对账

## 2. 三道闸门检查项与产出

### 闸门 1：开始前确认

检查项：

- 模式已锁定（`convert-and-polish`、`polish-existing-project` 或 `frontend-continuation`）
- 目标端明确（或沿用既有工程栈）
- 设计基线与事实源明确
- 若输入来自设计平台、插件/MCP、导出包或生成代码，已执行结构化源检查：结构/样式属性、tokens、组件映射、参考代码、导出 HTML/CSS 是否可用；Figma 场景已优先尝试目标 node/selection/frame 的 Dev Mode/MCP/Code Connect 上下文
- 已确认未把可读结构化源降级为截图、下载图或纯视觉猜测
- 已确认没有把整张 Figma 文件/页面/canvas 图片下载或渲染作为默认第一步；如使用整图，已记录用户明确要求或结构化源不可访问的原因
- 已确认“1:1 / pixel-perfect / 像设计稿”只表示高保真视觉关系目标，不表示像素级 100% 承诺，也不表示按设计稿坐标绝对定位复刻
- 已确认 framework layout discovery：现有 app shell、route layout、page wrapper、content slot、scroll container、sticky/fixed 区域、page title/breadcrumbs/tabs、toolbar/action area、filter/search region、overlay roots、grid/spacing/breakpoints、loading/empty/error surfaces 和同类 page pattern samples 已盘点
- 已确认 responsive foundation：固定设计画布、多页面 UI、dashboard/workbench、shell/page-frame 或响应式缺陷已记录 viewport/container 口径、canvas policy、layout primitives、query policy、tokenized spacing/gaps、任意值策略、固定值例外和验收矩阵；具体屏幕尺寸只作代表样本，不作通用规则
- 已确认页面范式与布局实现方案：list/detail/create-edit/dashboard-workbench/wizard/settings-configuration/approval-workflow/graph-canvas/monitoring-logs/report-analytics/search-selection 或项目已有 archetype；已记录 pattern seed/reuse/variant/new reusable primitive/approved exception
- 已确认 layout primitive reuse：已有 route layout/page container/content slot/scroll root/toolbar/tabs/breadcrumbs/overlay root/table-list-form shell 能承载时，不自造 page-local 替代物
- 已确认 component system mapping：button/card/tabs/table/list/modal/drawer/popover/tooltip/toast/confirm/form/field/menu/filter/search/status/chart/icon 等设计元素已映射到项目组件、组件 variant、headless primitive、token 或 approved exception
- 已确认 token/theme system：颜色、typography、spacing、radius、shadow、density、motion、breakpoints 和 component variants 使用项目 theme/CSS variables/design tokens/utility config 或 approved fallback；无页面级自造 scale
- 已确认 route/menu/permission ownership：page title、breadcrumbs、menu active、return path、route guard、permission-driven actions、hidden/disabled behavior 接入项目体系或明确非目标
- 已确认 table/list pattern：筛选区、工具栏、列设置、分页、排序、批量操作、行操作、详情入口、loading/empty/error 和窄屏策略使用项目 pattern 或记录例外
- 已确认 form/validation pattern：form state、field binding、schema/validation、错误提示、提交中、禁用态、接口错误映射、成功/失败反馈和返回/重置路径使用项目 pattern 或记录例外
- 已确认 state/data/performance matrix：loading/empty/error/permission denied/disabled/submitting/success/failure、长文本、空值、长列表、真实格式化字段、预期数据量、分页/虚拟列表/懒加载、图表/canvas 渲染成本已记录
- 已确认 UI layer map：app shell、page frame、content sections、collection items、local controls、overlay/feedback、decoration/media、data/state 的 owner、边界、状态归属和 stacking/clipping 风险明确
- 已确认交付表面：`content-only`、`inside-existing-shell` 或 `full-page-with-shell`
- 已确认公共面决策：现有 shell、顶部栏、侧边栏/导航、面包屑、页签、工具栏、全局 modal/drawer/confirm/toast roots、loading/empty/error 模式复用或非目标边界明确
- 已确认最小执行合同：本轮做什么、复用什么、主交互和状态、最小闭环层级、非目标、是否仍有唯一阻塞问题
- 已确认目标框架和项目目录约定：route/page、feature/module、components、mock/fixtures、selectors/formatters、styles/assets、tests/stories 的归属清晰；若无现成约定，已按框架官方或事实标准记录最小结构
- 已确认字体与资源清单：关键字体 family/weight/style/变量轴、图片/图标/媒体、tokens、资源来源、项目可访问性、授权/来源状态（已知时）和缺失项 fallback/blocked 决策
- 已确认图标与细节清单：远端/设计源/项目资产中已有图标、SVG、插画、logo、装饰形状、border/padding/radius/shadow/motion 和状态 variants 的来源明确；缺失时已记录 ask/fallback/blocked
- 已确认可见元素保真清单：关键 icons/buttons/links/tabs/chips/badges/progress/list rows/table rows/borders/dividers/status labels/text/counts/state variants 已建立 source -> implementation 映射；重复组已记录预期数量和代表性 variants
- 已确认高保真不依赖本机字体：关键字体必须来自项目可访问资源、批准 provider 或明确系统 fallback；缺失字体/字重时不得继续用微调掩盖
- 已确认本轮数据范围：静态 fixture / BFF-shaped mock / 真实 API 集成；若不是 API 集成，已确认不实现 API 状态机或业务裁定
- 若本轮是后续 API/功能/bugfix 变更，已确认 accepted baseline、API/行为契约来源、影响面、回归面和不影响的页面/组件
- 已确认真实浏览器验收路径：项目已有 E2E/agent-browser/Playwright/Cypress/browser automation/浏览器驱动截图或 trace/Storybook-in-browser 命令，或无现成命令时的最小真实浏览器验收路径；smoke 只作为健康检查
- 已确认 AI 浏览器验收预算：最小真实浏览器验收可直接执行；若进入跨多路由/多视口/多轮视觉 diff/大范围回归/登录或第三方流程/慢速远端环境等高成本 AI 探索式 E2E，已向用户确认覆盖范围、时间或 token 成本、停止条件和人工复核项
- 范围与非目标明确
- 壳层是否保留明确

产出：

- 本轮执行声明（做什么 / 不做什么）
- 结构化源检查记录（若适用）：尝试的来源、可用性、最终基线

### 闸门 2：模式化中段闸门

检查项：

- `convert-and-polish` 路径：
- 结构映射完成，关键页面区块无错位
- framework layout/page archetype pass 已完成，页面运行位置、page wrapper、content slot、scroll container、toolbar/tabs/breadcrumbs、overlay roots、grid/spacing/breakpoints 归属清晰
- responsive foundation pass 已完成；页面未散写新的私有断点、固定列宽、固定高度补丁、任意像素 utility、整页缩放或 spacing scale，例外已记录 owner、范围和风险；重复出现的值已上收为 token、variant、layout primitive 或 framework config
- 已记录 pattern seed/reuse 决策；同类页面不再各自自造 layout 方案，必要 variant/new primitive/exception 有理由
- 未使用 page-local shell/container/grid/spacing scale/scroll root/toolbar/tabs/breadcrumb/table-list-form shell/overlay root 替代已有项目或框架 primitive
- component-system pass 已完成；通用 UI、table/list、form/validation、overlay/feedback 和 chart/canvas 没有被页面级自造为并行体系
- token/theme pass 已完成；没有新造 page-local color/spacing/radius/shadow/density/breakpoint scale
- route/menu/permission、table/list、form/validation、state/data/performance pass 已完成；状态矩阵、真实数据压力、数据规模和窄屏策略不留到 Gate 3 才发现
- UI 层级归属正确：page title/breadcrumbs/tabs/toolbar/filter 不落入错误内容卡片；repeated item 不拥有页面级状态；overlay/feedback 接正确 root；decoration/media 不遮挡交互层
- 壳层边界正确，内容区替换范围正确
- 交付表面与公共面复用正确：未因设计稿缺少公共区域而漏接现有 shell、导航、面包屑、工具栏或统一 overlay/feedback roots；若为 content-only，已明确非目标
- 文案、图片、入口、弹框挂载点到位
- 主流程与路由可走通
- 可见元素保真清单已完成实现映射：关键 icons/buttons/links/tabs/chips/badges/progress/list rows/table rows/borders/dividers/status labels/text/counts/state variants 已映射到代码、项目 token、资源路径或已披露 fallback/blocked
- 可交互对象已完成 affordance 审计：语义元素/组件、cursor、hover、active/pressed、focus-visible、disabled、loading/submitting、selected/current、移动端触控和键盘路径符合项目范式
- 弹框、抽屉、popover、confirm、toast 已覆盖打开、关闭、取消/确认、失败反馈和返回主任务路径
- 图标与细节保真已完成：已有远端/项目图标未被自绘、替换、截图化；border、padding、radius、shadow、state variants 和 motion 使用设计源、项目 token 或已记录 fallback
- 无未经授权的再设计
- 无下载图/截图替代结构化事实源的降级
- 已完成布局策略记录：普通页面、卡片、列表、表单、仪表盘和内容布局优先 Flex/Grid/flow
- 已完成 stacking/clipping 审计：z-index、portal root、sticky/fixed、overflow、tooltip/popover anchor、drawer/modal root 不用来掩盖错误组件归属
- 已完成绝对定位审计：主布局区域、重复卡片/行、响应式列、表单、仪表盘和内容流未由 absolute/fixed 坐标驱动；仅存在浮层、tooltip、badge、floating action、装饰叠层、canvas/game/diagram 或小型锚定元素等有边界例外
- 已完成工程目录边界记录：页面入口、feature-private 组件、共享组件、mock/fixtures、selectors/formatters、styles/assets、tests/stories 按目标框架和项目约定归位，未把整页实现、mock、选择器、样式和测试混堆到一个文件夹或一个大文件
- 已完成 mock/BFF 边界记录：mock 数据只作为展示夹具或 BFF-shaped fixture；前端只保留轻量 UI 状态、薄展示选择器和演示级基础校验；派生业务指标、生命周期/状态流转、授权/资格、可执行动作裁定、集成状态归一化、基于业务枚举组合推导领域文案、目标去向等 BFF/domain-owned 决策未在前端 mock 中推导
- 已完成字体与资源清单：关键字体/字重/图片/图标/媒体已接入项目资源或批准 provider；缺失项已明确 blocked/fallback，不继续无效视觉微调
- 已完成浏览器验收计划：最终截图、视觉比对或人工核对将在 `document.fonts.ready`/同等加载确认后执行，并检查字体/图片/媒体 404
- `polish-existing-project` 路径：
- 现状审计快照已完成（八层覆盖、壳层约束、阻塞项）
- 现有 framework layout/page archetype 健康度已审计；偏离项目/框架 route layout、page wrapper、content slot、scroll container、toolbar/tabs/breadcrumb pattern、overlay root 或同类页面范式的成本已列入差距清单
- page-local layout 风险已审计；每页自造 shell/container/grid/scroll/toolbar/table-list-form shell 等问题已修复、列入修复范围或记录为例外
- 现有 component system 健康度已审计；页面级自造 button/card/tabs/table/list/modal/form/toast/confirm/tooltip/status/chart/icon 等问题已修复、列入修复范围或记录例外
- 现有 token/theme 健康度已审计；page-local color/spacing/radius/shadow/density/breakpoint scale 风险已修复、列入修复范围或记录例外
- 现有 route/menu/permission、table/list、form/validation、state/data/performance 健康度已审计；硬编码导航/权限、并行表格/表单状态机、缺状态矩阵、长文本/空值/数据量/性能风险已列入差距清单
- 现有 UI layer ownership 已审计；shell/page frame/content/repeated item/local control/overlay/decoration/data-state 的错层、状态错主、portal/z-index/overflow 问题已列入差距清单或修复范围
- 现有工程目录健康度已审计；混堆的页面入口、组件、fixtures、展示选择器、样式或测试已列入差距清单或修复范围
- 现有布局健康度与绝对定位审计已完成；坐标式布局风险已列入差距清单或修复范围
- 现有字体与资源健康度已审计；本机字体依赖、缺失字重、资源 404、placeholder、截图替代 UI 等风险已列入差距清单或修复范围
- 现有图标与细节 token 健康度已审计；自绘图标、错用图标库、丢失 hover/focus/disabled/loading、随意改圆角/尖角、padding/radius/shadow/motion 脱离 token 等风险已列入差距清单或修复范围
- 现有可见元素差距已审计；漏图标、漏按钮、漏 tabs/chips/progress、漏列表/表格行、漏边框/分割线、状态标签/关键文案缺失、数量不一致或不可见等风险已列入差距清单或修复范围
- 现有 mock/API 边界已审计；静态展示阶段不应承担的业务裁定已列入差距清单或修复范围
- 现有公共面健康度已审计；shell、导航、页面工具栏、modal/drawer/toast/confirm roots、loading/empty/error 模式的复用或缺口已列入差距清单
- 现有交互可用性已审计；点击目标、语义控件、cursor、hover/active/focus、禁用/加载、弹层关闭、移动端触控和返回路径缺口已列入差距清单
- 点名范围与目标结果差距清单已明确
- 最小闭环建议与本轮实施边界已确认
- 若用户不扩围，风险与剩余差距已明确记录
- `frontend-continuation` 路径：
- accepted baseline 已确认，不把未确认 WIP 当作保留基线
- 变更类型已确认：API/BFF integration、functional change、bug fix、regression fix 或 mixed
- API/行为契约来源已确认：schema/OpenAPI/BFF route/typed client/mock contract/用户决策/现有代码
- 影响面已列出：routes/pages、shared components、hooks、store/query cache、API clients、tokens/assets、fixtures、tests/stories、browser flows
- 回归面已列出：受共享变更影响的其他页面、组件、故事、测试和关键路径
- 已确认不会用 API/bugfix 任务顺手替换图标、改 token、重设计 shell、打乱 UI layer ownership 或改变无关页面
- 已确认使用项目既有 API client、query/cache、form、validation、loading/empty/error、toast/confirm 和权限模式；若新增模式，原因明确
- 已确认组件与 API/BFF/domain 边界：展示组件不承担生命周期、权限、资格、重试策略、跨记录 workflow 等领域裁定
- 自测/回归路径已明确，至少覆盖被改路径和受影响消费者

产出：

- `convert-and-polish`：结构差异清单 + UI layer map + 交付表面/公共面决策 + 可见元素保真清单与实现映射 + 交互 affordance 审计 + 工程目录边界 + 布局策略与绝对定位审计 + 字体/资源/图标/细节 token 清单 + mock/BFF 边界 + 进入精修的页面批次
- `polish-existing-project`：现状审计快照 + UI layer ownership 健康度 + 公共面健康度 + 可见元素差距清单 + 交互可用性健康度 + 字体/资源/图标/细节 token 健康度 + 差距闭环决议 + 进入实施的页面批次
- `frontend-continuation`：accepted baseline + API/行为契约来源 + 影响面 + 回归面 + 共享消费者 + 自测/回归计划 + 不变更边界

### 闸门 3：精修验收通过

检查项：

- 八层精修覆盖达到本轮目标
- 主流程可演示（能看、能点、能识别哪里可点、能键盘/触控基本操作、能校验、有反馈、有状态、能关闭弹层并返回）
- 公共面与交付表面符合 Gate 1：content-only 不冒充 full page；inside-existing-shell 复用已接受 shell；full-page-with-shell 覆盖必要导航、反馈和 overlay roots
- 框架布局方案符合 Gate 1：页面在选定 app shell/route layout/page wrapper/content slot/scroll container 中运行；toolbar/tabs/breadcrumbs/filters/overlays/grid/spacing/breakpoints 与选定 page archetype 一致；没有未经记录的 parallel page-local layout
- 响应式基座符合 Gate 1：代表性 viewport/container 下无非预期横向溢出、重叠、错层、不可关闭 overlay 或不可读文本；任意值、固定值和比例缩放例外与记录一致，且没有用每元素高度补丁掩盖缺失的布局规则
- 组件与 token 体系符合 Gate 1：通用组件、表格/列表、表单/校验、弹层/反馈、图表/画布和 token/theme 复用项目 pattern 或 approved exception；没有未经记录的 page-local 并行体系
- route/menu/permission、状态矩阵、真实数据压力和性能策略符合 Gate 1：长文本、空值、长列表、真实格式化字段、loading/empty/error/permission denied/submitting/failure、分页/虚拟列表/懒加载或图表/canvas 成本已在浏览器或等效路径核对
- UI layer ownership 符合 Gate 1：组件属于正确层级，状态 owner 清晰，page frame/content/repeated item/overlay/decoration/data-state 不错位，z-index/portal/overflow 没有掩盖错层
- 新增文件遵循目标框架和项目目录约定；页面入口、组件、fixtures、展示选择器、样式/assets 和测试职责边界清晰
- 设计还原以视觉关系一致为准：间距、对齐、字体层级、颜色、圆角、阴影、密度、状态接近设计稿；无为了坐标复刻牺牲响应式与可维护性
- 图标和细节没有自造：已有远端/设计源/项目图标按来源复用，border/padding/radius/shadow/motion/state variants 来自设计源、项目 token/组件 variant 或已披露 fallback
- 可见元素清单已在浏览器中对账：关键图标、按钮、链接、tabs、chips、badges、进度条、列表/表格行、分割线、边框容器、状态标签、关键文案/数字和状态 variants 没有遗漏、未批准替换、数量不一致、遮挡、不可见、资源 404 或文本溢出
- 关键字体与资源已在真实浏览器中验证：字体 family/weight/style 实际加载，图片/图标/媒体无 404 或未披露 placeholder；截图或视觉比对在字体与关键资源加载后执行
- 若关键字体或资源缺失，验收结论只能是条件通过或未通过，并写明 pending asset / fallback 视觉风险；不得把交付结论写成 pixel-perfect 或像素级 100%
- 静态 mock 阶段未实现 BFF/API 业务状态机；真实 API 集成若在范围内，已明确契约来源、加载/错误/空态、mutation 副作用、缓存策略、鉴权假设和验证路径
- 后续 API/功能/bugfix 变更若在范围内，已验证受影响页面、共享消费者和不应改变的页面；共享 token/component/hook/API client 变更有回归证据
- 校验与反馈闭环完整（必填/格式、错误反馈、禁用态、加载/提交中、弹框/抽屉/toast/confirm 开合闭环）
- 可交互元素 affordance 完整：真实 click targets 有语义、cursor、hover/active/focus-visible；disabled/non-clickable 不伪装可点击；移动端触控目标不遮挡、不溢出、可关闭
- E2E/真实浏览器自测已执行并覆盖主流程、公共面、UI 层级、主要交互、弹层、桌面/窄屏或移动视口、console errors、failed requests、字体和关键资源加载；smoke/unit/component/typecheck 只作为补充证据
- AI 浏览器验收结论基于可复核证据：命令结果、断言、trace、截图、console/network 日志和明确交互步骤；未把模型主观判断当作唯一验收依据
- 若 E2E/真实浏览器自测或浏览器调试未执行，验收结论只能是条件通过、self-reviewed 或代码级候选结果；必须提醒用户缺少 console/network/runtime/layout/screenshot 证据，说明需要的环境/工具/访问方式，并写明人工检查清单；不得用 smoke-only 结果声称 demo-ready 完成
- 动画克制且统一，不破坏主流程感知
- 交付相关文档记录已同步更新（若本轮有文档变更）
- 关键风险和残留项已标注
- 已明确进入下一批页面或结束当前批次
- 后续建议清晰可执行

产出：

- 验收结论（通过 / 条件通过 / 未通过）
- 风险与阻塞
- 文档更新记录
- 下一步建议

## 3. 完成时收尾输出格式

```md
### 交付收尾

- 模式：<convert-and-polish | polish-existing-project | frontend-continuation>
- 目标端：<React | Vue | 静态 HTML-H5 | 小程序 | 其他>
- 本轮范围：<页面/模块 + 完成层级>
- 事实源：<结构化源/参考代码/导出 HTML/已接受实现/视觉降级 + 是否做过结构化源检查>
- 框架布局方案：<framework layout discovery + chosen layout implementation + page archetype + seed/reuse/variant/exception decision + browser fit result>
- 响应式基座：<viewport/container model + canvas policy + layout primitives + query/token/arbitrary-value policy + fixed-value exceptions + representative browser fit result>
- 组件体系映射：<design elements -> project components/variants/tokens/headless primitives/exceptions + no parallel local systems>
- Token/theme：<theme/CSS variables/design tokens/utility config/component variants + fallback/blocked + no page-local scale>
- 路由/菜单/权限：<route meta/menu/breadcrumb/title/return path/permission/action visibility owner>
- UI 层级：<layer map + owner/state/portal/stacking/clipping 决策>
- 交付表面：<content-only | inside-existing-shell | full-page-with-shell + 公共面复用/非目标边界>
- 交互可用性：<语义控件、cursor、hover/active/focus-visible、disabled/loading、弹框/抽屉/toast/confirm、键盘/触控与返回路径验收>
- 工程结构：<目标框架/项目目录约定 + 页面入口、组件、fixtures、selectors/formatters、styles/assets、tests/stories 归属>
- 布局策略：<Flex/Grid/flow 优先 + 绝对定位例外与风险；无则写“无例外”>
- 字体与资源：<关键字体/字重/图片/图标/媒体来源 + 实际加载验证 + fallback/blocked 风险>
- 图标与细节：<图标/illustration/token 来源 + border/padding/radius/shadow/motion/state variants 映射 + fallback/blocked 风险>
- 设计元素对账：<可见元素清单 + source -> implementation 映射 + 浏览器对账结果 + missing/fallback/blocked/residual risk>
- 数据边界：<静态 fixture | BFF-shaped mock | 真实 API 集成；前端 UI 状态与 BFF/domain-owned 状态边界>
- 状态/真实数据/性能：<状态矩阵 + 长文本/空值/长列表/格式化字段 + 数据规模 + pagination/virtualization/lazy loading/chart-canvas strategy>
- 后续变更影响面：<API/功能/bugfix 基线 + 影响页面/共享消费者 + 回归覆盖；非 continuation 写“无”>
- 自测证据：<真实浏览器 E2E/agent-browser/Playwright/Cypress/browser automation/浏览器驱动截图或 trace 命令或手工浏览器路径 + smoke/单元/组件补充证据 + 覆盖内容 + AI 探索式 E2E 预算确认情况（如适用）+ 未验收项 + 若浏览器验收/调试不可用则写明用户提醒内容>
- 闸门结果：
  - Gate 1：<通过/未通过 + 关键确认项>
  - Gate 2：<通过/未通过 + 路径对应摘要（结构复刻或审计闭环）>
  - Gate 3：<通过/条件通过/未通过 + 精修覆盖摘要>
- 文档更新记录：<变更文件/同步情况；无则写“无”>
- 未完成与风险：<列表>
- 最小闭环下一步：<建议>
```
