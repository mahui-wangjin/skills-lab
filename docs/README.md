# docs

## 文档索引

- 项目级规则文件：`../AGENTS.md`
- Memory MCP 项目标识：`skills-lab`
- 设计规格文档目录：`./superpowers/specs/`
- 当前新增设计文档：`./superpowers/specs/2026-06-30-design-to-frontend-framework-layout-gate.md`（将 design-to-frontend-delivery 的 frontend foundation gate 固化为前端交付、开发与精修门禁：真实项目、多页面交付、前端开发或精修前，先发现并锁定 app shell、route layout、page wrapper、content slot、scroll container、toolbar/tabs/breadcrumbs、overlay roots、grid/spacing/breakpoints、page archetype、组件映射、token/theme、route/menu/permission、table/list、form/validation、状态矩阵、真实数据压力和性能假设；已有 layout primitive、组件、token、表格/表单/弹层/路由权限 pattern 能承载时不得自造 page-local shell/container/grid/scroll/table/list/form shell、组件体系、校验体系、权限导航逻辑或 style scale；第一个同类页面形成 pattern seed，后续同类页面复用或记录 variant/exception）
- 当前新增设计文档：`./superpowers/specs/2026-06-30-design-to-frontend-responsive-foundation.md`（将 design-to-frontend-delivery 的响应式基座固化为通用方法论：固定设计画布只是 baseline，不是 viewport contract；固定画布、多页面 UI、dashboard/workbench、shell/page-frame 或响应式缺陷场景先记录 viewport/container 口径、canvas policy、layout primitives、query policy、tokenized spacing/gaps、任意值策略、固定值例外和代表性浏览器验收矩阵；具体屏幕尺寸只作样本，不写成通用规则，重复任意像素值需上收为 token、variant、layout primitive 或 framework config）
- 当前新增设计文档：`./superpowers/specs/2026-06-29-design-to-frontend-fidelity-inventory.md`（将 design-to-frontend-delivery 的高保真可见元素清单固化为门禁：Figma/设计平台/高保真/反复精修任务在编码或最终精修前先建立 compact visible-element inventory，覆盖图标、按钮、tabs、chips、progress、列表/表格行、分割线、边框容器、关键文案/数字/状态 variants，并建立 source -> implementation 映射；Gate 3 必须在真实浏览器按清单对账，无法浏览器对账时只能降级为 conditional/self-reviewed 或代码级候选结果）
- 当前新增设计文档：`./superpowers/specs/2026-06-29-design-to-frontend-browser-acceptance-and-test-automation.md`（将前端交付验收收紧为真实浏览器优先：smoke 只作健康检查，单元/组件/typecheck 只作补充证据；AI 浏览器验收以命令、断言、trace、截图和 console/network 日志等可复核证据为准，高成本 AI 探索式 E2E 先确认覆盖范围、时间或 token 成本、停止条件和人工复核项；无法进行真实浏览器验收或浏览器调试时必须提醒用户缺少 console/network/runtime/layout/screenshot 证据并降级结论；同时将 smoke/E2E/browser automation 脚本纳入 maintainability-guard，防止测试代码堆成巨型脚本）
- 当前新增设计文档：`./superpowers/specs/2026-06-28-design-to-frontend-detail-and-continuation.md`（将 design-to-frontend-delivery 的图标/细节事实源和后续前端开发门禁固化：远端或项目已有图标、SVG、tokens、border/padding/radius/shadow/motion/state variants 必须复用或明确 fallback，不能静默自造；API/BFF 对接、功能修改和 bugfix 进入 frontend-continuation，先确认 accepted baseline、契约来源、影响面、回归面和共享消费者，避免误伤其他页面）
- 当前新增设计文档：`./superpowers/specs/2026-06-28-design-to-frontend-layer-ownership-e2e.md`（将 design-to-frontend-delivery 的 UI 层级归属和 E2E 自测固化为交付门禁：设计或现有页面必须映射 app shell、page frame、content sections、collection items、local controls、overlay/feedback、decoration/media、data/state 的 owner、状态和 stacking/portal/overflow 边界；其中自测优先级已由 2026-06-29 浏览器验收文档进一步收紧）
- 当前新增设计文档：`./superpowers/specs/2026-06-28-design-to-frontend-common-surface-interactions.md`（将 design-to-frontend-delivery 的公共面和交互可用性固化为演示级门禁：设计稿只画内容区时先确认 content-only/inside-existing-shell/full-page-with-shell 并复用现有 shell、导航和统一 overlay/feedback roots；可点击元素必须具备语义控件、cursor、hover/active/focus-visible、disabled/loading、弹层关闭、键盘/触控和返回反馈闭环）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-documentation-governance-skill.md`（新增 documentation-governance 通用技能：用文档治理门禁区分 OpenSpec/change spec、ADR、正式 source-of-truth docs、索引、源码旁文档、交付证据、项目明确批准的 audit/evidence artifact、归档和不持久化内容，防止文档膨胀、重复真相和过程记录污染正式文档）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-design-to-frontend-assets-and-fonts.md`（将 design-to-frontend-delivery 的字体与资源真实性固化为高保真门禁：缺少字体、字重、图片、图标或媒体时先补项目可访问资源或明确 fallback/blocked，不继续用样式微调掩盖资源缺失）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-design-to-frontend-mock-bff-boundary.md`（将 design-to-frontend-delivery 的静态 mock 与真实 BFF/API 集成边界固化：mock 只做展示夹具和轻量 UI 状态，不提前实现 BFF/domain-owned 业务裁定或 API 状态机）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-design-to-frontend-project-structure.md`（将 design-to-frontend-delivery 的工程目录边界固化：先识别目标框架和项目目录约定，再按页面入口、feature 组件、fixtures、selectors/formatters、styles/assets、tests/stories 分责归位）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-production-delivery-manager-document-routing.md`（将 production-delivery-manager 的文档归属门禁固化：正式 docs 只写长期事实，最终交付只写成果/关键改动/验证/风险/下一步，临时过程记录不得污染原有文档）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-design-to-frontend-layout-fidelity.md`（将 design-to-frontend-delivery 的“1:1/高保真”口径收口为专业布局保真：追求高保真视觉关系，不承诺像素级 100%，普通布局优先 Flex/Grid/flow，禁止用大量绝对定位复刻坐标）
- 当前新增设计文档：`./superpowers/specs/2026-06-27-maintainability-guard-boundary-check.md`（将 maintainability-guard 从“800 行触发”强化为“轻量边界检查始终执行，可复用/重复/测试边界/依赖方向触发完整 Gate”）
- 已更新设计文档：`./superpowers/specs/2026-06-27-design-to-frontend-structured-source-first.md`（将 design-to-frontend-delivery 优化为平台无关的结构化源优先，设计平台/MCP/Dev Mode/组件映射/参考代码可用时不得降级为按截图复刻；2026-06-29 追加 Figma 节点级规则：优先读取目标 node/selection/frame 的 Dev Mode/MCP/Code Connect 上下文，不默认下载或渲染整张设计文件、整页 canvas 或整图截图）
- 上一轮设计文档：`./superpowers/specs/2026-06-27-production-delivery-manager-result-first-reporting.md`（将 production-delivery-manager 的 HTML 报告优化为结果优先验收面，实施中只维护 evidence notes，最终一次性生成或补齐报告）
- 上一轮设计文档：`./superpowers/specs/2026-06-16-production-delivery-manager-human-validation-report.md`（补充 Human Validation Packet、HTML 交付报告、证据等级、截图限制、CI/workflow 证据和 `.production-delivery-reports/` 默认目录）
- 上一轮设计文档：`./superpowers/specs/2026-05-29-production-delivery-manager-delegation-quality-gate.md`（补充复杂/生产级任务的 Delegation Quality Gate、独立专家视角和不委派钢人反审规则）
- 已更新设计文档：`./superpowers/specs/2026-05-27-admin-ui-pattern-system-design.md`（补充非 CRUD 后台页面范式、完成门禁、降级规则和 Windows UTF-8 校验口径）
- 上一轮设计文档：`./superpowers/specs/2026-05-27-maintainability-guard-design.md`
- 已更新设计文档：`./superpowers/specs/2026-05-26-production-delivery-manager-workspace-isolation.md`（补充 worktree 回灌到交付目标与目标面验证规则）
- 历史设计文档：`./superpowers/specs/2026-05-25-reuse-first-guard-project-local-reuse.md`
- 历史设计文档：`./superpowers/specs/2026-04-23-reuse-first-guard-headless-native-refinement.md`
- 实施计划文档目录：`./superpowers/plans/`
- 当前新增实施计划：`./superpowers/plans/2026-04-17-reuse-first-guard.md`
- 新增 skill：`../skills/reuse-first-guard/`
- 新增 skill：`../skills/production-delivery-manager/`
- 新增 skill：`../skills/maintainability-guard/`
- 新增 skill：`../skills/admin-ui-pattern-system/`
- 新增 skill：`../skills/documentation-governance/`

## 维护约定

- 与当前仓库业务、架构、流程、设计、文档、代码实现直接相关的长期事实，优先写入项目文档，再写入项目 memory。
- 当项目规则、流程或长期事实发生变化时，同步更新本文件，保持文档入口可追踪。
