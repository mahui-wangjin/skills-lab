# Design to Frontend Fidelity Inventory

## 背景

用户反馈：Figma 高保真落地时，模型即使能读取目标节点 Dev Mode/MCP 结构化上下文，仍会漏图标、按钮、边线、分割线、状态标签或其他高保真细节。既有规则已经要求结构化源优先、图标/细节事实源锁定、真实浏览器验收，但缺少一个强制中间产物来回答“设计里到底有哪些可见元素必须出现”。

本次失败场景以 Figma node `4uUTQQbLTKun5YerfYow7R / 2:6039` 为代表：结构化源可以返回复杂页面结构、图标资产、按钮、tabs、阶段卡、任务列表、进度条、分割线和边框容器，但模型仍可能在实现和验收阶段凭主观印象漏项。

## 决策

`design-to-frontend-delivery` 新增“可见元素清单与浏览器对账”门禁：

- Figma、设计平台、高保真还原或反复精修任务，在编码或最终精修前必须建立 compact visible-element inventory。
- 清单覆盖非平凡可见元素：shell/page frame/content/repeated groups/local controls/overlays/decoration/data-state、图标/插画/logo/头像/SVG/bitmap、按钮/链接/tabs/chips/badges/progress/list rows/table rows/dividers/border containers、关键文本/数字/状态文案和 state variants。
- 每个条目或重复组必须映射 source -> implementation：Figma node/asset/token、Dev Mode/MCP 字段、Code Connect、导出资产、项目组件/token、代码文件、资源路径、fixture/state owner。
- 每个条目标注 `exact reuse`、`project component/token`、`approved fallback`、`missing/blocked` 或 `out of scope`。
- Gate 3 必须在真实浏览器按清单对账。漏图标、漏按钮、漏边线/分割线、数量不一致、资源 404、文本溢出、遮挡、不可见、未批准替换或状态 variants 缺失都算验收缺陷。
- 无法进行真实浏览器对账时，只能交付 `conditional`、`self-reviewed` 或代码级候选结果，并列出未对账项。

## 影响范围

- 更新 `skills/design-to-frontend-delivery/SKILL.md`：新增 Fidelity Inventory and Reconciliation Contract，并纳入三道闸门。
- 更新 `references/assets-and-visual-fidelity.md`：增加可见元素清单模板和浏览器对账要求。
- 更新 `references/convert-and-polish.md`：在 Gate 1、Gate 2、Gate 3 中要求清单、实现映射和浏览器对账。
- 更新 `references/polish-existing-project.md`：对既有实现增加可见元素差距审计。
- 更新 `references/delivery-checklists.md`：把设计元素对账加入统一验收和收尾输出。
- 更新 `agents/openai.yaml` 与 `README.md`：补充触发提示与手工 smoke case。

## 钢人反论

反论 1：这会不会让小改动过重？

回应：清单只针对 Figma/设计平台/高保真/反复精修/漏细节投诉等场景；普通小改动只需紧凑列非平凡元素和重复组，不要求逐像素或逐子节点展开。

反论 2：MCP 已经给了参考代码，为什么还要清单？

回应：MCP 参考代码是信息源，不是交付验收合同。清单把“源里有什么”转成“实现里必须有什么”，防止模型边看边写后凭感觉验收。

反论 3：清单会不会诱导照抄绝对定位？

回应：清单回答“哪些元素必须出现并对账”，不是“按 x/y 坐标布局”。布局仍受 Layout Fidelity Contract 约束，普通页面必须优先 Flex/Grid/flow。

反论 4：图标或细节找不到怎么办？

回应：必须记录 `missing/blocked` 或 `approved fallback`，并反馈资产/来源缺口；不能静默用相似图标、默认边框或个人审美替代。

反论 5：浏览器验收成本高怎么办？

回应：最小真实浏览器验收是前端质量主门禁，可直接执行；高成本 AI 探索式 E2E 仍按既有规则先向用户确认预算、覆盖范围和停止条件。

## 验证标准

- `quick_validate.py` 对 `skills/design-to-frontend-delivery` 通过。
- `git diff --check` 通过。
- `npx skills add . --list --full-depth` 能发现仓库 skill。
- 关键词检索能命中 `visible-element inventory`、`可见元素`、`Fidelity inventory`、`设计元素对账`、`漏图标`、`漏按钮` 或 `divider`。
- 从远端重新安装后，全局安装目录也包含上述规则。
