# design-to-frontend-delivery 结构化源优先优化

## 背景

用户在设计转前端任务中提供 Figma 地址，并已安装 Figma 插件/MCP。Agent 仍可能跳过 Dev Mode 类属性、MCP design context、Code Connect 或 reference code，转而下载图片按视觉稿复刻。

这种降级会显著增加返工概率。设计平台能提供结构、样式、tokens、组件映射或参考代码时，截图只能用于视觉校验，不能作为主事实源。

## 目标

- 建立平台无关的“结构化源优先”规则。
- 不把问题限定为 Figma；未来 Stitch、Framer、Webflow、设计 token 系统、导出 HTML/CSS、组件映射和其他平台同样适用。
- 在 Gate 1 强制记录是否尝试读取结构化源，避免 Agent 未尝试就按图复刻。
- 只有结构化源不存在、不可访问或用户明确要求忽略时，才允许视觉降级。

## 新口径

强事实源包括但不限于：

- Dev Mode 类 inspect 数据。
- MCP design context。
- Code Connect 或组件映射。
- tokens、样式变量、图层结构、约束、variants。
- 设计工具生成的 React/Vue/HTML 片段。
- 导出 HTML/CSS/JS。
- 用户提供的参考代码或已接受实现。

截图、下载图、静态渲染图仅用于：

- 视觉验收。
- 差异检查。
- 位图资产提取。

不得用于替代可读的结构化源。

## 修改范围

- `skills/design-to-frontend-delivery/SKILL.md`
- `skills/design-to-frontend-delivery/references/source-priority.md`
- `skills/design-to-frontend-delivery/references/convert-and-polish.md`
- `skills/design-to-frontend-delivery/references/delivery-checklists.md`
- `README.md`

## 验收

- Design-platform URL / plugin / MCP 输入必须先执行 Structured Source Gate。
- Gate 1 输出包含结构化源检查记录。
- 仅视觉降级前必须说明结构化源不存在、不可访问或被用户明确排除。
- `convert-and-polish` 不再只称为 HTML-first，而是 structured-source-first。
- README smoke case 覆盖“平台链接 + 插件/MCP 不得下载图当主基线”。
