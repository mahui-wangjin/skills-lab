# skills-lab

个人 skills 仓库，当前包含“前端设计落地与精修”、“通用工程决策守门”、“生产级工程交付总控”、“通用可维护性守门”、“后台管理界面范式系统”和“软件工程文档治理”六类 skill。

## Installation & Discovery

列出这个仓库里的可安装 skills：

```bash
npx skills add mahui-wangjin/skills-lab --list
```

安装指定 skill：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-frontend-delivery
```

安装 `reuse-first-guard`：

```bash
npx skills add mahui-wangjin/skills-lab --skill reuse-first-guard
```

安装 `production-delivery-manager`：

```bash
npx skills add mahui-wangjin/skills-lab --skill production-delivery-manager
```

安装 `maintainability-guard`：

```bash
npx skills add mahui-wangjin/skills-lab --skill maintainability-guard
```

安装 `admin-ui-pattern-system`：

```bash
npx skills add mahui-wangjin/skills-lab --skill admin-ui-pattern-system
```

```bash
npx skills add mahui-wangjin/skills-lab --skill documentation-governance
```

全局安装并跳过确认：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-frontend-delivery -g -y
```

```bash
npx skills add mahui-wangjin/skills-lab --skill reuse-first-guard -g -y
```

```bash
npx skills add mahui-wangjin/skills-lab --skill production-delivery-manager -g -y
```

```bash
npx skills add mahui-wangjin/skills-lab --skill maintainability-guard -g -y
```

```bash
npx skills add mahui-wangjin/skills-lab --skill admin-ui-pattern-system -g -y
```

```bash
npx skills add mahui-wangjin/skills-lab --skill documentation-governance -g -y
```

安装完成后重启 Codex，让新 skill 生效。

## Available Skills

### `design-to-frontend-delivery`

覆盖从设计输入解析、基线选择、工程转换到还原验收与精修交付的完整前端设计落地流程。

该 skill 现在采用“结构化源优先”原则：当 Figma、Stitch、Framer、Webflow 或其他设计/原型平台能够提供 Dev Mode 类属性、MCP design context、Code Connect/组件映射、tokens、样式变量、生成代码、导出 HTML/CSS 或参考实现时，必须先读取这些强事实源。截图、下载图和静态渲染图只能用于视觉验收、差异检查或位图资产提取，不能在强事实源可用时降级为按图复刻。

该 skill 同时采用“专业布局保真”原则：用户说“1:1”“pixel-perfect”“像设计稿”时，应理解为高保真视觉目标，而不是按设计稿 `x/y` 坐标复刻。普通页面的主布局区域、重复卡片/行、响应式列、表单、仪表盘和内容流必须优先使用语义结构、组件化、设计 tokens、Flexbox、CSS Grid、正常文档流和响应式约束；`position:absolute`、`left/top`、固定像素坐标只能用于浮层、badge、装饰叠层、canvas/diagram 或稳定容器内的小型锚定元素，并需要记录例外原因和响应式风险。

该 skill 还要求默认具备工程目录思维：设计落地前先识别目标框架和当前工程的路由、页面、feature/module、components、mock/fixtures、selectors/formatters、styles/tokens、assets、tests/stories 约定。页面入口只做接入和编排，组件、mock 数据、展示选择器、样式、资源和测试按职责归位；不得把整页实现、mock、状态、样式和测试堆到一个文件夹或一个大文件。若当前仓库没有约定，才按对应框架的官方或事实标准选择最小目录结构并记录原因。

该 skill 还要求区分“静态 mock 阶段”和“真实 BFF/API 集成阶段”：静态设计落地或视觉精修时，mock 数据只是展示夹具，可以做成 BFF-shaped fixture 便于未来替换；前端只保留 tab、选中项、弹框开关、loading/error/empty 等轻量 UI 状态、薄展示选择器和演示级基础校验。派生业务指标、生命周期/状态流转、授权/资格、可执行动作裁定、集成状态归一化、基于业务枚举组合推导领域文案、目标去向和跨记录工作流属于 BFF/domain-owned 决策，不应在静态 mock 页面里提前实现。

