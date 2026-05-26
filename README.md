# skills-lab

个人 skills 仓库，当前包含“前端设计落地与精修”、“通用工程决策守门”和“生产级工程交付总控”三类 skill。

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

用于用户明确点名或明确要求“生产级 / 完整生产级 / release-ready / 高确定性交付 / Leader 带团队交付”时的工程交付总控：先澄清需求和验收标准，再做项目检索、复用优先、工作区隔离判断、任务拆分、子 Agent 分工、实现、验证、钢人反论审查和最终交付。它不承诺“零风险”，而是要求每次完成都必须有验证证据、工作区与清理状态、剩余风险和下一步。

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
```

## Local Validation

在仓库根目录执行（将 `<your-codex-home>` 替换为你本机实际路径）：

```bash
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/design-to-frontend-delivery"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/reuse-first-guard"
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/production-delivery-manager"
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
- `用 production-delivery-manager 让多个 agent 并行改后端和后台前端`：应先检查 `git status --short`，说明使用当前工作区、分支或 git worktree 的理由；并行写代码时应分配不重叠范围，必要时使用独立 worktree，交付时报告清理状态。

## Publish This Repository

```bash
git remote add origin git@github.com:mahui-wangjin/skills-lab.git
git branch -M main
git add .
git commit -m "feat: add reuse-first-guard skill"
git push -u origin main
```
