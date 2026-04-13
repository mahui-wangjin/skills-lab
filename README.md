# skills-lab

个人 skills 仓库，当前定位为“前端设计落地与精修” skill 仓库。

## Installation & Discovery

列出这个仓库里的可安装 skills：

```bash
npx skills add mahui-wangjin/skills-lab --list
```

安装指定 skill：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-frontend-delivery
```

全局安装并跳过确认：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-frontend-delivery -g -y
```

安装完成后重启 Codex，让新 skill 生效。

## Available Skills

### `design-to-frontend-delivery`

覆盖从设计输入解析、基线选择、工程转换到还原验收与精修交付的完整前端设计落地流程。

`design-to-code-html-first` 已并入 `design-to-frontend-delivery` 的 reference 层，不再作为独立 skill 维护。
旧名已不再可安装，请改用 `design-to-frontend-delivery`。

## Repository Layout

```text
skills-lab/
  skills/
    design-to-frontend-delivery/
      SKILL.md
      agents/openai.yaml
      references/
```

## Local Validation

在仓库根目录执行（将 `<your-codex-home>` 替换为你本机实际路径）：

```bash
python "<your-codex-home>/skills/.system/skill-creator/scripts/quick_validate.py" "./skills/design-to-frontend-delivery"
```

### Manual Smoke Checks

- `设计稿 + 导出 HTML -> React`：应进入 `convert-and-polish`。
- `已有 React 工程，只说补交互但实际缺校验`：应进入 `polish-existing-project`，并触发范围缺口检测，给出最小闭环扩围建议（如补校验与反馈态）。
- `只有截图，没有 HTML`：应先做仅视觉降级确认，确认后再问目标端，默认推荐 React。

## Publish This Repository

```bash
git remote add origin git@github.com:mahui-wangjin/skills-lab.git
git branch -M main
git add .
git commit -m "feat: update design-to-frontend-delivery skill docs"
git push -u origin main
```