`design-to-code-html-first` 已并入 `design-to-frontend-delivery` 的 reference 层，不再作为独立 skill 维护。
旧名已不再可安装，请改用 `design-to-frontend-delivery`。

### `reuse-first-guard`

在关键开发决策前执行“先复用、再采购/集成/生成、最后才自研”的守门流程。适用于新增依赖、第三方服务、基础设施能力、新自研模块、新页面/组件/服务、重大重构，以及鉴权、支付、搜索、存储、消息、表单、上传、CMS、监控、工作流等高复用场景。

该 skill 现在把“当前工程已有实现”放在第一复用位：先找项目内现成模块、页面、组件、适配器、测试、模板、starter 或 demo，能直接复用或复制适配就不新写。只有用户明确要求新写，或项目内模式、官方能力、成熟复用路径都不匹配时，才继续讨论自研。

该 skill 现在额外强调一条稳定性规则：
当用户要“自定义 UI”时，默认只允许自定义视觉层；行为层优先复用原生浏览器能力、框架官方能力、Headless/unstyled primitives 或成熟领域库，不要顺手把通用状态机也写成自研实现。

### `production-delivery-manager`

用于用户明确点名或明确要求“生产级 / 完整生产级 / release-ready / 高确定性交付 / Leader 带团队交付 / 质量优先 / 严格交付”时的工程交付总控：先澄清需求和验收标准，再做项目检索、复用优先、工作区隔离判断、任务拆分、Delegation Quality Gate、子 Agent 分工或明确不委派理由、实现、交付目标回灌、验证、钢人反论审查和最终交付。它不承诺“零风险”，而是要求每次完成都必须有验证证据、工作区/分支/worktree 的集成状态、清理状态、剩余风险和下一步。

该 skill 的当前口径是：复杂或生产级任务默认需要可见的委派决策、独立专家视角或其他能改变结论的独立挑战面，不能因为“我自己写更快”就把交付降级成单 Agent 自写自验。只有任务确属小范围、低风险、可逆且验证明确，或真实子 Agent 不可用/不适合时，才允许单 Agent 处理，并必须在计划和钢人反论中说明原因；若缺少独立视角无法由测试、构建、浏览器验收、安全/数据库检查等客观证据补偿，最终声明必须降级为 partial、candidate 或 self-reviewed。

该 skill 现在把“人的 validation 是否友好”作为生产级交付的一部分：中等及复杂任务最终回复必须包含 Human Validation Packet，把最终交付成果、可用功能、架构审查面、核心逻辑、证据地图、钢人反论、残余风险和人工验收点翻译成用户可快速判断的形式。复杂/生产级、发布候选、合并主线、数据库/权限/安全/worker/外部副作用/浏览器验收，或用户明确要求报告时，默认在目标项目生成 HTML 交付报告：

```text
.production-delivery-reports/
  YYYY-MM-DD_<short-slug>/
    index.html
    evidence/
    manifest.json
```

报告是结果验收面，不是开发过程流水。实施过程中只维护简短 evidence notes（检查/结果/证明什么/限制），不要在每次失败、修复、重跑后反复编辑 HTML。最终在交付目标回灌、验证和钢人反论之后，用 `skills/production-delivery-manager/scripts/create_report.py` 一次性生成或补齐结果优先的 `Production Delivery Outcome` 报告。CI workflow、release-candidate workflow、本地测试、浏览器截图、日志摘录和子 Agent 审查都可以进入报告证据区，但必须标注证据等级和限制；截图只能证明可见 UI 状态，不能单独证明权限、数据隔离、幂等、事务或后端正确性。CI/workflow 是可重复机器验证的证据来源，HTML 报告负责汇总、解释和映射最终证据，不替代 CI，也不记录已被最终实现取代的中间尝试。

