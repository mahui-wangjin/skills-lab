# design-to-frontend-delivery 工程目录边界优化

## 背景

用户反馈：设计图还原时，Agent 容易只关注页面是否看起来接近设计稿，却缺少工程目录思维，把页面入口、组件、mock 数据、展示选择器、样式、资源和测试堆进同一个文件夹或同一个大文件。

用户期望：前端开发应默认知道目标框架和当前工程有目录与职责约定。设计落地不需要每次由用户提醒“mock、组件、业务划分要分目录”。

## RED 压力场景

```text
用户要求按设计稿做一个页面。
Agent 直接在一个 page 文件或随机新建的 feature 文件夹里堆：
- 大段 JSX 和多个 UI 区块
- mock 数组和展示选择器
- 本地状态、格式化函数和样式
- assets 引用和测试逻辑

最终页面能跑，但下一次接真实数据、复用组件、补状态或写测试时，必须继续翻同一个大文件或同一坨目录。
```

失败模式：

- 把设计还原误解成单文件静态稿迁移。
- 不先识别当前工程的路由、feature、components、fixtures、styles/assets、tests 约定。
- 随机新建 `components`、`mock`、`data`、`utils` 目录，破坏已有项目结构。
- 把页面入口、展示组件、fixtures、展示选择器、样式和测试混成一个变化轴。

说明：本轮 RED 来自用户明确反馈和当前 skill 缺口，未额外启动子代理 baseline。

## 设计变更

- 在 `SKILL.md` 增加 `Project Structure Contract`。
- 在 `convert-and-polish.md` 增加工程目录与职责边界步骤。
- 在 `polish-existing-project.md` 增加工程目录健康度审计和最小闭环扩围触发条件。
- 在 `delivery-checklists.md` 增加 Gate 1/Gate 2/Gate 3 的工程结构检查项和收尾输出字段。
- 在 README smoke case 中加入“按设计稿做 React/Vue 页面”的目录组织判断场景。

## 边界口径

默认先做：

- 识别目标框架和当前工程约定：route/page、feature/module、components、mock/fixtures、selectors/formatters、styles/tokens、assets、tests/stories。
- 页面入口只做路由接入和页面级编排。
- 大块 UI 放到 feature-private 组件；真正跨页面复用的组件才进入 shared。
- mock/fixture 数据放到已有夹具位置或 feature-local data/fixtures。
- 薄展示选择器、格式化和 key 校验放到 feature-local model/selectors/formatters 等现有命名体系。
- styles、tokens、assets、tests/stories 按目标框架和项目惯例归位。

禁止默认做：

- 随机新建通用 `components`、`mock`、`data`、`utils` 作为倾倒目录。
- 把整页 JSX、mock、展示选择器、样式和测试全部塞进一个文件或一个目录。
- 在已有工程约定清晰时，用另一个框架或模板的目录法覆盖本项目。

例外：

- 一次性静态 HTML 且没有宿主工程时，可以保持自包含文件；但仍应在文件内部区分数据、渲染、样式和交互，并不得把这种结构当作真实工程默认方案。

## 钢人反论

### 反论 1：目录规则会不会导致过度拆分？

回应：规则按职责和变化轴拆分，不按目录洁癖拆分。小页面可以保留少量 feature-local 文件；禁止的是把明显不同变化原因的内容混堆。

### 反论 2：不同框架目录最佳实践不同，写死目录名会误导。

回应：规则不写死 React/Vue/Next/Nuxt 等目录名，只要求先识别当前工程和目标框架约定。没有现成约定时，才按框架官方或事实标准选择最小结构。

### 反论 3：有些设计任务只是静态 demo，分目录会慢。

回应：一次性静态 HTML 可以自包含；但如果目标是已有工程或框架应用，目录边界是交付质量的一部分。页面能跑但后续无法接数据、复用和测试，不算专业交付。

### 反论 4：shared 目录能复用，为什么不都放 shared？

回应：shared 只放稳定、跨页面复用的组件或工具。feature-private 组件、fixtures 和展示选择器先贴近功能，避免过早抽象和全局污染。

## 验收标准

- `design-to-frontend-delivery` quick_validate 通过。
- 全量 5 个 skills quick_validate 通过。
- README smoke case 覆盖工程目录组织场景。
- 全局安装版包含 `Project Structure Contract`、工程目录边界和收尾输出的工程结构字段。
