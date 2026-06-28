# Delivery Checklists

## 1. 八层精修模型

所有页面按八层检查，不得只修样式：

1. 结构层：页面分区、DOM 层级、UI layer ownership、壳层接入、公共面复用、路由串联
2. 布局层：Flex/Grid/正常文档流、响应式约束、间距节奏、对齐关系、绝对定位例外
3. 内容层：文案、图片、图标、媒体、按钮归属、标题标签、资源来源
4. 交互层：语义控件、cursor/hover/active/focus-visible、点击反馈、展开收起、弹框/抽屉/toast/confirm 开合、键盘/触控、联动与返回路径
5. 数据边界层：静态 fixture、BFF-shaped mock、真实 API 集成、前端 UI 状态、BFF/domain-owned 状态
6. 校验层：必填/格式、错误提示、禁用态、提交与失败重试
7. 状态层：加载/空态/成功/失败/不可操作/角色差异
8. 表现层：字体实际加载、颜色、圆角、阴影、动效节奏、过渡一致性、反馈清晰度

## 2. 三道闸门检查项与产出

### 闸门 1：开始前确认

检查项：

- 模式已锁定（`convert-and-polish` 或 `polish-existing-project`）
- 目标端明确（或沿用既有工程栈）
- 设计基线与事实源明确
- 若输入来自设计平台、插件/MCP、导出包或生成代码，已执行结构化源检查：结构/样式属性、tokens、组件映射、参考代码、导出 HTML/CSS 是否可用
- 已确认未把可读结构化源降级为截图、下载图或纯视觉猜测
- 已确认“1:1 / pixel-perfect / 像设计稿”只表示高保真视觉关系目标，不表示像素级 100% 承诺，也不表示按设计稿坐标绝对定位复刻
- 已确认 UI layer map：app shell、page frame、content sections、collection items、local controls、overlay/feedback、decoration/media、data/state 的 owner、边界、状态归属和 stacking/clipping 风险明确
- 已确认交付表面：`content-only`、`inside-existing-shell` 或 `full-page-with-shell`
- 已确认公共面决策：现有 shell、顶部栏、侧边栏/导航、面包屑、页签、工具栏、全局 modal/drawer/confirm/toast roots、loading/empty/error 模式复用或非目标边界明确
- 已确认最小执行合同：本轮做什么、复用什么、主交互和状态、最小闭环层级、非目标、是否仍有唯一阻塞问题
- 已确认目标框架和项目目录约定：route/page、feature/module、components、mock/fixtures、selectors/formatters、styles/assets、tests/stories 的归属清晰；若无现成约定，已按框架官方或事实标准记录最小结构
- 已确认字体与资源清单：关键字体 family/weight/style/变量轴、图片/图标/媒体、tokens、资源来源、项目可访问性、授权/来源状态（已知时）和缺失项 fallback/blocked 决策
- 已确认高保真不依赖本机字体：关键字体必须来自项目可访问资源、批准 provider 或明确系统 fallback；缺失字体/字重时不得继续用微调掩盖
- 已确认本轮数据范围：静态 fixture / BFF-shaped mock / 真实 API 集成；若不是 API 集成，已确认不实现 API 状态机或业务裁定
- 已确认自测路径：项目已有 E2E/smoke/browser/screenshot/Storybook 命令，或无现成命令时的最小真实浏览器验收路径
- 范围与非目标明确
- 壳层是否保留明确

产出：

- 本轮执行声明（做什么 / 不做什么）
- 结构化源检查记录（若适用）：尝试的来源、可用性、最终基线

### 闸门 2：模式化中段闸门

检查项：

- `convert-and-polish` 路径：
- 结构映射完成，关键页面区块无错位
- UI 层级归属正确：page title/breadcrumbs/tabs/toolbar/filter 不落入错误内容卡片；repeated item 不拥有页面级状态；overlay/feedback 接正确 root；decoration/media 不遮挡交互层
- 壳层边界正确，内容区替换范围正确
- 交付表面与公共面复用正确：未因设计稿缺少公共区域而漏接现有 shell、导航、面包屑、工具栏或统一 overlay/feedback roots；若为 content-only，已明确非目标
- 文案、图片、入口、弹框挂载点到位
- 主流程与路由可走通
- 可交互对象已完成 affordance 审计：语义元素/组件、cursor、hover、active/pressed、focus-visible、disabled、loading/submitting、selected/current、移动端触控和键盘路径符合项目范式
- 弹框、抽屉、popover、confirm、toast 已覆盖打开、关闭、取消/确认、失败反馈和返回主任务路径
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
- 现有 UI layer ownership 已审计；shell/page frame/content/repeated item/local control/overlay/decoration/data-state 的错层、状态错主、portal/z-index/overflow 问题已列入差距清单或修复范围
- 现有工程目录健康度已审计；混堆的页面入口、组件、fixtures、展示选择器、样式或测试已列入差距清单或修复范围
- 现有布局健康度与绝对定位审计已完成；坐标式布局风险已列入差距清单或修复范围
- 现有字体与资源健康度已审计；本机字体依赖、缺失字重、资源 404、placeholder、截图替代 UI 等风险已列入差距清单或修复范围
- 现有 mock/API 边界已审计；静态展示阶段不应承担的业务裁定已列入差距清单或修复范围
- 现有公共面健康度已审计；shell、导航、页面工具栏、modal/drawer/toast/confirm roots、loading/empty/error 模式的复用或缺口已列入差距清单
- 现有交互可用性已审计；点击目标、语义控件、cursor、hover/active/focus、禁用/加载、弹层关闭、移动端触控和返回路径缺口已列入差距清单
- 点名范围与目标结果差距清单已明确
- 最小闭环建议与本轮实施边界已确认
- 若用户不扩围，风险与剩余差距已明确记录