该 skill 还要求文档归属先行：正式项目文档只写长期事实，例如架构边界、接口契约、产品行为、操作规则和已接受决策；最终交付摘要只写关键成果、关键改动、最终验证、剩余风险和下一步；临时 evidence notes、调试流水、失败重试记录、raw logs 和子 Agent 过程记录不得写进原有产品/架构/开发/治理文档。需要持久验收证据时放入 `.production-delivery-reports/` 或项目明确批准的 audit/evidence artifact，并保持 outcome-first。

### `maintainability-guard`

用于在前端、后端、worker、脚本、测试辅助等代码继续堆功能前做可维护性守门。它不按行数洁癖强拆，也不把 800 行当作唯一触发点；每次改代码都先做轻量边界检查，再按职责分离、关注点分离、高内聚低耦合、单一抽象层级、变化轴、复用/重复压力、测试边界、依赖方向和稳定接口判断是否允许继续原地开发、需要小步拆分，或必须先做结构恢复。

#### 推荐项目规则

安装 `maintainability-guard` 后，建议在目标项目的 `AGENTS.md`、`.cursorrules` 或等效规则文件中加入短规则，让 Agent 在长期开发中稳定触发，而不是等代码已经堆大后再人工提醒：

```md
- 修改任何代码前先做轻量边界检查：本次新增/改变的职责是什么，是否属于规则、adapter、mapper、权限、状态流转、格式化、hook、工作流步骤、展示转换或可复用交互，是否已有或即将出现第二调用方/第二用例，是否存在重复，是否让测试更难。
- 当任务继续修改 800 行以上源文件、已有职责混杂文件、预计高复用模块、出现重复逻辑、存在第二调用方/第二用例、测试边界不清、依赖方向不明，或用户明确提出可维护性、可扩展性、架构边界、复用、避免堆代码问题时，必须先使用 `maintainability-guard` 并输出 Maintainability Gate。
- `maintainability-guard` 的判断应保持方法论通用：行数只作为报警器，真正拆分依据是职责分离、关注点分离、高内聚低耦合、单一抽象层级、变化轴、复用/重复压力、测试边界、依赖方向和稳定接口。
```

使用口径：

- 不为了小文件洁癖拆分；行数只是触发 Maintainability Gate 的报警器之一，不是免检通行证。
- 继续原地开发、先做小步拆分、还是先做结构恢复，应由职责、变化轴、复用、测试边界和依赖方向共同决定。
- 小文件中新增 mapper、validator、permission、status transition、formatter、hook、adapter、workflow step、presentation transform 或可复用交互时，也要判断是否需要先抽边界。
- 示例可以使用具体框架术语，但通用判断条件不要绑定具体框架、目录名或分层命名。
- 对高复用组件、服务、工具函数、worker、测试基座和跨项目能力，应比普通一次性代码更早触发该 skill。

### `admin-ui-pattern-system`

用于设计、实现、重构或审查后台管理界面、中后台、admin panel、CRUD 列表、配置控制台、审批/流程页、图谱/画布工作台、审计观测页和非 CRUD 运营工具等场景。它不绑定 Vben、Ant Design、Element Plus、MUI、React Admin 或任何框架，而是要求先盘点当前模板/框架的组件与完整页面示例，确认业务内容区线稿和基础页面元素，再归纳或复用项目级后台页面范式，确认后再编码。

核心口径：

