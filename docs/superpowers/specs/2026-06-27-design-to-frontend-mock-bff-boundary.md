# design-to-frontend-delivery mock/BFF 边界优化

## 背景

用户反馈：在静态 mock 页面或设计图还原阶段，Agent 容易把“未来 BFF 会返回的数据和状态”提前写成前端推导逻辑，甚至解释成“复杂 API 状态”。这会把本应由 BFF/domain 负责的派生业务指标、生命周期/状态流转、授权/资格、可执行动作裁定、集成状态归一化等领域裁定塞进静态页面。

用户期望：静态页就是静态页。mock 数据可以像未来 BFF 响应一样集中，方便替换；前端只保留很轻的 UI 状态，不应该在 mock 阶段干 API/BFF 的活。

## RED 压力场景

```text
用户要求按设计稿做一个静态业务页面，未来真实数据由 BFF 返回。
Agent 为了“工程化”，新增 model/selectors/reducer：
- 根据 fixture 字段推导领域生命周期状态
- 根据记录类型推导授权/资格或可执行动作裁定
- 根据多个业务枚举组合推导展示文案、动作状态和目标去向
- 模拟 loading/retry/cache/API 状态机
最终页面能跑，但前端承担了 BFF 的业务裁定。
```

失败模式：

- 混淆静态 mock 阶段与真实 API 集成阶段。
- 把 BFF-shaped fixture 误当成前端领域模型。
- 为静态页面实现 API 状态机、业务 reducer、权限/可操作性推导。
- 只说“未来接 BFF 可替换”，但实际上页面 JSX 和模型已经绑定了前端推导规则。

说明：本轮未派生子代理做真实 baseline 测试；该 RED 来自用户明确反馈的失败模式，作为本次规则修复的压力场景。

## 设计变更

- 在 `SKILL.md` 增加 `Mock/BFF Boundary Contract`，明确静态 mock 不是 API 集成。
- 在 `convert-and-polish.md` 增加 `Mock/BFF 边界`，约束设计转前端时的 mock 数据、UI 状态和非目标项。
- 在 `polish-existing-project.md` 增加 mock/API 边界审计，识别既有页面中是否已经混入 BFF/domain-owned 推导。
- 在 `delivery-checklists.md` 增加数据边界层、Gate 1 数据范围确认、Gate 2 mock/BFF 边界记录、Gate 3 API 状态机非目标验收。
- 在 README smoke case 中加入“静态 mock 列表页/详情页，未来由 BFF 返回数据”的判断场景。

## 边界口径

前端 mock 阶段可以做：

- BFF-shaped fixture，便于后续替换数据来源。
- 当前 tab、选中项、展开项、弹框开关、本地表单草稿。
- loading/error/empty 的演示表面。
- 演示级基础校验和格式反馈，但不能升级成授权、资格或工作流裁定。
- 很薄的展示选择器：按 id 取 fixture、校验 tab key、统计已给定列表数量、把 fixture 字段传给组件。

前端 mock 阶段不该做：

- 派生业务指标、生命周期/状态流转、授权/资格和可执行动作裁定。
- 集成状态归一化、跨记录工作流、目标去向裁定。
- 按业务枚举组合推导领域文案、动作状态或目标去向。
- 假 API 状态机、轮询、缓存、乐观更新、重试策略、权限引擎或领域 reducer。

真实 API 集成时才需要确认：

- 契约来源。
- loading/error/empty 行为。
- mutation 副作用。
- cache policy。
- authorization assumptions。
- 验证路径。

## 钢人反论

### 反论 1：前端总得有一些状态，否则页面不能交互。

回应：规则允许轻量 UI 状态，例如 tab、弹框、选中项、展开项、本地表单草稿和演示用 loading/error/empty。禁止的是业务状态裁定和 API 状态机。

### 反论 2：mock 数据如果不做推导，会不会重复写很多状态？

回应：静态 mock 的目标是展示与替换，不是归一化领域模型。可以把未来 BFF 会返回的展示字段直接写进 fixture。重复少量展示字段比在前端提前实现错误业务规则更低风险。

### 反论 3：做 BFF-shaped fixture 会不会变成伪 API 契约？

回应：规则要求命名为 fixture/mock，并明确“replaceable data seam”。如果用户没有提供真实契约，不得把 fixture 声称为 API contract。

### 反论 4：有些项目没有 BFF，前端确实要算业务规则。

回应：这属于真实产品架构/接口集成范围，不是静态设计落地默认行为。若用户明确要求前端承担规则，应切换范围，确认契约、规则来源、验证路径和长期维护边界。

### 反论 5：规则会不会误伤基础校验和格式反馈？

回应：不会。规则允许演示级基础校验、格式反馈和本地表单草稿；禁止的是把这些 UI 反馈升级成授权、资格、生命周期或跨记录工作流裁定。

### 反论 6：规则会不会禁止前端展示后端将来返回的文案或动作？

回应：不会。前端可以展示 fixture 或真实接口返回的字段。禁止的是在 mock 阶段根据业务枚举组合自行推导领域文案、动作状态或目标去向。

## 验收标准

- `design-to-frontend-delivery` quick_validate 通过。
- 全量 5 个 skills quick_validate 通过。
- README smoke case 覆盖静态 mock/BFF 返回数据场景。
- 全局安装版包含 `Mock/BFF Boundary Contract`、`Mock/BFF 边界` 和数据边界层。
