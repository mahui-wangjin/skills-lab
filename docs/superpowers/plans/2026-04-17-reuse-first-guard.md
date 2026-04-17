# reuse-first-guard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `skills-lab` 中新增可安装的全局通用 skill `reuse-first-guard`，用于在关键开发决策前执行“复用优先、必要时再做选型评估”的半阻断流程。

**Architecture:** 该实现以单个 skill 目录为核心，主流程写入 `SKILL.md`，把评估细则下沉到 `references/evaluation-criteria.md`，再通过 `agents/openai.yaml` 提供安装后的可发现性。仓库侧同步更新 `README.md`、`AGENTS.md` 与 `docs/README.md`，并以 `quick_validate.py` 和最小 smoke check 作为验收闭环。

**Tech Stack:** Markdown, YAML, Python validation script (`quick_validate.py`)

---

### Task 1: 建立计划与骨架

**Files:**
- Create: `docs/superpowers/plans/2026-04-17-reuse-first-guard.md`
- Create: `skills/reuse-first-guard/SKILL.md`
- Create: `skills/reuse-first-guard/agents/openai.yaml`
- Create: `skills/reuse-first-guard/references/evaluation-criteria.md`

- [ ] **Step 1: 写入实施计划**

将本文件写入仓库，固定文件边界、任务顺序与校验命令。

- [ ] **Step 2: 初始化 skill 骨架**

Run:

```powershell
python C:\Users\97227\.codex\skills\.system\skill-creator\scripts\init_skill.py reuse-first-guard --path E:\develop\code\my-project\skills-lab\skills --resources references --interface "display_name=Reuse First Guard" --interface "short_description=Enforce reuse-first checks before new build decisions." --interface "default_prompt=Use $reuse-first-guard before building new dependencies, services, infrastructure, or modules from scratch."
```

Expected: 创建 `skills/reuse-first-guard/`、`SKILL.md`、`agents/openai.yaml` 和 `references/`。

- [ ] **Step 3: 检查骨架文件是否生成**

Run:

```powershell
Get-ChildItem -Recurse E:\develop\code\my-project\skills-lab\skills\reuse-first-guard
```

Expected: 输出包含 `SKILL.md`、`agents\openai.yaml`、`references\`。

### Task 2: 编写 skill 主体与参考规则

**Files:**
- Modify: `skills/reuse-first-guard/SKILL.md`
- Create: `skills/reuse-first-guard/references/evaluation-criteria.md`
- Modify: `skills/reuse-first-guard/agents/openai.yaml`

- [ ] **Step 1: 用最终 frontmatter 和主体流程替换模板**

在 `skills/reuse-first-guard/SKILL.md` 中写入：

- 最终 `name` 和 `description`
- 强制触发条件
- 两段式执行流
- 半阻断策略
- 固定输出格式
- 何时读取 `references/evaluation-criteria.md`

- [ ] **Step 2: 写入评估维度参考文档**

在 `skills/reuse-first-guard/references/evaluation-criteria.md` 中写入：

- 复用路径检查顺序
- 常见判断问题
- 允许自研的例外条件
- 推荐输出时的简版评估维度
- 至少 4 个典型开发场景

- [ ] **Step 3: 校对 agent 元数据**

确保 `skills/reuse-first-guard/agents/openai.yaml` 与 skill 目标一致，核心字段应为：

```yaml
interface:
  display_name: "Reuse First Guard"
  short_description: "Require reuse-first checks before building new dependencies, services, or custom modules."
  default_prompt: "Use $reuse-first-guard to decide whether to reuse, buy, integrate, generate, or build when a development task introduces new technical decisions."
```

### Task 3: 接入仓库规则与文档入口

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/README.md`

- [ ] **Step 1: 更新 README 技能列表**

在 `README.md` 中：

- 新增 `reuse-first-guard` 到 `Available Skills`
- 补安装命令示例
- 说明其用于关键开发决策前的复用优先与选型守门

- [ ] **Step 2: 更新项目规则**

在 `AGENTS.md` 中新增硬性规则：

- 新增依赖、新服务、新基础设施、新自研模块、重大重构时必须先使用 `reuse-first-guard`
- 若判断有更低成本复用路径，先给替代方案与推荐结论
- 若仍要自研，必须写明理由再进入实现

- [ ] **Step 3: 更新 docs 索引**

在 `docs/README.md` 中补充：

- `reuse-first-guard` skill 路径
- 实施计划文档路径

### Task 4: 验证与收尾

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/README.md`
- Modify: `skills/reuse-first-guard/SKILL.md`
- Modify: `skills/reuse-first-guard/references/evaluation-criteria.md`
- Modify: `skills/reuse-first-guard/agents/openai.yaml`

- [ ] **Step 1: 运行结构校验**

Run:

```powershell
python C:\Users\97227\.codex\skills\.system\skill-creator\scripts\quick_validate.py E:\develop\code\my-project\skills-lab\skills\reuse-first-guard
```

Expected: `Skill is valid!`

- [ ] **Step 2: 运行最小 smoke check**

人工检查以下 4 个请求是否会被该 skill 正确覆盖：

- `我要做一个用户鉴权模块`
- `我要给现有系统接入支付`
- `我要做一个只属于我们业务的核心排程引擎`
- `我要换掉项目里的表单库`

Expected: 前两类优先推荐复用路径，第三类可在满足理由时允许自研，第四类输出简版选型判断。

- [ ] **Step 3: 查看工作区差异**

Run:

```powershell
git diff -- README.md AGENTS.md docs/README.md docs/superpowers/plans/2026-04-17-reuse-first-guard.md skills/reuse-first-guard
```

Expected: 差异仅包含本次新增 skill、规则接入与文档更新。

- [ ] **Step 4: 更新项目 memory**

写回：

- 本轮目标
- 关键改动
- 风险或阻塞
- 下一步
