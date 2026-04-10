# skills-lab

个人 skills 仓库，当前用于沉淀“设计转代码”类规则型 skill。

## Installation & Discovery

列出这个仓库里的可安装 skills：

```bash
npx skills add mahui-wangjin/skills-lab --list
```

安装指定 skill：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-code-html-first
```

全局安装并跳过确认：

```bash
npx skills add mahui-wangjin/skills-lab --skill design-to-code-html-first -g -y
```

安装完成后重启 Codex，让新 skill 生效。

## Available Skills

### `design-to-code-html-first`

设计转代码时，优先复用最强实现基线，而不是直接按视觉稿重写。

- 第一优先级是导出 HTML、导出代码、设计工具生成代码
- 第二优先级是用户提供的参考代码和现有实现
- 视觉稿、截图、mockup 仅作为校验和兜底
- 如果只有视觉稿，必须先明确降级说明，并询问用户是继续视觉还原，还是继续提供导出 HTML、参考代码或现有实现

适用场景：

- Stitch、Figma、Framer、Webflow 等设计产物转 React、Vue、静态 HTML、小程序
- 设计图、导出 HTML、现有工程三者并存且可能互相冲突
- 用户强调“最大化保证设计和实现一致性”

## Repository Layout

```text
skills-lab/
  skills/
    design-to-code-html-first/
      SKILL.md
      agents/openai.yaml
      references/source-priority.md
```

## Local Validation

```bash
python "C:\Users\97227\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "E:\develop\code\my-project\skills-lab\skills\design-to-code-html-first"
```

## Publish This Repository

```bash
git remote add origin git@github.com:mahui-wangjin/skills-lab.git
git branch -M main
git add .
git commit -m "feat: add design-to-code-html-first skill"
git push -u origin main
```