- 后台页面不能从 API 字段、数据库表或组件清单直接堆出来。
- 编码前必须完成业务任务建模、当前模板能力盘点、内容区线稿、基础元素确认、项目范式建议、字段/搜索/操作/状态治理。
- 公共管理平台外壳通常不用反复澄清；重点确认右侧业务内容区怎么组织。
- 常规列表/CRUD 默认采用“可折叠适用备注/说明 + Tabs（如需要）+ 筛选区 + 操作工具栏 + 主列表 + 分页”的骨架。
- 基础元素必须优先复用框架/项目示例，包括检索区、检索折叠、属性筛选、快速搜索、隐藏筛选、刷新、全屏、列设置、字段显示/隐藏、密度、固定列、分页、批量操作等。
- 一页只显示一个主体信息；次级信息通过下钻新页面、抽屉、弹窗或专门流程承载。
- 详情、编辑和次级信息默认优先使用抽屉承载；短确认、极轻量输入和临时选择器才使用弹窗；信息过多、流程复杂或需要多 Tab/深链时使用独立页面。
- 字段超过 6 个必须做 P0/P1/P2/P3 分级；搜索条件超过 4 个必须支持折叠；行操作超过 3 个必须收纳。
- 图谱/画布类页面必须画布优先，说明、图例、添加节点/关系表单、属性编辑和新增关系流程不得长期挤压主画布。
- 非 CRUD 后台页面必须先选主范式，例如总览工作台、分步向导、导入映射、规则构建器、运行监控、Diff/发布确认、权限矩阵、对象 360、异常复核台、消息运营、搜索选择器、时间线、日历排期、报表分析或模板编辑；不得退化为“一个表格 + 一堆按钮 + 一堆卡片”。
- 缺少模板证据、线稿确认、状态覆盖或浏览器验收时，只能交付候选方案、局部修复或自审结果，不能声称后台产品级完成。
- 布局选择必须先回答主任务：找对象、按层级定位、配置发布、分步导入、异常复核、运行监控、关系编辑、风险总览、状态解释或对象 360；多个任务同时存在时只能选一个主体，其余下钻、抽屉、Tabs 或步骤承载。
- 必须输出布局决策记录：主任务判定、决策路径、被排除的相邻范式及原因、次级任务承载位置、证据来源。

#### 推荐项目规则

安装 `admin-ui-pattern-system` 后，建议在目标项目的 `AGENTS.md`、`.cursorrules` 或等效规则文件中加入短规则：

```md
- 设计、开发、重构或审查后台管理界面、中后台、admin panel、CRUD、配置治理、审批/流程、图谱/画布、审计观测和非 CRUD 运营工具页面时，必须先使用 `admin-ui-pattern-system`。
- 后台页面不得直接按接口字段或数据库字段堆叠；编码前必须先盘点当前模板/框架已有组件和完整页面示例，画出业务内容区线稿，归纳或复用项目级页面范式，并说明主页面、抽屉、独立页面、弹窗分别承载什么。
- 常规列表/CRUD 默认使用“可折叠说明/备注、Tabs（如需要）、筛选、操作工具栏、列表、分页”的基础骨架；检索折叠、属性筛选、快速搜索、刷新、全屏、列设置、字段隐藏/显示等基础元素应优先复用框架或项目示例。
- 一页只呈现一个主体信息；其他信息通过下钻新页面、按钮打开抽屉/弹窗或专门流程承载，不得在一个页面长期堆叠主列表、详情、表单、说明、图例和审计。
- 详情、编辑和次级信息默认优先使用抽屉；短确认/极轻量输入才使用弹窗；信息过多、流程复杂、多 Tab、长时间停留或需要深链时使用独立页面。
- 字段多、搜索多、操作多时必须做分级、折叠、列设置、更多菜单和状态验收，不允许为了一屏展示牺牲可用性。
- 非 CRUD 页面必须先确认主范式和主任务，复杂流程使用步骤、工作台、矩阵、Diff、时间线、监控或详情 360 等合适布局，不得强行套普通 CRUD 表格。
- 完成前必须说明模板/示例来源、内容区线稿、关键状态、实际桌面/窄屏验收结果和已知取舍；未执行项必须写“未验收”，证据不足时只能标为候选或局部修复。
- 输出必须标注证据等级：`full`、`candidate`、`local-fix` 或 `self-reviewed`，避免把未确认线稿或未验收实现说成完成。
```

### `documentation-governance`

用于创建、修改、重组、审计或决定不写软件工程项目文档时的文档治理门禁。它先判断内容到底属于 OpenSpec/变更规格、ADR、正式 source-of-truth docs、README/index、源码旁文档、交付报告证据、项目明确批准的 audit/evidence artifact、归档，还是根本不应该持久化。

