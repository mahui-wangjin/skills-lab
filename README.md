# skills-lab

个人 skills 仓库，当前包含“前端设计落地与精修”、“通用工程决策守门”、“生产级工程交付总控”、“通用可维护性守门”和“后台管理界面范式系统”五类 skill。

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

安装完成后重启 Codex，让新 skill 生效。

## Available Skills

### `design-to-frontend-delivery`

覆盖从设计输入解析、基线选择、工程转换到还原验收与精修交付的完整前端设计落地流程。

`design-to-code-html-first` 已并入 `design-to-frontend-delivery` 的 reference 层，不再作为独立 skill 维护。
旧名已不再可安装，请改用 `design-to-frontend-delivery`。

### `reuse-first-guard`

在关键开发决策前执行“先复用、再采购/集成/生成、最后才自研”的守门流程。适用于新增依赖、第三方服务、基础设施能力、新自研模块、新页面/组件/服务、重大重构，以及鉴权、支付、搜索、存储、消息、表单、上传、CMS、监控、工作流等高复用场景。

该 skill 现在把“当前工程已有实现”放在第一复用位：先找项目内现成模块、页面、组件、适配器、测试、模板、starter 或 demo，能直接复用或复制适配就不新写。只有用户明确要求新写，或项目内模式、官方能力、成熟复用路径都不匹配时，才继续讨论自研。

该 skill 现在额外强调一条稳定性规则：
当用户要“自定义 UI”时，默认只允许自定义视觉层；行为层优先复用原生浏览器能力、框架官方能力、Headless/unstyled primitives 或成熟领域库，不要顺手把通用状态机也写成自研实现。

### `production-delivery-manager`

用于用户明确点名或明确要求“生产级 / 完整生产级 / release-ready / 高确定性交付 / Leader 带团队交付”时的工程交付总控：先澄清需求和验收标准，再做项目检索、复用优先、工作区隔离判断、任务拆分、子 Agent 分工、实现、交付目标回灌、验证、钢人反论审查和最终交付。它不承诺“零风险”，而是要求每次完成都必须有验证证据、工作区/分支/worktree 的集成状态、清理状态、剩余风险和下一步。

### `maintainability-guard`

用于在前端、后端、worker、脚本、测试辅助等代码继续堆功能前做可维护性守门。它不按行数洁癖强拆，而是把行数作为报警器，再按职责分离、关注点分离、高内聚低耦合、单一抽象层级、变化轴、测试边界、依赖方向和稳定接口判断是否允许继续原地开发、需要小步拆分，或必须先做结构恢复。

#### 推荐项目规则

安装 `maintainability-guard` 后，建议在目标项目的 `AGENTS.md`、`.cursorrules` 或等效规则文件中加入短规则，让 Agent 在长期开发中稳定触发，而不是等代码已经堆大后再人工提醒：

```md
- 当任务继续修改 800 行以上源文件、已有职责混杂文件、预计高复用模块，或用户明确提出可维护性、可扩展性、架构边界、避免堆代码问题时，必须先使用 `maintainability-guard`。
- `maintainability-guard` 的判断应保持方法论通用：行数只作为报警器，真正拆分依据是职责分离、关注点分离、高内聚低耦合、单一抽象层级、变化轴、测试边界、依赖方向和稳定接口。
```

使用口径：

- 不为了小文件洁癖拆分；行数只是触发 Maintainability Gate 的报警器。
- 继续原地开发、先做小步拆分、还是先做结构恢复，应由职责、变化轴、复用、测试边界和依赖方向共同决定。
- 示例可以使用具体框架术语，但通用判断条件不要绑定具体框架、目录名或分层命名。
- 对高复用组件、服务、工具函数、worker、测试基座和跨项目能力，应比普通一次性代码更早触发该 skill。

### `admin-ui-pattern-system`

用于设计、实现或审查后台管理界面、中后台、admin panel、CRUD 列表、配置控制台、审批/流程页、图谱/画布工作台、审计观测页等场景。它不绑定 Vben、Ant Design、Element Plus、MUI、React Admin 或任何框架，而是要求先盘点当前模板/框架的组件与完整页面示例，再归纳或复用项目级后台页面范式，确认后再编码。

核心口径：

- 后台页面不能从 API 字段、数据库表或组件清单直接堆出来。
- 编码前必须完成业务任务建模、当前模板能力盘点、项目范式建议、字段/搜索/操作/状态治理。
- 详情、编辑和次级信息默认优先使用抽屉承载；短确认、极轻量输入和临时选择器才使用弹窗；信息过多、流程复杂或需要多 Tab/深链时使用独立页面。
- 字段超过 6 个必须做 P0/P1/P2/P3 分级；搜索条件超过 4 个必须支持折叠；行操作超过 3 个必须收纳。
- 图谱/画布类页面必须画布优先，图例、表单、属性编辑和新增关系流程不得长期挤压主画布。

