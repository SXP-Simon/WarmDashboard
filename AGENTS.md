# AGENTS.md — AstrBot 报告视觉模板开发守则（暖色仪表盘 Warm Dashboard）

STYLEKIT_STYLE_REFERENCE
style_name: 暖色仪表盘
style_slug: warm-dashboard
style_source: /styles/warm-dashboard

# Hard Prompt

## 什么时候用
当你希望 AI 严格按风格规则生成代码时使用。它是生产界面最稳的默认选择。

## 怎么用
- 把完整提示词复制到 ChatGPT、Claude、Cursor 或其他编码助手。
- 在提示词后追加具体产品、页面或组件需求。
- 生成后按禁止项和交互状态检查，确认没有风格漂移。

请严格遵守以下风格规则并保持一致性，禁止风格漂移。

## 执行要求

- 优先保证风格一致性，其次再做创意延展。
- 遇到冲突时以禁止项为最高优先级。
- 输出前自检：颜色、排版、间距、交互是否仍属于该风格。

## Style Rules

你是一个 Warm Dashboard（暖色仪表盘）设计风格的前端开发专家。

## 绝对禁止

- 禁止使用冷色背景（蓝色、紫色）
- 禁止使用纯黑文字 text-black
- 禁止使用硬边阴影
- 禁止使用高饱和度霓虹色
- 禁止使用粗边框 border-2 及以上

## 必须遵守

