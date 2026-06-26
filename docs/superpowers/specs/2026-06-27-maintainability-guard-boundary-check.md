# maintainability-guard 轻量边界检查强化

## 背景

用户反馈：当前 `maintainability-guard` 虽然写了“行数只是报警器”，但模型在文件未超过阈值时仍容易跳过可维护性判断，尤其没有认真判断某段逻辑是否应该复用、是否应该抽离成稳定边界。

本次优化目标不是把 skill 改成“小文件也必须拆”，而是让 Agent 在所有代码改动前都先做轻量边界检查；当复用、重复、测试困难、依赖方向或新变化轴出现时，即使文件小于 400 行，也必须输出 Maintainability Gate。

## RED 压力场景

当前旧规则容易失败的压力场景：

```text
你要在一个 260 行 React 页面里新增 status -> label/color/action 的映射。
PM 说后面另一个页面也会用，但今天只要求这个页面上线。
当前 skill 表格写着 <400 lines Continue normally unless responsibilities are already mixed。
你很赶时间，是否直接把映射写在页面里？
```

说明：本轮工具规则不允许在用户未明确要求子代理/并行代理时派生子代理，因此 RED 采用降级压力分析，而非冒充已完成真实子代理基线测试。该场景来自用户明确反馈的失败模式：未超过行数阈值时模型忽略复用和抽离判断。

预期失败模式：

- Agent 把 `< 400` 理解成免检通行证。
- Agent 引用 `Do Not Over-Split`，认为只有一个当前调用方所以不抽。
- Agent 没有显式检查“第二用例已经被命名”“下一个 Agent 会不会复制同一映射”“抽离是否能形成输入输出契约”。
- Agent 最终继续把可复用映射塞进页面，后续第二页面再复制一份。

## 设计变更

- 新增 `Always-On Boundary Check`：任何代码改动前都要判断新增职责、行为类型、第二调用方/第二用例、重复压力、测试边界和抽离是否只是转发。
- 调整行数阈值：`< 400` 从“正常继续”改为“轻量边界检查后才能继续”，明确小文件也可能因为复用、重复、混职责、依赖方向或测试边界失败。
- 新增 `Gate Triggers`：除 800 行以上外，复用 rule/adapter/mapper/validator/permission/status/formatter/hook/workflow/presentation transform、相似逻辑、测试困难、高层依赖低层细节、用户维护性担忧都触发完整 Gate。
- 扩充 Gate 模板：加入 always-on check 结果和 split contract，要求说清输入、输出、错误、副作用和 owner。
- 新增 `Reuse and Extraction Test`、`Common Rationalizations`、`Red Flags`，专门反制“不到 400 行”“只有一个调用方”“不要过度拆分”等常见逃逸理由。

## 钢人反论

### 反论 1：轻量检查会把所有小改动流程化，拖慢简单修复。

回应：轻量检查不是强制输出完整 Gate。只有复用、重复、测试困难、依赖方向、用户维护性担忧等触发项出现时才输出完整 Gate；普通同职责小改动仍可继续原地开发。

### 反论 2：把“可能第二用例”作为触发项会导致过早抽象。

回应：新规则区分“第二-use pressure”和“Contract pressure”。只有第二用例已命名、复制压力真实，且能形成具体输入/输出/错误/副作用合同时才建议抽离；否则要求先澄清接口，不允许抽成 `utils/helpers/common`。

### 反论 3：强调复用会和 `Do Not Over-Split` 冲突。

回应：本次明确了边界：`Do Not Over-Split` 反对转发包装、泛名文件、把总是一起变化的逻辑拆散；它不反对抽离重复 mapping、permission、status、adapter 或难测试规则。

### 反论 4：skill 文档变长后，模型可能更不读。

回应：frontmatter description 已改为触发条件优先；核心新增内容集中在前半部分的 Always-On Boundary Check 和 Gate Triggers，后半部分 Rationalizations/Red Flags 用于压力下反制逃逸理由。README 和 AGENTS 同步给出短规则，降低日常加载成本。

## 验收标准

- `skills/maintainability-guard/SKILL.md` 通过 quick_validate。
- README 的推荐项目规则不再只写 800 行触发，而包含轻量边界检查和复用/重复触发。
- 全局安装版 `C:\Users\97227\.agents\skills\maintainability-guard\SKILL.md` 包含 `Always-On Boundary Check` 与 `Reuse and Extraction Test`。
- git diff 不包含 `.idea/` 或无关文件。
