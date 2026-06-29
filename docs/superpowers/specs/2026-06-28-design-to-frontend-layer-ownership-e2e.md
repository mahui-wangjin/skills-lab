# design-to-frontend-delivery UI 层级归属与 E2E 自测优化

## 背景

用户反馈：设计转前端时，Agent 容易犯 UI 层级错误，没有认真判断一个组件到底属于哪一层。常见表现是页面标题、筛选、工具栏、列表卡片、弹框、装饰背景和数据状态混在一起；视觉上接近设计稿，但组件 owner、状态 owner、portal/root、z-index 和 overflow 边界是错的。

用户进一步要求：改完后需要让 AI 做端到端自测，尽可能避免返工。不能只凭代码 diff、静态截图或自信判断说完成。

## RED 压力场景

```text
用户给出设计图，里面有页面标题、筛选区、列表卡片、卡片操作、弹框、toast 和背景装饰。
Agent 按视觉位置写组件：
- 页面标题和筛选被塞进第一个内容卡片
- 行级操作拥有页面级弹框状态
- 全局 toast 在列表组件里自建
- 背景装饰覆盖点击层
- z-index 一路加高掩盖 portal/overflow 错误
- 改完只跑 typecheck，没有真实打开页面点击
最终交付看起来差不多，但一进入真实页面就出现错层、遮挡、弹层不可关闭、移动端溢出或返工。
```

失败模式：

- 只看视觉邻近关系，不建立 UI layer ownership。
- 把 shell、page frame、content section、repeated item、local control、overlay/feedback、decoration/media、data/state 混成一个组件层。
- 用 z-index、absolute、portal 或 overflow 修补错层，而不是修正 owner。
- 没有真实浏览器或 E2E 自测，导致问题在用户验收时才暴露。

## 设计变更

- 在 `SKILL.md` 增加 `UI Layer Ownership Contract`。
- 在 `SKILL.md` 增加 `End-to-End Self-Test Contract`。
- 在 `convert-and-polish.md` 增加 UI 层级归属映射和 E2E 自测步骤。
- 在 `polish-existing-project.md` 增加 UI layer ownership 审计、最小精修合同中的自测路径和完成前自测要求。
- 在 `delivery-checklists.md` 增加 Gate 1/2/3 的 UI layer map、stacking/clipping 审计和 E2E/真实浏览器自测证据。
- 在 `source-priority.md` 要求将结构化源的 layer hierarchy 转成 frontend ownership map。
- 在 README smoke case 中增加 UI 层级归属场景。

## 边界口径

必须先判断的 layer：

- App shell layer：全局 layout、导航、侧栏、顶栏、账号区、route frame、providers。
- Page frame layer：页面标题、面包屑、页面 tabs、页面工具栏、页面筛选、页面级 loading/error/empty。
- Content section layer：正文区块、表单、图表、汇总、详情面板。
- Collection item layer：卡片、表格行、列表项、树节点、时间线项。
- Local control layer：字段组、局部校验、局部菜单、局部 popover、局部操作组。
- Overlay and feedback layer：modal、drawer、confirm、toast、tooltip、notification、floating action。
- Decoration and media layer：背景、插画、非交互装饰、媒体框、skeleton shimmer。
- Data/state layer：fixtures、selectors、formatters、UI state、BFF/API state、权限和领域决策。

必须完成的自测：

- 优先运行项目已有真实浏览器 E2E、browser、screenshot 或 Storybook 验收命令；2026-06-29 后 smoke 仅作为健康检查，不再与真实浏览器验收并列。
- 没有现成命令时，执行最小真实浏览器自测。
- 覆盖主流程、公共面、UI 层级、主要交互、弹层、桌面与窄屏/移动视口、console errors、failed requests、字体和资源加载。
- 无法自测时，只能标为 conditional 或 self-reviewed，不得声称 demo-ready 完成。

## 钢人反论

### 反论 1：UI layer map 会不会变成额外文档负担？

回应：要求的是短 map，不是长文档。它服务于实现判断：组件 owner、状态 owner、portal/root、stacking/clipping 和复用范围。没有这个判断，高保真实现容易错层。

### 反论 2：很多设计工具 layer 本身就乱，照着 layer hierarchy 会不会更错？

回应：规则不是照搬设计工具 layer 名，而是把结构化层级翻译成前端 ownership map。设计工具 layer 是证据，不是最终架构。

### 反论 3：E2E 自测会不会让小改动成本过高？

回应：规则允许“最小真实浏览器自测”。已有项目脚本优先；没有脚本时只要求覆盖被改页面和关键路径。无法运行时可降级，但不能声称完整完成。

### 反论 4：mock 阶段跑 E2E 会不会逼 Agent 接真实 API？

回应：不会。E2E 自测只验证当前 mock/demo 范围内的 UI 层级、交互、资源和状态，不扩大到真实 API/BFF。

### 反论 5：z-index 和 portal 本来就是浮层方案，规则会不会误伤？

回应：规则禁止用它们掩盖错误 owner，不禁止合法 overlay、tooltip、drawer、modal 和 anchored popover。合法使用需要记录 root、anchor、stacking 和 clipping 边界。

## 验收标准

- `design-to-frontend-delivery` quick_validate 通过。
- 全量 skills quick_validate 通过。
- README smoke case 覆盖 UI 层级归属错误场景。
- 安装版包含 `UI Layer Ownership Contract`、`End-to-End Self-Test Contract`、`UI layer map`、`E2E self-test path` 和自测证据收尾字段。
