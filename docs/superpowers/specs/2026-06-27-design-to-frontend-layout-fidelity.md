# design-to-frontend-delivery 专业布局保真优化

## 背景

用户反馈：当用户说“1:1 还原设计稿”时，Agent 容易把这句话理解成按设计稿坐标复刻，从而用 `position:absolute`、`left/top`、固定像素宽高或截图叠层驱动主布局区域和重复内容。短期看起来接近设计图，但可维护性、响应式、内容伸缩和组件复用都很差。

用户真正需要的是专业前端设计还原：尽量保持设计稿的间距、文字、对齐、颜色、层级、状态和交互一致，同时用可维护的布局结构实现。

## RED 压力场景

```text
用户说：“请 1:1 还原这个 Figma 页面，越像越好，明天要演示。”
设计稿是一个普通业务页面：顶部筛选、卡片列表、右侧信息栏、弹窗入口。
Agent 为了快，用一个相对定位容器包住页面，再给每个区块写 position:absolute、left/top、固定宽高。
1440 截图接近，但 1280/移动端溢出，文案变长后重叠，后续复用组件困难。
```

失败模式：

- 把“1:1 / pixel-perfect / 像设计稿”误读成坐标复刻。
- 把设计工具 canvas 坐标当作 CSS 布局源，而不是把 auto-layout、constraints、spacing、tokens 翻译成前端布局。
- 只追求单一截图相似，忽略响应式、语义结构、组件化和内容伸缩。
- 没有在 Gate 2 审计绝对定位是否属于合理例外。

说明：本轮未派生子代理做真实 baseline 测试；该 RED 来自用户明确反馈的失败模式，作为本次规则修复的压力场景。

## 设计变更

- 在 `SKILL.md` 增加 `Layout Fidelity Contract`，明确高保真是视觉关系目标，不是复制坐标。
- 在 `source-priority.md` 增加“保留设计意图而非 raw canvas coordinates”的规则，并把 auto-layout/constraints/grid/tokens 到 Flex/Grid/flow 的翻译列为允许工程适配。
- 在 `convert-and-polish.md` 增加 `Layout-fidelity-first 布局策略`，要求结构映射后先定布局策略，再写样式。
- 在 `polish-existing-project.md` 增加现有布局健康度与绝对定位审计，避免旧工程在“继续精修”时继续沿用坐标式布局。
- 在 `delivery-checklists.md` 增加布局层、Gate 1 高保真口径确认、Gate 2 布局策略与绝对定位审计、Gate 3 视觉关系验收；绝对定位审计明确主布局区域、重复卡片/行、响应式列、表单、仪表盘和内容流不得由 absolute/fixed 坐标驱动。
- 在 README smoke case 中加入“1:1 还原设计稿”必须走专业布局保真，不得大量 absolute 坐标复刻。

## 钢人反论

### 反论 1：有些设计确实需要绝对定位，否则做不出效果。

回应：规则没有禁用绝对定位。浮层、tooltip、badge、floating action、装饰叠层、canvas/game/diagram、稳定容器内的小型锚定元素仍允许；禁止的是普通页面布局大量坐标复刻。需要例外时必须记录边界和响应式风险。

### 反论 2：设计工具提供 x/y 坐标，为什么不能用？

回应：x/y 是设计画布上的当前快照，不是 Web 布局契约。Web 要面对字体渲染差异、内容长度、断点、滚动、缩放和动态状态。专业还原应从 auto-layout、constraints、spacing、tokens、grid 和组件语义推导 Flex/Grid/flow。

### 反论 3：禁止坐标复刻会降低视觉相似度。

回应：短期单截图可能会慢一点，但长期能稳定保持间距、对齐、字体层级、颜色和状态关系；坐标复刻在另一个宽度或内容变化下很快失真。验收目标调整为视觉关系高保真，而不是单点像素重叠。

### 反论 4：skill 规则太多，Agent 可能读不到。

回应：关键规则放在主 `SKILL.md` 顶部的 `Layout Fidelity Contract` 和 `agents/openai.yaml` 默认 prompt，执行细节放到 references 与 checklist。README 加 smoke case，用于安装后人工/自动检验。

## 验收标准

- `design-to-frontend-delivery` quick_validate 通过。
- 全量 5 个 skills quick_validate 通过。
- 本地 `npx skills add . --list --full-depth` 能发现该 skill，并 description 不破坏安装发现。
- 全局安装版包含 `Layout Fidelity Contract`、`Layout-fidelity-first 布局策略` 和 `绝对定位审计`。
