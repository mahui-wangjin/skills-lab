# production-delivery-manager 工作区隔离规则增强

## 背景

`production-delivery-manager` 已覆盖需求澄清、检索、计划、实现、验证、钢人反论和交付，但首版没有把工作区隔离作为显式 gate。对于生产级交付、长周期任务和多 agent 并行写代码，缺少该 gate 容易导致用户本地改动被误碰、并行写入范围重叠、临时产物残留，或把隔离 worktree 当成最终验收工作区。

## 目标

- 在正式计划和实现前显式判断当前工作区是否可用。
- 要求在 Git 仓库中先检查 `git status --short`。
- 对大改动、高风险重构、长周期任务、多 agent 并行写代码或用户需要保留当前工作区的情况，优先使用独立分支或 git worktree。
- 对小型、可逆、低风险文档或单文件变更，允许说明理由后继续使用当前工作区，避免制造额外清理成本。
- 交付时报告工作区决策、清理状态和剩余未跟踪文件。

## 非目标

- 不强制所有任务都创建 worktree。
- 不替代具体项目自己的分支、提交、发布或验收规则。
- 不允许因为使用 worktree 而跳过最终目标工作区或真实验收环境确认。

## 规则变更

- `SKILL.md` 的交付循环新增 `Workspace isolation`。
- `Gate Rules` 新增 `Workspace Isolation`，要求检查 git 状态、识别无关用户改动、选择当前工作区/分支/worktree。
- `Delivery Plan` 必须包含 workspace decision。
- `Implementation` 必须关注临时文件、测试产物和本地输出清理。
- `Handoff` 必须包含 workspace and cleanup status。
- `delivery-gates.md` 新增 `Gate 2.5: Workspace Isolation`，并定义当前工作区、分支或 worktree 的适用条件。
- `delegation-patterns.md` 要求代码写入型子 agent 使用指定分支或 worktree，并清理自己产生的临时产物。

## 验收

- `quick_validate.py ./skills/production-delivery-manager` 通过。
- `git diff --check` 通过。
- README smoke check 能体现多 agent 并行场景下的 git status、worktree 和清理状态要求。
