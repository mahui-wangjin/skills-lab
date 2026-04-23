# skills-lab

个人 skills 仓库，当前包含“前端设计落地与精修”和“通用工程决策守门”两类 skill。

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

全局安装并跳过确认：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-frontend-delivery -g -y
```

```bash
npx skills add mahui-wangjin/skills-lab --skill reuse-first-guard -g -y
```

安装完成后重启 Codex，让新 skill 生效。

## Available Skills

### `design-to-frontend-delivery`

覆盖从设计输入解析、基线选择、工程转换到还原验收与精修交付的完整前端设计落地流程。

`design-to-code-html-first` 已并入 `design-to-frontend-delivery` 的 reference 层，不再作为独立 skill 维护。
旧名已不再可安装，请改用 `design-to-frontend-delivery`。

### `reuse-first-guard`

在关键开发决策前执行“先复用、再采购/集成/生成、最后才自研”的守门流程。适用于新增依赖、第三方服务、基础设施能力、新自研模块、重大重构，以及鉴权、支付、搜索、存储、消息、表单、上传、CMS、监控、工作流等高复用场景。

该 skill 现在额外强调一条稳定性规则：
当用户要“自定义 UI”时，默认只允许自定义视觉层；行为层优先复用原生浏览器能力、框架官方能力、Headless/unstyled primitives 或成熟领域库，不要顺手把通用状态机也写成自研实现。

## Repository Layout

```text
skills-lab/
  skills/
    design-to-frontend-delivery/
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
```

### Manual Smoke Checks

- `设计稿 + 导出 HTML -> React`：应进入 `convert-and-polish`。
- `已有 React 工程，只说补交互但实际缺校验`：应进入 `polish-existing-project`，并触发范围缺口检测，给出最小闭环扩围建议（如补校验与反馈态）。
- `只有截图，没有 HTML`：应先做仅视觉降级确认，确认后再问目标端，默认推荐 React。
- `我要做一个用户鉴权模块`：应优先给出现成方案与不建议直接自研的原因。
- `我要给现有系统接入支付`：应优先推荐第三方支付方案，而不是自建支付流程。
- `我要做一个只属于我们业务的核心排程引擎`：应在给出业务壁垒、性能、TCO 等理由后，才允许有条件自研。
- `我要做一个自定义样式的上传控件`：应优先建议“UI 自绘 + 原生 file input / Headless 行为层 / 成熟上传库”，不应默认把去重、队列、重试、上限控制继续扩成自研上传状态机。

## Publish This Repository

```bash
git remote add origin git@github.com:mahui-wangjin/skills-lab.git
git branch -M main
git add .
git commit -m "feat: add reuse-first-guard skill"
git push -u origin main
```
