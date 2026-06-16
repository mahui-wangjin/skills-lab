# production-delivery-manager Human Validation Report 增强

## 背景

`production-delivery-manager` 已经要求需求澄清、工作区隔离、委派决策、验证证据、钢人反论和最终交付。但用户反馈指出：高质量交付的证据没有被整理成人可快速验收的界面，导致用户虽然不想审全量代码，仍然难以判断架构、核心逻辑和残余风险是否可接受。

同时，项目中已有 CI / release-candidate workflow 这类机器门禁。它们应作为可重复验证证据进入交付报告，而不是被报告替代。

## 设计目标

- 将“人的 validation 是否友好”纳入生产级交付定义。
- 保留小任务轻量化，不让每个小改动都生成报告。
- 对中等及复杂任务强制输出 Human Validation Packet。
- 对复杂/生产级/发布候选/高风险/浏览器验收任务生成 HTML 交付报告。
- 统一报告默认目录为 `.production-delivery-reports/`，便于在业务仓库中归档、提交或外部保存。
- 用脚本生成报告骨架，降低格式漂移和手写遗漏。
- 明确 CI/workflow 是证据来源，报告负责解释证据。
- 明确截图是验证证据的一类，但只能证明可见 UI 状态，不能替代后端、权限、数据隔离、幂等、事务等验证。

## 关键规则

默认报告路径：

```text
.production-delivery-reports/
  YYYY-MM-DD_<short-slug>/
    index.html
    evidence/
    manifest.json
```

触发 HTML 报告的场景：

- 用户要求报告、证据包、validation package、HTML report 或 delivery trace。
- 任务为复杂或生产级，且涉及架构、核心业务逻辑、权限、安全、数据、schema、migration、队列、worker、外部副作用、AI runtime 或发布流程。
- 发布候选、合并主线、上线、回滚或最终验收。
- 浏览器/UI 验收产生截图、trace、console/network 检查或产品验收证据。
- CI/workflow、本地验证、截图、子 Agent 审查、分支或 worktree 证据需要统一证据视图。

不默认生成报告的场景：

- 错别字、很小文档改动、单行可逆修改、只读解释、临时排查。

## 脚本职责

新增 `skills/production-delivery-manager/scripts/create_report.py`。

脚本只负责确定性骨架：

- 创建 `.production-delivery-reports/<日期>_<slug>/`。
- 创建 `index.html`。
- 创建 `evidence/`。
- 创建 `manifest.json`。
- 写入稳定章节和占位内容。

脚本不负责判断任务是否完成，也不伪造测试结果。Agent 必须用真实验证证据替换报告占位内容。

## CI / Workflow 关系

CI / workflow 是证据提供者：

- lint/typecheck/build/test/e2e/migration/release-candidate 等 workflow 结果可作为 `automated_assertion` 或 `build_typecheck` 证据。
- 报告应记录 workflow 名称、提交或分支、运行结果、artifact 或链接，以及“证明什么 / 不证明什么”。
- CI 通过不等于用户验收，不等于生产已发布，也不等于真实第三方系统已验证。
- CI 未运行时必须写明，不得用本地验证冒充 CI。

HTML 报告是证据汇总和解释层：

- 把 CI、本地命令、浏览器截图、日志摘录、子 Agent 审查和人工检查组织成可审页面。
- 给用户最少但关键的架构、核心逻辑和风险验收点。

## 文件改动

- `skills/production-delivery-manager/SKILL.md`
  - 扩展触发描述。
  - 将第 9 步改为 Human Validation Handoff。
  - 增加 Human Validation Packet 和 HTML 报告完成标准。
- `skills/production-delivery-manager/references/human-validation-report.md`
  - 新增报告触发规则、默认目录、证据等级、CI/workflow 证据、HTML 契约、截图限制和最终回复契约。
- `skills/production-delivery-manager/scripts/create_report.py`
  - 新增报告骨架生成脚本。
- `skills/production-delivery-manager/references/delivery-gates.md`
  - 新增 Gate 5.5 Human Validation Report。
  - 扩展最终 handoff 模板。
- `skills/production-delivery-manager/references/steelman-review.md`
  - 钢人反论增加“交付是否可被人类验收”的审查维度。
- `skills/production-delivery-manager/references/delegation-patterns.md`
  - 补充 Evidence Reporter / Docs Release surface 对 HTML 报告和 validation packet 的检查责任。
- `skills/production-delivery-manager/agents/openai.yaml`
  - 更新 UI 描述和默认 prompt。
- `README.md` 与 `docs/README.md`
  - 同步公开口径和文档索引。

## 可维护性判断

本次没有把报告模板和证据等级全部塞进 `SKILL.md` 主体，而是放入独立 reference 和脚本。原因：

- `SKILL.md` 保持触发、核心流程和硬门禁，避免上下文过重。
- 报告格式未来可能单独迭代，不应和交付主流程强耦合。
- HTML 模板、证据等级、截图限制、CI 证据映射等属于条件加载资料，符合 skill progressive disclosure。
- 脚本只做脚手架，不把业务判断写死，避免降低 skill 的适用范围。

## 验证标准

- `quick_validate.py skills/production-delivery-manager` 通过。
- 全仓 5 个 skill 的 `quick_validate.py` 通过。
- `scripts/create_report.py` 能在临时目录生成 `index.html`、`evidence/` 和 `manifest.json`。
- `npx skills add . --list --full-depth` 能发现 5 个 skills。
- `git diff --check` 无空白错误。
- 全局安装 `production-delivery-manager` 后，安装目录包含 `human-validation-report.md`、`create_report.py` 和 `.production-delivery-reports` 规则。