核心口径：
- 正式文档只承载长期有效事实：当前产品行为、架构边界、接口契约、操作规则、工程约定和已接受决策。
- OpenSpec 或等价 change spec 承载拟议/进行中的跨模块变更、验收标准、影响面、迁移和评审链；实现完成后要把当前事实回写到正式文档。
- ADR 承载已接受的重要决策、备选方案、取舍、后果和 supersession 链，不承载实施计划、调试过程或普通小偏好。
- 交付报告和项目明确批准的 audit/evidence artifact 只承载最终成果、关键改动、验证、风险和下一步；临时过程记录、raw logs、失败重试和子 Agent transcript 不得污染正式 docs。
- 每个长期事实只有一个 canonical home；索引可以短摘要和链接，不能复制完整规则。
- 单文件持续膨胀时按生命周期、受众、领域、owner、source-of-truth 责任拆分，不按 agent 会话或日期机械拆分。
- 归档、弃用、superseded 和删除都必须显式标状态、替代入口、owner 和触发条件；不能让两个文档同时看起来都是 current。
- 治理要同时优化搜索便捷性和修改复杂度：文档路径、文件名、标题、索引别名要能被搜到；同一个长期事实变化时应只有一个 canonical 编辑位置。

推荐项目规则：

```md
- 创建、修改、重组或审计项目文档前，先使用 `documentation-governance` 做文档路由判断。
- 任何文档写入前先判断内容是拟议变更、已接受决策、当前事实、接口契约、操作规程、最终验收证据、项目明确批准的 audit/evidence artifact、原始参考、历史归档还是临时过程信息。
- 正式 source-of-truth docs 只写长期事实；过程记录、调试流水、raw logs、失败重试、子 Agent transcript 和 scratch reasoning 不得写入正式产品/架构/开发/治理文档。
- OpenSpec/change spec 用于拟议或进行中的跨模块变更和验收；ADR 用于已接受且有重要取舍的决策；正式 docs 用于当前稳定事实；README/docs index 只做入口和链接。
- 新增长期文档必须更新最近的索引；废弃内容必须标注 superseded/archived 并给出反向链接。
- 单文件膨胀时优先按生命周期、受众、领域、owner 和 source-of-truth 责任拆分，避免把当前事实、计划、决策和临时过程记录混在一起。
- 文档结构调整必须说明搜索入口和修改成本：读者怎样找到 canonical answer；下一次同一事实变化时需要改几个文件。
```

## Repository Layout

```text
skills-lab/
  skills/
    design-to-frontend-delivery/
      SKILL.md
      agents/openai.yaml
      references/
    production-delivery-manager/
      SKILL.md
      agents/openai.yaml
      scripts/
      references/
    reuse-first-guard/
      SKILL.md
      agents/openai.yaml
      references/
    maintainability-guard/
      SKILL.md
      agents/openai.yaml
    admin-ui-pattern-system/
      SKILL.md
      agents/openai.yaml
      references/
    documentation-governance/
      SKILL.md
      agents/openai.yaml
      references/
```

## Local Validation

在仓库根目录执行（将 `<your-codex-home>` 替换为你本机实际路径）：

```powershell
$env:PYTHONUTF8='1'
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/design-to-frontend-delivery"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/reuse-first-guard"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/production-delivery-manager"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/maintainability-guard"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/admin-ui-pattern-system"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/documentation-governance"
```

Windows 下中文 skill 需要启用 UTF-8 模式，否则 Python 可能按 GBK 读取 `SKILL.md` 并报 `UnicodeDecodeError`。

### Manual Smoke Checks

