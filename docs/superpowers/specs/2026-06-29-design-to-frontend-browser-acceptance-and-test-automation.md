# design-to-frontend-delivery 浏览器验收与测试自动化治理

## 背景

用户反馈：前端交付中把 `E2E/smoke/browser/screenshot` 并列会误导模型，把 smoke 当成真实浏览器验收的替代品；同时 smoke 脚本容易继续承接选择器、点击、截图、断言、报告和修复尝试，最终膨胀成几千行，反而降低可维护性和问题修复能力。

## 决策

`design-to-frontend-delivery` 将真实浏览器验收设为前端质量主门禁：

- 单元测试、组件测试、typecheck、lint 负责逻辑和静态正确性。
- smoke 只负责健康检查：应用启动、关键路由加载、基础壳层渲染、明显控制台或网络失败暴露。
- 真实浏览器 E2E、agent-browser、Playwright、Cypress、browser automation、浏览器驱动截图/trace 或 Storybook-in-browser 负责产品体验验收：布局、响应式、弹层、交互、资源加载、控制台/网络错误、截图证据和用户工作流。
- AI 浏览器验收负责收集可复核证据，不负责用主观判断无限探索。证据应包括命令结果、断言、trace、截图、console/network 日志和明确交互步骤。
- 最小真实浏览器验收是默认质量门禁；高成本 AI 探索式 E2E 需要用户确认验收预算。高成本范围包括跨多路由/多视口/多轮视觉 diff/大范围回归/登录或第三方流程/慢速远端环境，或明显增加时间与 token 的探索式浏览。
- 确认高成本 AI E2E 时，必须说明目标流程、视口、证据、预计成本或时间、停止条件和人工复核项。
- 无法进行真实浏览器验收或浏览器调试时，必须提醒用户缺少 `console/network/runtime/layout/screenshot` 证据，说明需要的环境、工具或访问方式，并把结果降级为 conditional、self-reviewed 或代码级候选结果；不得用 smoke-only 结果声称 demo-ready、accepted、fixed 或 complete。

`maintainability-guard` 将测试和自动化代码视为普通代码治理对象：

- smoke、E2E、browser automation、validation、reporting、fixtures、selectors 和 helpers 都必须执行可维护性边界检查。
- AI-driven browser/E2E automation 必须证据化和预算化：目标流程、视口、断言、截图/trace、console/network 日志、停止条件；高成本探索先确认验收预算。
- runner/bootstrap、fixtures/test data、selectors/page objects/actions、assertions、screenshot/console/network/evidence capture、reporting/cleanup/retry policy 是独立职责。
- 测试自动化文件混入三类以上职责时，新增场景前先输出 Maintainability Gate。
- 超过 1200 行的测试自动化文件，扩展前至少拆一个清晰职责；超过 2000 行不新增场景直到有恢复切片；超过 3000 行视为 maintainability incident。

## 影响范围

- `skills/design-to-frontend-delivery/SKILL.md`
- `skills/design-to-frontend-delivery/references/convert-and-polish.md`
- `skills/design-to-frontend-delivery/references/polish-existing-project.md`
- `skills/design-to-frontend-delivery/references/frontend-continuation.md`
- `skills/design-to-frontend-delivery/references/delivery-checklists.md`
- `skills/maintainability-guard/SKILL.md`
- `README.md`

## 验收

- `design-to-frontend-delivery` 和 `maintainability-guard` 通过 `quick_validate.py`。
- `git diff --check` 通过。
- 全局安装副本 `C:\Users\97227\.agents\skills\...` 与源 skill 内容一致（忽略 CRLF/LF 行尾差异）。