- 背景使用暖色调 bg-[#d4a088] 或 bg-[#c9967a]
- 卡片使用奶油白 bg-[#faf8f5] 或 bg-white
- 使用大圆角 rounded-2xl 或 rounded-3xl
- 使用柔和漫射阴影 shadow-xl shadow-black/10
- 图表使用青绿 #4a9d9a 和金黄 #e8b86d 配色
- 文字使用深灰 text-gray-800 或 text-gray-600
- 侧边栏使用半透明白色 bg-white/80 backdrop-blur
- 数据高亮使用点缀色圆形背景

## 核心特征

背景：
- 主背景：bg-[#d4a088] 珊瑚/赤陶色
- 可选变体：bg-[#c9967a] 更深、bg-[#e0b8a4] 更浅

卡片：
- 背景：bg-[#faf8f5] 奶油白 或 bg-white
- 圆角：rounded-2xl 或 rounded-3xl
- 阴影：shadow-xl shadow-black/8（柔和漫射）
- hover：hover:shadow-2xl hover:-translate-y-1

配色系统：
- 青绿（主要强调）：#4a9d9a - 用于主按钮、正向数据
- 金黄（图表主色）：#e8b86d - 用于图表、高亮
- 珊瑚（次要强调）：#c17767 - 用于负向数据、警告
- 灰绿（辅助）：#6b8e8e - 用于次要元素

文字：
- 标题：text-gray-800 font-semibold/bold
- 正文：text-gray-600
- 次要：text-gray-500 text-gray-400
- 暖背景上：text-white

## 布局

侧边栏：
- bg-white/80 backdrop-blur-xl
- 宽度 w-60
- 包含 logo、头像、导航

主区域：
- bg-[#d4a088] 暖色背景
- p-6 md:p-8 lg:p-10
- 统计卡片网格 + 图表卡片

## Animation & Interaction Rules
- Micro-Focus: 作为数据密集的仪表盘，卡片交互绝不能引发剧烈的视觉跳跃。悬停时仅允许极轻微的上浮（`hover:-translate-y-0.5`），并通过增强阴影（`shadow-xl` 变 `shadow-2xl`）来聚焦视线。
- Tinted Diffusion: 抛弃死黑色的阴影。悬停高光操作（如主按钮）时，必须散发出与主色同色系的柔和光晕（如 `hover:shadow-[0_8px_20px_rgba(74,157,154,0.25)]`），维持整体的温暖氛围。
- Data Pulse: 增强数据易读性。当悬停在数据卡片上时，可令内部的关键指标（KPI 数值）快速地微量放大（`group-hover:scale-105`）或切换为强调色（青绿或金黄），帮助用户锁定核心信息。
- Warm Utility: 所有状态过渡需兼顾高效与柔和，推荐使用 `duration-200 ease-out`。

---

# Warm Dashboard (暖色仪表盘) Design System

> 温暖柔和的仪表盘设计风格，采用珊瑚/赤陶色背景、奶油白卡片、柔和阴影，营造舒适专业的数据展示体验。

## 核心理念

Warm Dashboard（暖色仪表盘）是一种温暖、专业的界面设计风格，通过暖色调背景和柔和的卡片设计，让数据展示更加亲和友好。

核心理念：
- 温暖舒适：珊瑚/赤陶色背景传递温暖感
- 清晰层次：奶油白卡片在暖色背景上形成清晰对比
- 柔和触感：大圆角、漫射阴影营造柔软视觉
- 专业可读：深灰文字确保数据可读性
- 点缀色彩：青绿、金黄作为数据高亮和图表色

设计原则：
- 视觉一致性：所有组件必须遵循统一的视觉语言，从色彩到字体到间距保持谐调
- 层次分明：通过颜色深浅、字号大小、留白空间建立清晰的信息层级
- 交互反馈：每个可交互元素都必须有明确的 hover、active、focus 状态反馈
- 响应式适配：设计必须在移动端、平板、桌面端上保持一致的体验
- 无障碍性：确保色彩对比度符合 WCAG 2.1 AA 标准，所有交互元素可键盘访问

---

## Token 字典（精确 Class 映射）

### 边框
```
宽度: border
颜色: border-gray-200/50
圆角: rounded-2xl
```

### 阴影
```
小: shadow-lg shadow-black/5
中: shadow-xl shadow-black/8
大: shadow-2xl shadow-black/10
悬停: hover:shadow-2xl hover:-translate-y-1
聚焦: focus:ring-2 focus:ring-[#4a9d9a]/30
```

### 交互效果
```
悬停位移: （无）
悬停缩放: （无）
悬停透明度: hover:-translate-y-0.5
过渡动画: transition-all duration-200
按下状态: active:scale-[0.98]
```

### 字体
```
标题: font-semibold text-gray-800
正文: text-gray-600
等宽: font-mono text-gray-700
```

### 字号
```
Hero: text-3xl md:text-4xl
H1: text-2xl md:text-3xl
H2: text-xl md:text-2xl
H3: text-lg md:text-xl
正文: text-sm md:text-base
小字: text-xs
```

### 间距
```
Section: py-12 md:py-16
容器: px-6 md:px-8 lg:px-10
卡片: p-5 md:p-6 lg:p-8
小间距: gap-3
中间距: gap-4 md:gap-6
大间距: gap-6 md:gap-10
```

### 颜色角色
```
背景主色: bg-[#d4a088]
背景辅色: bg-[#faf8f5]
背景强调色: bg-[#4a9d9a], bg-[#e8b86d], bg-[#c17767], bg-[#6b8e8e]
正文主色: text-gray-800
正文辅色: text-gray-600
正文弱化色: text-gray-400
按钮主色: bg-[#4a9d9a] text-white
按钮辅色: bg-white text-gray-700
```

---

## [FORBIDDEN] 绝对禁止

以下 class 在本风格中**绝对禁止使用**，生成时必须检查并避免：

### 禁止的 Class
- `bg-blue-500`
- `bg-blue-600`
- `bg-purple-500`
- `bg-purple-600`
- `text-black`
- `rounded-none`
- `rounded-sm`
- `shadow-[0px_0px_0px`
- `border-2`
- `border-4`
- `bg-[#00ffff]`
- `bg-[#ff00ff]`
- `text-[#00ffff]`

### 禁止的模式
- 匹配 `^rounded-none$`
- 匹配 `^rounded-sm$`
- 匹配 `^text-black$`
- 匹配 `^border-[2-4]$`

### 禁止原因
- `rounded-none`: Warm Dashboard uses large rounded corners (rounded-2xl or rounded-3xl)
- `rounded-sm`: Warm Dashboard uses large rounded corners (rounded-2xl or rounded-3xl)
- `text-black`: Warm Dashboard uses text-gray-800 for primary text, not pure black
- `border-2`: Warm Dashboard uses subtle single-pixel borders
- `bg-blue-500`: Warm Dashboard uses warm color palette, avoid cold backgrounds

> WARNING: 如果你的代码中包含以上任何 class，必须立即替换。

---

## [REQUIRED] 必须包含

### 按钮必须包含
```
px-5 py-2.5 md:px-6 md:py-3
rounded-xl
shadow-lg
hover:shadow-xl hover:-translate-y-0.5
transition-all duration-200
font-medium text-sm md:text-base
```

### 卡片必须包含
```
bg-[#faf8f5]
rounded-2xl md:rounded-3xl
shadow-xl shadow-black/8
p-5 md:p-6 lg:p-8
hover:shadow-2xl hover:-translate-y-1
transition-all duration-300
```

### 输入框必须包含
```
w-full px-4 py-3
bg-white
border border-gray-200
rounded-xl
text-gray-800
placeholder:text-gray-400
focus:outline-none focus:ring-2 focus:ring-[#4a9d9a]/30
focus:border-[#4a9d9a]
transition-all duration-200
```

---

## [COMPARE] Warm Dashboard 错误 vs 正确对比

以下错误示例只代表“未经过当前风格适配的通用默认值”，不要把错误示例当成视觉建议。

### 按钮

[WRONG] **错误示例**（通用组件库默认样式，不要直接复制）：
```html
<button class="{GENERIC_LIBRARY_BUTTON_DEFAULT}">
  点击我
</button>
```

[CORRECT] **正确示例**（使用当前风格的 token）：
```html
<button class="px-5 py-2.5 md:px-6 md:py-3 rounded-xl shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200 font-medium text-sm md:text-base bg-[#4a9d9a] text-white">
  点击我
</button>
```

### 卡片

[WRONG] **错误示例**（未经当前风格适配的通用卡片）：
```html
<div class="{GENERIC_LIBRARY_CARD_DEFAULT}">
  <h3>{TITLE}</h3>
</div>
```

[CORRECT] **正确示例**（使用当前风格的 card token）：
```html
<div class="bg-[#faf8f5] rounded-2xl md:rounded-3xl shadow-xl shadow-black/8 p-5 md:p-6 lg:p-8 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 p-5 md:p-6 lg:p-8">
  <h3 class="font-semibold text-gray-800 text-lg md:text-xl">{TITLE}</h3>
</div>
```

### 输入框

[WRONG] **错误示例**（未经当前风格适配的通用输入框）：
```html
<input class="{GENERIC_LIBRARY_INPUT_DEFAULT}" />
```

[CORRECT] **正确示例**（使用当前风格的 input token）：
```html
<input class="w-full px-4 py-3 bg-white border border-gray-200 rounded-xl text-gray-800 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#4a9d9a]/30 focus:border-[#4a9d9a] transition-all duration-200" placeholder="{PLACEHOLDER}" />
```

---

## [TEMPLATES] Warm Dashboard 页面骨架模板

以下骨架只使用当前风格的 token。替换 `{PLACEHOLDER}` 时，不要移除或替换这些 token：

### 导航栏骨架
```html
<nav class="bg-[#d4a088] text-gray-800 border border-gray-200/50 px-6 md:px-8 lg:px-10">
  <div class="flex items-center justify-between max-w-6xl mx-auto gap-4 md:gap-6">
    <a href="/" class="font-semibold text-gray-800 text-lg md:text-xl">
      {LOGO_TEXT}
    </a>
    <div class="flex gap-4 md:gap-6 text-gray-600 text-xs">
      {NAV_LINKS}
    </div>
  </div>
</nav>
```

### Hero 区块骨架
```html
<section class="bg-[#4a9d9a] text-gray-800 py-12 md:py-16 px-6 md:px-8 lg:px-10">
  <div class="max-w-4xl mx-auto">
    <h1 class="font-semibold text-gray-800 text-3xl md:text-4xl">
      {HEADLINE}
    </h1>
    <p class="text-gray-600 text-sm md:text-base max-w-xl">
      {SUBHEADLINE}
    </p>
    <button class="px-5 py-2.5 md:px-6 md:py-3 rounded-xl shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200 font-medium text-sm md:text-base bg-[#4a9d9a] text-white">
      {CTA_TEXT}
    </button>
  </div>
</section>
```

### 卡片网格骨架
```html
<section class="bg-[#d4a088] text-gray-800 py-12 md:py-16 px-6 md:px-8 lg:px-10">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-semibold text-gray-800 text-xl md:text-2xl">{SECTION_TITLE}</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
      <!-- Card template - repeat for each card -->
      <div class="bg-[#faf8f5] rounded-2xl md:rounded-3xl shadow-xl shadow-black/8 p-5 md:p-6 lg:p-8 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 p-5 md:p-6 lg:p-8">
        <h3 class="font-semibold text-gray-800 text-lg md:text-xl">{CARD_TITLE}</h3>
        <p class="text-gray-600 text-sm md:text-base text-gray-400">{CARD_DESCRIPTION}</p>
      </div>
    </div>
  </div>
</section>
```

### 表单输入骨架
```html
<input class="w-full px-4 py-3 bg-white border border-gray-200 rounded-xl text-gray-800 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#4a9d9a]/30 focus:border-[#4a9d9a] transition-all duration-200" placeholder="{PLACEHOLDER}" />
```

### 页脚骨架
```html
<footer class="bg-[#faf8f5] text-gray-600 py-12 md:py-16 px-6 md:px-8 lg:px-10">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-10">
      <div>
        <span class="font-semibold text-gray-800 text-lg md:text-xl">{LOGO_TEXT}</span>
        <p class="text-gray-600 text-xs">{TAGLINE}</p>
      </div>
      <div>
        <h4 class="font-semibold text-gray-800 text-lg md:text-xl">{COLUMN_TITLE}</h4>
        <ul class="text-gray-600 text-xs">
          {FOOTER_LINKS}
        </ul>
      </div>
    </div>
  </div>
</footer>
```

---

## [CHECKLIST] Warm Dashboard 生成后自检清单

**输出代码前，逐项验证当前风格的 token 和规则。如有违反，先修正再交付：**

### Token 检查
- [ ] 按钮包含： `px-5 py-2.5 md:px-6 md:py-3 rounded-xl shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200 font-medium text-sm md:text-base`
- [ ] 卡片包含： `bg-[#faf8f5] rounded-2xl md:rounded-3xl shadow-xl shadow-black/8 p-5 md:p-6 lg:p-8 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300`
- [ ] 输入框包含： `w-full px-4 py-3 bg-white border border-gray-200 rounded-xl text-gray-800 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-[#4a9d9a]/30 focus:border-[#4a9d9a] transition-all duration-200`

### 禁止项检查
- [ ] 没有使用 `bg-blue-500`
- [ ] 没有使用 `bg-blue-600`
- [ ] 没有使用 `bg-purple-500`
- [ ] 没有使用 `bg-purple-600`
- [ ] 没有使用 `text-black`
- [ ] 没有使用 `rounded-none`
- [ ] 没有使用 `rounded-sm`
- [ ] 没有使用 `shadow-[0px_0px_0px`

### 风格规则检查
- [ ] 背景使用暖色调 bg-[#d4a088] 或 bg-[#c9967a]
- [ ] 卡片使用奶油白 bg-[#faf8f5] 或 bg-white
- [ ] 使用大圆角 rounded-2xl 或 rounded-3xl
- [ ] 使用柔和漫射阴影 shadow-xl shadow-black/10
- [ ] 图表使用青绿 #4a9d9a 和金黄 #e8b86d 配色

### 风格漂移检查
- [ ] 没有违反：禁止使用冷色背景（蓝色、紫色）
- [ ] 没有违反：禁止使用纯黑文字 text-black
- [ ] 没有违反：禁止使用硬边阴影
- [ ] 没有违反：禁止使用高饱和度霓虹色
- [ ] 没有违反：禁止使用粗边框 border-2 及以上

### 通用交付检查
- [ ] 响应式布局在手机、平板和桌面下稳定，没有横向溢出
- [ ] 所有交互元素有清晰焦点、可访问名称和 reduced-motion 方案
- [ ] 文本对比度达到 WCAG AA，且没有用颜色单独传递状态
- [ ] 结果仍然能够一眼识别为 Warm Dashboard

---

## [EXAMPLES] 示例 Prompt

### 1. 社交媒体数据仪表盘

展示粉丝、互动、增长等数据

```
用 Warm Dashboard 风格创建一个社交媒体分析仪表盘，要求：

## 布局
- 左侧：半透明白色侧边栏 bg-white/80 backdrop-blur-xl
- 右侧：珊瑚色主区域 bg-[#d4a088]

## 侧边栏
- Logo + 品牌名
- 用户头像（圆形，珊瑚色边框）
- 导航菜单：Dashboard、Insights、Reports、Comments、Channels
- 当前页高亮：bg-[#faf8f5] + 左侧小圆点

## 主区域
- 顶部：标题 + 通知/设置图标
- 统计卡片行（3列）：Views、Followers、Reposts
- 活动图表卡片：折线图，金黄色 #e8b86d
- Top Performers 列表
- 底部渠道统计条

## 数据可视化
- 正向数据：text-[#4a9d9a]
- 负向数据：text-[#c17767]
- 图表主色：#e8b86d
```

### 2. 项目管理仪表盘

任务进度、团队成员、截止日期

```
用 Warm Dashboard 风格创建一个项目管理仪表盘，要求：

## 背景
- 主区域：bg-[#d4a088]
- 卡片：bg-[#faf8f5] rounded-3xl shadow-xl

## 组件
1. 项目概览卡片：进度环形图、完成百分比
2. 任务列表：复选框、优先级标签、截止日期
3. 团队成员：头像堆叠、在线状态
4. 时间线：垂直时间轴、里程碑节点

## 配色
- 完成状态：#4a9d9a 青绿
- 进行中：#e8b86d 金黄
- 延期：#c17767 珊瑚
- 未开始：#9ca3af 灰色
```

### 3. 财务数据仪表盘

收入支出、趋势图表、预算对比

```
用 Warm Dashboard 风格创建一个个人财务仪表盘，要求：

## 布局
- 珊瑚色背景 bg-[#d4a088]
- 奶油白卡片 bg-[#faf8f5]

## 数据卡片
1. 总资产卡片：大数字、增长趋势
2. 收入/支出对比：柱状图
3. 分类饼图：餐饮、交通、娱乐等
4. 近期交易列表：图标、金额、日期

## 配色规则
- 收入/正向：#4a9d9a
- 支出/负向：#c17767
- 图表填充：#e8b86d
- 次要数据：#6b8e8e
```

## 绝对禁止（匹配即拒绝）

以下模式一旦出现，视为风格违规——不找借口，直接重写。

- 使用冷色背景（蓝色、紫色）
- 使用纯黑文字 text-black
- 使用硬边阴影
- 使用高饱和度霓虹色
- 使用粗边框 border-2 及以上

## 自检清单（交付前逐条确认）

如果任何一条不通过，说明风格漂移了——修改后再交付。

- [ ] 没有紫色到蓝色的渐变
- [ ] 没有使用 Inter / Roboto / Geist 等过度使用的字体
- [ ] 没有嵌套卡片（卡片里面套卡片）
- [ ] 没有在彩色背景上放灰色文字
- [ ] 正文对比度满足 WCAG AA（≥4.5:1）
- [ ] 没有 bounce / elastic 缓动曲线
- [ ] 动效有 prefers-reduced-motion 备选方案
- [ ] 正文行宽不超过 65-75 个字符
- [ ] 没有单侧粗边框装饰（border-left/right accent stripe）
- [ ] 没有渐变文字（background-clip: text）
- [ ] 没有把玻璃态（glassmorphism）当作默认风格
- [ ] 没有 tiny uppercase tracked eyebrow 放在每个 section 标题上面
- [ ] 禁止使用冷色背景（蓝色、紫色）
- [ ] 禁止使用纯黑文字 text-black
- [ ] 禁止使用硬边阴影
- [ ] 禁止使用高饱和度霓虹色
- [ ] 禁止使用粗边框 border-2 及以上

---

# AstrBot 插件运行与渲染规则

1. **模板结构**：本仓库为外部模板仓库，安装后位于插件数据目录的 `templates/gda_warm_dashboard/` 下。
2. **必需文件**：`image_template.html`, `html_template.html`, `topic_item.html`, `user_title_item.html`, `quote_item.html`, `activity_chart.html`, `chat_quality_item.html`, `template.json`, `preview.jpg`。
3. **资源内联要求**：渲染通过 Headless T2I，HTML 中所有资源必须为内联 SVG、Base64 或有效公网 CDN 绝对路径。
4. **安全转义**：`topic.detail` 与 `quote.reason` 包含插件预生成的安全富文本胶囊，必须使用 `| safe`。
