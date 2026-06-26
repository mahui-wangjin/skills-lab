# production-delivery-manager 结果优先报告优化

## 背景

`production-delivery-manager` 在复杂交付中要求 Human Validation Packet 和 HTML 交付报告。实际使用中，Agent 容易在实现过程中反复编写报告：发现问题、修改实现、重写报告、再次发现问题、再次重写报告，导致核心实现被频繁打断。

用户真正关心的是最终成果：交付了什么、加了哪些功能、如何验证、还有哪些风险，而不是 Agent 的迭代过程。

## 目标

- 保留生产级交付的可审性和证据完整性。
- 把 HTML 报告从“过程记录”改为“最终成果验收面”。
- 让 Agent 在实现阶段专注实现和验证，只维护轻量 evidence ledger。
- 最终报告只总结最终状态、已交付能力、证据、风险和人工验收点。

## 新口径

实施过程中只维护 evidence ledger：

```md
- Evidence: <command/check/artifact>
  Result: <passed/failed/skipped/not run>
  Proves: <one sentence>
  Limit: <one sentence>
```

HTML 报告只在最终阶段生成或补齐：

1. 交付目标已回灌。
2. 最终验证已完成。
3. 钢人反论已完成。
4. 使用最终 evidence ledger 生成结果优先报告。

报告必须优先回答：

- Delivered capabilities：最终交付了哪些能力或行为变化。
- Human checkpoints：用户应验收哪些点。
- Evidence map：最终证据证明什么、不证明什么。
- Residual risk：仍有哪些未证明或需接受的风险。

报告不应包含：

- 逐步调试流水账。
- 已被最终实现取代的失败尝试。
- 原始命令长日志。
- 子 Agent transcript。
- 文件级逐行 diff 解说。

## 修改范围

- `skills/production-delivery-manager/SKILL.md`
- `skills/production-delivery-manager/references/delivery-gates.md`
- `skills/production-delivery-manager/references/human-validation-report.md`
- `skills/production-delivery-manager/scripts/create_report.py`
- `skills/production-delivery-manager/agents/openai.yaml`
- `README.md`

## 验收

- `production-delivery-manager` 仍能触发生产级交付门禁。
- 中等/复杂任务仍有 Human Validation Packet。
- 报告触发场景仍会生成 `.production-delivery-reports/<date>_<slug>/index.html`。
- 默认报告标题和结构转为结果优先：`Production Delivery Outcome`、`Delivered Capabilities`。
- 技能说明明确禁止在实现循环中反复打磨 HTML 报告。