产出：

- `convert-and-polish`：结构差异清单 + UI layer map + 交付表面/公共面决策 + 交互 affordance 审计 + 工程目录边界 + 布局策略与绝对定位审计 + 字体/资源清单 + mock/BFF 边界 + 进入精修的页面批次
- `polish-existing-project`：现状审计快照 + UI layer ownership 健康度 + 公共面健康度 + 交互可用性健康度 + 字体/资源健康度 + 差距闭环决议 + 进入实施的页面批次

### 闸门 3：精修验收通过

检查项：

- 八层精修覆盖达到本轮目标
- 主流程可演示（能看、能点、能识别哪里可点、能键盘/触控基本操作、能校验、有反馈、有状态、能关闭弹层并返回）
- 公共面与交付表面符合 Gate 1：content-only 不冒充 full page；inside-existing-shell 复用已接受 shell；full-page-with-shell 覆盖必要导航、反馈和 overlay roots
- UI layer ownership 符合 Gate 1：组件属于正确层级，状态 owner 清晰，page frame/content/repeated item/overlay/decoration/data-state 不错位，z-index/portal/overflow 没有掩盖错层
- 新增文件遵循目标框架和项目目录约定；页面入口、组件、fixtures、展示选择器、样式/assets 和测试职责边界清晰
- 设计还原以视觉关系一致为准：间距、对齐、字体层级、颜色、圆角、阴影、密度、状态接近设计稿；无为了坐标复刻牺牲响应式与可维护性
- 关键字体与资源已在真实浏览器中验证：字体 family/weight/style 实际加载，图片/图标/媒体无 404 或未披露 placeholder；截图或视觉比对在字体与关键资源加载后执行
- 若关键字体或资源缺失，验收结论只能是条件通过或未通过，并写明 pending asset / fallback 视觉风险；不得把交付结论写成 pixel-perfect 或像素级 100%
- 静态 mock 阶段未实现 BFF/API 业务状态机；真实 API 集成若在范围内，已明确契约来源、加载/错误/空态、mutation 副作用、缓存策略、鉴权假设和验证路径
- 校验与反馈闭环完整（必填/格式、错误反馈、禁用态、加载/提交中、弹框/抽屉/toast/confirm 开合闭环）
- 可交互元素 affordance 完整：真实 click targets 有语义、cursor、hover/active/focus-visible；disabled/non-clickable 不伪装可点击；移动端触控目标不遮挡、不溢出、可关闭
- E2E/真实浏览器自测已执行并覆盖主流程、公共面、UI 层级、主要交互、弹层、桌面/窄屏或移动视口、console errors、failed requests、字体和关键资源加载
- 若 E2E/真实浏览器自测未执行，验收结论只能是条件通过或 self-reviewed，并写明未验收原因与人工检查清单；不得声称 demo-ready 完成
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

- 模式：<convert-and-polish | polish-existing-project>
- 目标端：<React | Vue | 静态 HTML-H5 | 小程序 | 其他>
- 本轮范围：<页面/模块 + 完成层级>
- 事实源：<结构化源/参考代码/导出 HTML/已接受实现/视觉降级 + 是否做过结构化源检查>
- UI 层级：<layer map + owner/state/portal/stacking/clipping 决策>
- 交付表面：<content-only | inside-existing-shell | full-page-with-shell + 公共面复用/非目标边界>
- 交互可用性：<语义控件、cursor、hover/active/focus-visible、disabled/loading、弹框/抽屉/toast/confirm、键盘/触控与返回路径验收>
- 工程结构：<目标框架/项目目录约定 + 页面入口、组件、fixtures、selectors/formatters、styles/assets、tests/stories 归属>
- 布局策略：<Flex/Grid/flow 优先 + 绝对定位例外与风险；无则写“无例外”>
- 字体与资源：<关键字体/字重/图片/图标/媒体来源 + 实际加载验证 + fallback/blocked 风险>
- 数据边界：<静态 fixture | BFF-shaped mock | 真实 API 集成；前端 UI 状态与 BFF/domain-owned 状态边界>
- 自测证据：<E2E/smoke/browser/screenshot 命令或手工浏览器路径 + 覆盖内容 + 未验收项>
- 闸门结果：
  - Gate 1：<通过/未通过 + 关键确认项>
  - Gate 2：<通过/未通过 + 路径对应摘要（结构复刻或审计闭环）>
  - Gate 3：<通过/条件通过/未通过 + 精修覆盖摘要>
- 文档更新记录：<变更文件/同步情况；无则写“无”>
- 未完成与风险：<列表>
- 最小闭环下一步：<建议>
```
