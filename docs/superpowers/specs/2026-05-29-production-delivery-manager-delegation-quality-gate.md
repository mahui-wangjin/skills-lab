# production-delivery-manager 委派质量门禁增强

## 背景

`production-delivery-manager` 已经要求需求、检索、工作区隔离、交付目标回灌、验证和钢人反论，但实际使用中仍可能出现一个问题：用户要求严格生产级交付时，Agent 仍把任务判断为“我自己能做”，然后单 Agent 自写、自验、自行宣布完成。

这会弱化 Manager Agent 的核心价值：任务拆解、专家分工、独立审查、验证证据和最终质量判断。

## 目标

- 对复杂、生产级、严格交付、质量优先任务，默认进入完整门禁。
- 明确 `Delegation Quality Gate`，要求在实现前说明是否使用真实子 Agent、角色分工、文件范围和审查重点。
- 复杂或生产级任务默认至少需要一个独立质量面，例如架构、风险、测试、E2E、数据库、安全、文档或发布审查。
- 保留简单任务直做的例外，避免流程表演。
- 如果不使用真实子 Agent，必须在计划中说明原因，并在钢人反论中挑战该决定。
- 如果缺少真实子 Agent 或独立审查，需要用更强的客观验证补偿；无法补偿时，最终声明降级为 partial、candidate 或 self-reviewed。

## 非目标

- 不强制所有任务都派发多个 Agent。
- 不把委派本身当作完成质量的证明。
- 不允许多个 Agent 编辑同一文件范围导致冲突。
- 不替代项目自己的代码审查、CI、发布或人工验收规则。

## 规则变更

- `SKILL.md` 增加质量优先口径：不能因为速度把生产级任务降级为单 Agent 交付。
- `SKILL.md` 新增 `Delegation Quality Gate`，要求复杂/生产级任务在实现前说明角色、真实子 Agent、文件范围、审查风险和不委派理由。
- `SKILL.md` 的完成标准要求复杂/生产级交付报告 delegation decision、独立挑战面、不委派理由或自审降级声明。
- `delivery-gates.md` 新增 `Gate 3.5: Delegation Quality Gate`，定义好的/坏的不委派理由。
- `delegation-patterns.md` 增加最小质量面：架构面、风险面、验证面、文档/发布面。
- `steelman-review.md` 增加过程反审：复杂/生产级任务必须挑战“是否由同一 Agent 实现、审查、验证和接受”。
- README smoke check 增加质量优先和简单任务例外场景。

## 验收

- `quick_validate.py ./skills/production-delivery-manager` 通过。
- `git diff --check` 通过。
- 钢人反论应能明确挑战“多 Agent 没用或没派发”的理由，而不是只审查产物内容。
- README 中的生产级交付说明能让使用者知道：复杂任务默认要有独立专家视角，简单任务可以压缩但要说明理由。
