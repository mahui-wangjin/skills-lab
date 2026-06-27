# production-delivery-manager 文档归属与结果汇总优化

## 背景

用户反馈：Agent 把过程性台账、执行记录和流水式说明写进原本不是台账用途的项目文档。用户真正关心的是最终汇总：关键成果、关键改动、最终验证、剩余风险和下一步。

这不是“是否需要记录证据”的问题，而是文档归属错误：把 evidence ledger、最终验收报告和正式项目文档混在一起。

## RED 压力场景

```text
用户要求生产级交付。
Agent 一边实现一边把以下内容写进已有产品/架构/开发文档：
- 我先做了什么，后来发现什么
- 失败命令、重跑命令和调试流水
- 子 Agent 过程记录
- 临时 evidence ledger
- 已被最终实现取代的中间尝试

最终用户打开正式文档，看见的是施工日志，而不是长期有效的事实。
```

失败模式：

- 把 `update docs or task ledgers when project rules require it` 误读成“可以把过程写进 docs”。
- 把 evidence ledger 当作正式文档内容。
- 把 Human Validation Packet 写成开发日记。
- 把 report/evidence/docs 三种 artifact 混用。

## 设计变更

- `SKILL.md` 增加 result-first handoff 与 document routing rule。
- `delivery-gates.md` 增加 Gate 4.1 Document Routing。
- `human-validation-report.md` 增加 Document Routing Boundary，并补充 Key Changes 结果区。
- `agents/openai.yaml` 默认提示加入 document-routing checks。
- README 增加文档归属与最终汇总 smoke case。

## 正确归属

正式项目文档只写：

- 长期产品行为。
- 架构边界和模块职责。
- 公共接口、数据契约和操作规则。
- 已接受的决策和明确后续承诺。

最终交付摘要只写：

- 关键成果。
- 关键改动。
- 最终验证。
- 剩余风险。
- 下一步。

`.production-delivery-reports/` 或项目明确台账路径才承载：

- 结果型 HTML 验收报告。
- 被最终报告引用的截图、短日志、CI/workflow 证据。
- 必须持久化的 evidence artifact。

默认不持久化：

- 调试流水。
- 失败重试全过程。
- raw command dumps。
- 子 Agent transcript。
- 已被最终实现取代的中间尝试。

## 钢人反论

### 反论 1：没有过程记录，后续怎么追责或复盘？

回应：默认交付不是审计追踪。若用户明确要求 audit trail，可把过程证据放到报告 evidence 或项目批准的台账路径，并标注用途；不能污染正式 source-of-truth docs。

### 反论 2：项目规则要求更新 docs，是否仍要写？

回应：要写长期事实，但不是写过程。比如架构边界、接口契约、使用规范、验收标准可以进 docs；“我跑了什么命令、失败了几次”不进 docs。

### 反论 3：失败检查是否要隐藏？

回应：不隐藏。仍在最终验证或报告中说明失败/跳过检查对风险的影响，但按结果和风险表达，不写完整流水账。

### 反论 4：小任务是否需要报告？

回应：不需要。小任务直接给结果、验证和风险；除非用户明确要求，不生成 HTML report，不写过程文档。

## 验收标准

- production-delivery-manager quick_validate 通过。
- 全量 5 个 skills quick_validate 通过。
- README smoke case 覆盖“只要最终汇总，不要过程污染正式文档”。
- 安装版包含 Document Routing、Document Routing Boundary、Key Changes 和 result-first handoff 规则。