#### 推荐项目规则

安装 `admin-ui-pattern-system` 后，建议在目标项目的 `AGENTS.md`、`.cursorrules` 或等效规则文件中加入短规则：

```md
- 开发或审查后台管理界面、中后台、admin panel、CRUD、配置治理、审批/流程、图谱/画布、审计观测页面时，必须先使用 `admin-ui-pattern-system`。
- 后台页面不得直接按接口字段或数据库字段堆叠；编码前必须先盘点当前模板/框架已有组件和完整页面示例，归纳或复用项目级页面范式，并说明主页面、抽屉、独立页面、弹窗分别承载什么。
- 详情、编辑和次级信息默认优先使用抽屉；短确认/极轻量输入才使用弹窗；信息过多、流程复杂、多 Tab、长时间停留或需要深链时使用独立页面。
- 字段多、搜索多、操作多时必须做分级、折叠、列设置、更多菜单和状态验收，不允许为了一屏展示牺牲可用性。
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
```

## Local Validation

在仓库根目录执行（将 `<your-codex-home>` 替换为你本机实际路径）：

```bash
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/design-to-frontend-delivery"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/reuse-first-guard"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/production-delivery-manager"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/maintainability-guard"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/admin-ui-pattern-system"
```

### Manual Smoke Checks

- `设计稿 + 导出 HTML -> React`：应进入 `convert-and-polish`。
- `已有 React 工程，只说补交互但实际缺校验`：应进入 `polish-existing-project`，并触发范围缺口检测，给出最小闭环扩围建议（如补校验与反馈态）。
- `只有截图，没有 HTML`：应先做仅视觉降级确认，确认后再问目标端，默认推荐 React。
- `我要做一个用户鉴权模块`：应优先给出现成方案与不建议直接自研的原因。
- `我要给现有系统接入支付`：应优先推荐第三方支付方案，而不是自建支付流程。
- `我要做一个只属于我们业务的核心排程引擎`：应在给出业务壁垒、性能、TCO 等理由后，才允许有条件自研。
- `我要做一个自定义样式的上传控件`：应优先建议“UI 自绘 + 原生 file input / Headless 行为层 / 成熟上传库”，不应默认把去重、队列、重试、上限控制继续扩成自研上传状态机。
- `我要新增一个后台列表页`：应先找当前工程已有列表页、路由、查询表单、表格、弹窗和测试模式，优先复制适配最近的本地示例，而不是从空白页面新写。
- `帮我做一个生产级的后台权限模块` 或 `用 production-delivery-manager 交付这个功能`：应进入 `production-delivery-manager`，先锁定验收标准，再查项目已有权限模式和官方文档，拆分实现与审查任务，最后必须给出验证证据、钢人反论和剩余风险。
- `用 production-delivery-manager 让多个 agent 并行改后端和后台前端`：应先检查 `git status --short`，说明使用当前工作区、分支或 git worktree 的理由；并行写代码时应分配不重叠范围，必要时使用独立 worktree，交付前必须说明变更是否已回灌到用户原始工作区/目标分支并在那里验证。
- `我在主分支上提出需求，agent 用 worktree 改完了`：不应直接声称完成；除非用户接受 branch/PR-only 交付，否则必须 merge/cherry-pick/apply 回主工作区或目标分支，无法回灌时只能报告候选实现和阻塞原因。
- `主分支上有人正在手工改文档，我还要你继续改另一个文档`：不应因为存在本地改动就硬性停止；应判断改动是否重叠、是否可逆、最终验收是否就在当前工作区，只有重叠或意图不明时才询问、隔离或暂缓。
- `继续往这个 1500 行页面/服务里加一个功能`：应先进入 `maintainability-guard`，输出 Maintainability Gate，按职责、变化轴、测试边界和依赖方向判断是否允许继续原地开发。
- `这个组件以后多个页面都要用`：应先进入 `maintainability-guard`，确认是否已有稳定输入输出、是否真的出现第二个使用场景、是否会变成万能组件，再决定抽取边界。
- `我要新增一个后台管理页面`：应先进入 `admin-ui-pattern-system`，盘点当前模板已有列表、搜索、表格工具栏、抽屉、弹窗、详情页和完整示例，再提出项目页面范式，不应直接按接口字段堆组件。
- `这个后台页面字段很多、操作很多`：应进入 `admin-ui-pattern-system`，输出字段分级、搜索折叠、列设置、操作收纳和状态验收方案。
- `图谱编辑器右侧表单太挤`：应进入 `admin-ui-pattern-system`，按画布工作台范式重设布局，画布优先，属性与新增关系默认用 inspector/抽屉/独立流程承载。

## Publish This Repository

```bash
git remote add origin git@github.com:mahui-wangjin/skills-lab.git
git branch -M main
git add .
git commit -m "feat: add reuse-first-guard skill"
git push -u origin main
```