- `设计稿 + 导出 HTML -> React`：应进入 `convert-and-polish`。
- `Figma/其他设计平台链接 + 已安装插件或 MCP`：应先读取平台可提供的结构、样式、tokens、组件映射或 reference code；能拿到结构化源时不得下载图当主基线。
- `请 1:1 还原这个设计稿`：应理解为高保真视觉目标，优先用 Flex/Grid/flow、tokens 和响应式约束实现间距、对齐、字体、颜色和状态，不得用大量 absolute/left/top 坐标复刻普通页面布局。
- `按设计稿做一个 React/Vue 页面`：应先识别当前工程路由、feature、components、fixtures、styles/assets 和测试约定；页面入口、组件、mock 数据、展示选择器、样式和测试按职责归位，不得全部堆进一个页面文件或随机新建的 mock/components 文件夹。
- `静态 mock 列表页/详情页，未来由 BFF 返回数据`：应把 mock 数据集中为展示夹具或 BFF-shaped fixture，只保留当前 tab、选中项、弹框等轻量 UI 状态、薄展示选择器和演示级基础校验；不得在前端推导派生业务指标、生命周期/状态流转、授权/资格、可执行动作裁定、集成状态归一化或 API 状态机。
- `已有 React 工程，只说补交互但实际缺校验`：应进入 `polish-existing-project`，并触发范围缺口检测，给出最小闭环扩围建议（如补校验与反馈态）。
- `只有截图，没有 HTML`：应先做仅视觉降级确认，确认后再问目标端，默认推荐 React。
- `我要做一个用户鉴权模块`：应优先给出现成方案与不建议直接自研的原因。
- `我要给现有系统接入支付`：应优先推荐第三方支付方案，而不是自建支付流程。
- `我要做一个只属于我们业务的核心排程引擎`：应在给出业务壁垒、性能、TCO 等理由后，才允许有条件自研。
- `我要做一个自定义样式的上传控件`：应优先建议“UI 自绘 + 原生 file input / Headless 行为层 / 成熟上传库”，不应默认把去重、队列、重试、上限控制继续扩成自研上传状态机。
- `我要新增一个后台列表页`：应先找当前工程已有列表页、路由、查询表单、表格、弹窗和测试模式，优先复制适配最近的本地示例，而不是从空白页面新写。
- `帮我做一个生产级的后台权限模块` 或 `用 production-delivery-manager 交付这个功能`：应进入 `production-delivery-manager`，先锁定验收标准，再查项目已有权限模式和官方文档，拆分实现与审查任务，最后必须给出验证证据、钢人反论和剩余风险。
- `用 production-delivery-manager 做完整产品化交付，质量比速度重要`：应把任务按复杂/生产级处理，显式输出 Delegation Quality Gate；默认安排至少一个独立专家视角（如 Architect、Reviewer、Security、Database、E2E、Docs/Release），除非说明真实子 Agent 不可用或任务确属小范围低风险。
- `用 production-delivery-manager，但这个需求看起来很简单`：可以压缩流程，但必须说明为什么不派发子 Agent，并在最终钢人反论中挑战这个判断；不能只用“我自己更快”作为理由。
- `用 production-delivery-manager，但当前环境没有真实子 Agent`：必须明示 no-delegation reason，用 targeted tests、typecheck、build、浏览器/E2E、安全/数据库检查或人工审阅补偿；无法补偿时只能交付 partial/candidate/self-reviewed。
- `用 production-delivery-manager，并且最后给我可审的交付报告`：实施中只记录 evidence notes，不反复写 HTML；最终在交付目标中生成 `.production-delivery-reports/<日期>_<slug>/index.html`，首页先给出 Delivered Capabilities 和 Human Validation Packet，后续展开架构、核心逻辑、证据地图、CI/workflow、本地验证、浏览器截图/限制、钢人反论、workspace 集成和残余风险。
- `用 production-delivery-manager，但不要啰嗦过程，只要最终汇总`：最终输出应只包含关键成果、关键改动、最终验证、剩余风险和下一步；不得把临时过程记录、失败重试、子 Agent 流水或 raw logs 写进正式 docs。
- `做了浏览器测试并截了图`：截图应进入 HTML 报告的 Browser Evidence 或 Evidence Map，并标为 `screenshot` 证据；同时写明它证明的是可见状态，不替代后端/API/权限/数据隔离测试。
- `CI release-candidate workflow 已经跑过`：应把 workflow 名称、提交/分支、结果、artifact 或链接写进 Evidence Map，并说明它证明的是可重复机器门禁，不等于用户已验收或生产已发布。
- `用 production-delivery-manager 改一个单文件文案错字`：可直接做并简短报告验证和风险，不需要完整多 Agent 矩阵。
- `用 production-delivery-manager 让多个 agent 并行改后端和后台前端`：应先检查 `git status --short`，说明使用当前工作区、分支或 git worktree 的理由；并行写代码时应分配不重叠范围，必要时使用独立 worktree，交付前必须说明变更是否已回灌到用户原始工作区/目标分支并在那里验证。
- `我在主分支上提出需求，agent 用 worktree 改完了`：不应直接声称完成；除非用户接受 branch/PR-only 交付，否则必须 merge/cherry-pick/apply 回主工作区或目标分支，无法回灌时只能报告候选实现和阻塞原因。
- `主分支上有人正在手工改文档，我还要你继续改另一个文档`：不应因为存在本地改动就硬性停止；应判断改动是否重叠、是否可逆、最终验收是否就在当前工作区，只有重叠或意图不明时才询问、隔离或暂缓。
- `继续往这个 1500 行页面/服务里加一个功能`：应先进入 `maintainability-guard`，输出 Maintainability Gate，按职责、变化轴、测试边界和依赖方向判断是否允许继续原地开发。
- `这个文件不到 400 行，但我要把同一个状态映射给另一个页面也用`：应先进入 `maintainability-guard`，不能用小文件当免检理由；需要判断是否已有第二用例、是否会复制逻辑、是否该形成稳定输入输出契约。
- `这个组件以后多个页面都要用`：应先进入 `maintainability-guard`，确认是否已有稳定输入输出、是否真的出现第二个使用场景、是否会变成万能组件，再决定抽取边界。
- `我要新增一个后台管理页面`：应先进入 `admin-ui-pattern-system`，盘点当前模板已有列表、搜索、表格工具栏、抽屉、弹窗、详情页和完整示例，再提出项目页面范式，不应直接按接口字段堆组件。
- `这个后台页面字段很多、操作很多`：应进入 `admin-ui-pattern-system`，输出字段分级、搜索折叠、列设置、操作收纳和状态验收方案。
- `图谱编辑器右侧说明、图例和添加节点表单一直堆着`：应进入 `admin-ui-pattern-system`，先画内容区线稿，按画布工作台范式重设布局，画布优先，说明/图例折叠或弹出，属性与新增关系默认用 inspector/抽屉/独立流程承载。
- `我要做规则配置向导/数据导入映射/权限矩阵/运行监控/异常复核台`：应进入 `admin-ui-pattern-system` 的非 CRUD 范式，先确认主任务、步骤/矩阵/工作台/时间线/Diff 等布局，再进入实现。
- `后台页面已经做完了但没有浏览器验收或线稿确认`：应降级为候选方案或局部修复，不能声称产品级完成。

- `这个项目文档越来越乱，哪些要写 OpenSpec、哪些写 ADR、哪些写正式文档`：应进入 `documentation-governance`，先输出 Documentation Governance Gate，按拟议变更、已接受决策、当前事实、索引、证据 artifact、归档或不持久化来路由。
- `这次实现过程我跑了很多命令和失败重试，要不要写进 docs`：默认不写进正式 docs；只在最终报告或项目明确批准的 audit/evidence artifact 中保留结果化证据，正式 docs 只更新长期事实和当前边界。
- `一个开发规划文档一直被追加，已经很长`：应按生命周期、受众、领域、owner 和 source-of-truth 责任审查是否拆分、弃用、归档或改成索引，不能继续把当前事实、计划、ADR 和临时过程记录堆在同一文件。
## Publish This Repository

```bash
git remote add origin git@github.com:mahui-wangjin/skills-lab.git
git branch -M main
git add .
git commit -m "feat: add reuse-first-guard skill"
git push -u origin main
```
