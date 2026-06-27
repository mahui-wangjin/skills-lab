# Convert and Polish

## 1. 开始前基线确认（闸门 1）

开始实现前必须明确：

- 当前模式已锁定为 `convert-and-polish`
- 目标端（React / Vue / 静态 HTML-H5 / 小程序 / 同类前端）
- 基线工件及其标识（例如导出 HTML 包、设计工具代码快照、参考提交号或版本标签）
- 结构化源检查结果（例如平台 Dev Mode/MCP 上下文、设计工具生成代码、导出 HTML/CSS、tokens、组件映射、参考代码是否可用）
- 结构事实源（默认 HTML/设计工具代码）
- 工程目录约定：路由/页面入口、feature/module、components、mock/fixtures、styles/tokens、assets、tests/stories 的现有归属
- 复刻范围与非目标项
- 是否保留宿主壳层（Header/Footer/Layout/Router）

若输入来自设计平台链接、插件、MCP、设计导出或生成代码，必须先按 `source-priority` 执行 Structured Source Gate。能获得结构、样式属性、tokens、组件映射、参考代码或导出 HTML/CSS 时，不得降级为按截图复刻。

若结构化源不可用且只剩视觉稿，先走 `source-priority` 的仅视觉降级确认，不直接开工。

## 2. Structured-source-first 结构映射

先做结构复刻，再做体验精修：

1. 按最强结构化事实源对齐页面区块、层级、主流程入口、弹框挂载点。
2. 只做最小工程化改写（语法迁移、循环渲染、资源路径与类型接线）。
3. 不为“更工程化”主动重组 DOM、重写文案、重设计交互层级。
4. 截图或下载图只用于视觉验收、差异检查或位图资产提取，不作为结构来源替代可读的结构化源。

## 3. Layout-fidelity-first 布局策略

结构事实源通过后，先定义可维护布局策略，再写样式：

1. 将设计工具的 auto-layout、constraints、grid、spacing、tokens、variants 翻译为 Flexbox、CSS Grid、正常文档流、响应式约束、`aspect-ratio` 和项目组件。
2. 把用户说的“1:1”“像设计稿”“pixel-perfect”理解为视觉关系目标：间距、对齐、字体层级、颜色、密度、状态和交互行为尽量一致，而不是复制 `x/y` 坐标。
3. 普通页面的主布局区域、重复卡片/行、响应式列、表单、仪表盘和内容流不得由 `position: absolute`、`left/top`、固定像素坐标或截图叠层驱动。
4. 绝对定位只允许用于浮层、popover、tooltip、badge、floating action、装饰叠层、canvas/game/diagram 或稳定容器内的小型锚定元素。
5. 若视觉接近度只能靠大量绝对定位达成，停止实现并改为 Flex/Grid/flow 结构；确需例外时在 Gate 2 记录范围、原因和响应式风险。

## 4. 保留工程壳层时只替换内容区

当用户或宿主约束要求保留公共壳层时：

- 保留壳层边界与宿主路由框架。
- 仅替换页面内容区，不改共享 Header/Footer/Layout/Router 规则。
- 壳层与内容区冲突时先确认边界，不静默改壳。

## 5. 工程目录与职责边界

设计落地必须进入目标框架和当前工程的目录体系，而不是把所有内容堆到一个文件夹或一个页面文件里：

1. 先识别当前项目的框架约定和本地样板：路由/页面入口放哪里，feature/module 如何组织，组件、fixtures、样式、assets、测试分别在哪里。
2. 页面入口只做路由接入和页面级编排；大块 UI 拆到 feature-private 组件；跨页面复用组件进入项目已有共享组件位置。
3. mock/fixture 数据放到项目已有数据夹具位置，或放在 feature-local data/fixtures 文件中；不要把大段 mock 数组塞进页面 JSX。
4. 薄展示选择器、格式化、tab key 校验、fixture 查询等放到 feature-local model/selectors/formatters 等现有命名体系中；不要把它们升级成领域 reducer 或 API 状态机。
5. 样式、tokens、assets 和 tests/stories 按目标框架与项目约定归位；没有现成约定时，先按框架官方或事实标准选择最小目录结构，并记录该选择。
6. 一次性静态 HTML 且无宿主工程时可以自包含，但仍要在文件内部区分数据、渲染、样式和交互，不把这种临时结构推广到真实工程。

## 6. Mock/BFF 边界

若本轮是静态页、原型页、视觉精修或 mock 数据交付：

1. mock 数据只作为展示夹具，可以模拟未来 BFF 响应形状，便于后续替换数据来源。
2. 前端只保留轻量 UI 状态：当前 tab、选中项、展开项、弹框开关、本地表单草稿，以及 loading/error/empty 的演示表面。
3. 前端可以实现演示级基础校验和格式反馈，但这只能是 UI 反馈，不能升级成授权、资格或工作流裁定。
4. 只允许很薄的展示选择器：按 id 取 fixture、校验 tab key、统计已给定列表数量、把 fixture 字段传给组件。
5. 不在前端 mock 阶段实现 BFF/API 的领域裁定：派生业务指标、生命周期/状态流转、授权/资格、可执行动作裁定、集成状态归一化、基于业务枚举组合推导领域文案、目标去向和跨记录工作流。
6. 不为静态页面引入假的 API 状态机、轮询、缓存、乐观更新、重试策略、权限引擎或领域 reducer。

若用户明确要求真实 API/BFF 接入，必须把范围从“设计落地/静态 mock”切换为“接口集成”，并先确认契约来源、加载/错误/空态、mutation 副作用、缓存策略、鉴权假设和验证路径。

## 7. 结构复刻通过后再进入精修（闸门 2）

结构阶段通过前，不进入交互精修。闸门 2 至少确认：

- 结构映射已完成，主流程可走通
- 关键文案、图片、按钮入口、弹框挂载点到位
- 无明显“按截图重设计”或“下载图替代结构化源”痕迹
- 布局策略已记录，普通布局优先 Flex/Grid/flow，无大量绝对定位复刻坐标
- 绝对定位例外已记录用途、边界和响应式风险
- 工程目录边界已记录：页面入口、feature 组件、mock/fixtures、selectors/formatters、styles/assets、tests/stories 未混堆
- mock/BFF 边界已记录：本轮是静态夹具、BFF-shaped fixture、还是明确 API 集成；未把业务裁定写进 mock 页面

产出：结构差异清单 + 精修页面批次。

## 8. 精修与交付（闸门 3）

结构通过后按八层模型补齐布局、数据边界、交互、校验、状态与表现，直至达到演示标准。
最终只交付一份单目标前端结果，不并行产出多端版本。
