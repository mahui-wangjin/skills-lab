# reuse-first-guard Project-Local Reuse Refinement

## Context

`reuse-first-guard` 已经能阻止默认自研通用能力，并且在自定义 UI 场景下强调“视觉层可以自绘，行为层优先复用”。但真实工程中还有一个更高频的问题：

即使不引入新外部库，Agent 也可能在当前代码工程已有相似页面、模块、适配器、测试或 demo 的情况下，从空白文件开始重写。

这会导致：

- 页面和组件偏离现有设计系统。
- API、权限、审计、错误处理、测试风格不一致。
- 同一个技术形态在仓库里出现多套平行实现。
- 后续维护者难以判断哪个实现是基准。

## Decision

将“当前代码工程已有实现”提升为 `reuse-first-guard` 的第一复用层。

新的优先级：

1. 当前工程已有模块、页面、组件、适配器、helper、测试、fixture、模板、starter 或 demo。
2. 已选框架、平台、SDK 或产品的官方能力。
3. SaaS 或托管服务。
4. 成熟开源库、模板或 starter。
5. 代码生成或 AI 生成。
6. 自研。

## Rules

使用该 skill 时，初始 gate 仍必须先输出固定模板，不能先读仓库。若还未做仓库检查，可以在模板中将 project-local reuse 标为 `pending`。

Gate 输出后、规划或实现前，必须检查当前工程是否已有相同技术形态：

- 后端：module、service、controller、DTO、adapter、guard、middleware、job、worker、测试。
- 前端：page、route、menu、form、table、drawer、modal、tabs、filter、空态/错误态/加载态、浏览器验收脚本。
- 治理能力：权限、审计、错误 envelope、幂等、观测、命名、目录结构、测试 fixture。
- 仓库内维护的框架 examples、playground、generated starter、内部模板、seed、mock。

如果存在匹配模式，默认顺序是：

1. 直接复用已有 API 或组件。
2. 复制并适配最近的本地示例。
3. 对既有模式增加薄扩展点。
4. 只为真实缺口新增代码。

## Custom Build Exception

只有以下情况才允许跳过项目内复用并继续自研：

- 用户明确要求新写或不复用。
- 已记录本地复用检查，确认没有合适模式。
- 业务差异是真正的核心竞争力。
- 合规、安全、性能、供应商锁定或长期 TCO 明确要求新实现。

## Expected Behavior

当用户说“新增一个后台列表页”“做一个新服务”“加一个 API client”“实现一个审批流”时，Agent 应该先想到：

> 当前工程里有没有相同页面结构、模块边界、权限审计、测试模式或示例可以照抄？

而不是直接进入新文件设计。

## Touched Files

- `skills/reuse-first-guard/SKILL.md`
- `skills/reuse-first-guard/references/evaluation-criteria.md`
- `skills/reuse-first-guard/agents/openai.yaml`
- `README.md`
- `AGENTS.md`
- `docs/README.md`
