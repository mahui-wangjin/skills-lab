# production-delivery-manager 工作区隔离规则增强

## 背景

`production-delivery-manager` 已覆盖需求澄清、检索、计划、实现、验证、钢人反论和交付，但首版没有把工作区隔离作为显式 gate。对于生产级交付、长周期任务和多 agent 并行写代码，缺少该 gate 容易导致用户本地改动被误碰、并行写入范围重叠、临时产物残留，或把隔离 worktree 当成最终验收工作区。

2026-05-29 追加问题：实际使用中，agent 可能在用户主工作区触发任务后创建 worktree，在 worktree 内完成修改和验证，却没有把结果合并、cherry-pick 或应用回用户原始工作区/目标分支，最终仍按“已完成”交付，导致用户在主分支看不到效果，也无法判断是否已在真实交付面验收。

## 目标

- 在正式计划和实现前显式判断当前工作区是否可用。
- 要求在 Git 仓库中先检查 `git status --short`。
- 明确本地未提交或未跟踪改动只是判断上下文，不是自动阻断条件。
- 对大改动、高风险重构、长周期任务、多 agent 并行写代码或用户需要保留当前工作区的情况，优先使用独立分支或 git worktree。
- 对小型、可逆、低风险文档或单文件变更，允许说明理由后继续使用当前工作区，避免制造额外清理成本。
- 对主分支上同时存在人工文档改动的场景，只要改动范围不重叠、最终验收目标仍是当前工作区，可以继续在当前工作区做可审查的增量变更。
- 交付时报告工作区决策、清理状态和剩余未跟踪文件。
- 明确原始工作区/当前分支是默认交付目标，除非用户要求 PR-only、branch-only 或接受 worktree/分支作为交付物。
- worktree 只作为候选执行面；未回灌到交付目标并在交付目标验证前，不允许声称任务完成。

## 非目标

- 不强制所有任务都创建 worktree。
- 不把“存在本地改动”解释为必须停止、必须 worktree 或必须要求用户先提交。
- 不替代具体项目自己的分支、提交、发布或验收规则。
- 不允许因为使用 worktree 而跳过最终目标工作区或真实验收环境确认。
- 不强制所有 worktree 产物自动合并；若存在冲突、重叠脏改、权限或用户偏好限制，必须降级为候选实现/分支交付并说明未应用到目标分支。

## 规则变更

- `SKILL.md` 的交付循环新增 `Workspace isolation`。
- `Gate Rules` 新增 `Workspace Isolation`，要求检查 git 状态、识别无关用户改动、选择当前工作区/分支/worktree，并明确本地改动不是自动阻断条件。
- `Delivery Plan` 必须包含 workspace decision。
- `Delivery Plan` 必须包含 delivery target 和隔离实现的 integration method。
- `Implementation` 必须关注临时文件、测试产物和本地输出清理。
- `Verification` 必须优先在 delivery target 执行；仅在 worktree 验证时必须标记为 partial evidence。
- `Handoff` 必须包含 workspace、delivery target、integration 和 cleanup status。
- `delivery-gates.md` 新增 `Gate 2.5: Workspace Isolation`，并定义当前工作区、分支或 worktree 的适用条件。
- `delivery-gates.md` 新增 `Gate 4.5: Delivery-Target Integration`，要求最终验证前确认变更已进入交付目标。
- `delegation-patterns.md` 要求代码写入型子 agent 使用指定分支或 worktree，并清理自己产生的临时产物；主 agent 负责将候选变更整合到交付目标。

## 验收

- `quick_validate.py ./skills/production-delivery-manager` 通过。
- `git diff --check` 通过。
- README smoke check 能体现多 agent 并行场景下的 git status、worktree 和清理状态要求。
