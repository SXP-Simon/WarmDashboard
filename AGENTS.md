# AGENTS.md — AstrBot 报告视觉模板开发守则

本仓库支持四套核心设计风格规范：
1. **日系清新风 (Japanese Fresh)** (`gda_japanese_fresh`)
2. **暖色仪表盘 (Warm Dashboard)** (`gda_warm_dashboard`)
3. **拼贴艺术风 (Collage Art)** (`gda_collage_art`)
4. **新艺术运动风 (Art Nouveau)** (gda_art_nouveau)

---

# 模块一：日系清新风 (Japanese Fresh) 规范

STYLEKIT_STYLE_REFERENCE
style_name: 日系清新风
style_slug: japanese-fresh
style_source: /styles/japanese-fresh

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

You are a Japanese Fresh design style frontend development expert. All generated code must strictly follow these constraints:

## 绝对禁止

- Never use bold or heavy font weights (font-bold, font-semibold)
- Never use uppercase text -- it is too aggressive for this aesthetic
- Never use border-2 or thicker -- only hairline borders
- Never use visible shadows (shadow-lg/xl) -- elements float without weight
- Never use dark or black backgrounds
- Never use sharp corners (rounded-none) -- always gentle rounded-lg/xl
- Never crowd sections together -- maintain extreme breathing room
- Never use fast, abrupt interaction transitions under 200ms

## 必须遵守

- Use extreme whitespace (py-32, py-40) between sections -- Ma is the primary design tool
- Use only hairline borders (border with opacity-30, never border-2)
- Include one delicate botanical SVG line drawing per major section
- Use font-extralight/font-light exclusively for all text
- Keep inputs as bottom-line only with floating labels
- Use warm neutral border color #d4d4cf instead of harsh gray
- Apply asymmetric element placement for wabi-sabi character
- Use transition duration-500 for slow, meditative interactions
- Use weightless hover feedback (subtle lift + transparent tint) instead of heavy depth

## Color Palette

Primary:
- Sky Blue: #64b5f6
- Rice White: #fafaf8
- Mint Green: #98d8c8
- Gentle Pink: #ffb7c5
- Powder Blue: #b8d4e3
- Text: #4a5568
- Secondary text: #7a8a9e
- Muted: #b0b8c4
- Border: #d4d4cf

## Unique Elements

- Ma-based extreme whitespace (py-32+ sections)
- Hairline 0.5px borders at 30% opacity
- Botanical line-drawing SVG accents (one per section)
- Bottom-line only input fields with floating labels
- Linen/paper texture background pattern

## Animation & Interaction Rules

- Weightless Float: hover 仅允许极轻上浮（约 0.5px），避免重阴影和大位移。
- Airy Transitions: 颜色变化采用 duration-500 + ease-in-out，像晨雾中缓慢显现。
- Subtle Focus: 表单 focus 只调整发丝级边框颜色，不使用粗 ring 或强 glow。
- Tactile Click: active 态优先微调透明度和背景层，不使用明显缩放。

---

# Japanese Fresh (日系清新风) Design System

> 以Ma (间) 留白哲学、侘寂美学和极致呼吸感为核心，通过发丝级边框、植物线描装饰和极简温暖中性色，营造沉静治愈的设计体验。

## 核心理念

Japanese Fresh embodies Ma (space between) and wabi-sabi (beauty in imperfection). Design is not about what you add, but what you allow to breathe.

Core principles:
- Ma (間): Intentional, generous whitespace is the primary design element. Sections use py-32+ to create profound breathing room between content
- Wabi-sabi: Embrace subtle imperfection -- asymmetric layouts, slightly off-center elements, and organic rather than rigid alignment
- Hairline Borders: All borders are 0.5-1px maximum, using warm neutral colors like #d4d4cf at 30-40% opacity
- Natural Textures: Subtle linen/paper grain texture backgrounds reference natural materials (washi paper, unbleached cotton)
- Botanical Accents: Single delicate line-drawn botanical SVG elements per section -- one branch, one leaf, never crowded
- Bottom-line Inputs: Inputs use only a bottom border line, floating labels, no surrounding frame
- No Shadows: Forms exist without shadow; they float in whitespace by their own presence

---

## Token 字典（精确 Class 映射）

### 边框
```
宽度: border
颜色: border-[#d4d4cf]
圆角: rounded-xl
```

### 阴影
```
小: shadow-none
中: shadow-[0_1px_3px_rgba(0,0,0,0.03)]
大: shadow-[0_2px_6px_rgba(0,0,0,0.04)]
悬停: hover:shadow-[0_2px_8px_rgba(0,0,0,0.05)]
聚焦: focus:shadow-[0_0_0_2px_rgba(100,181,246,0.08)]
```

### 交互效果
```
悬停位移: hover:-translate-y-px
悬停缩放: hover:brightness-[1.02]
悬停透明度: （无）
过渡动画: transition-all duration-500 ease-in-out
按下状态: active:scale-[0.99]
```

### 字体
```
标题: font-sans font-extralight text-[#4a5568] tracking-wide
正文: font-sans font-light text-[#6b7280] leading-relaxed
等宽: font-mono
```

### 字号
```
Hero: text-3xl md:text-5xl lg:text-6xl
H1: text-2xl md:text-4xl
H2: text-xl md:text-2xl
H3: text-base md:text-lg
正文: text-sm md:text-base
小字: text-xs md:text-sm
```

### 间距
```
Section: py-32 md:py-32 lg:py-40
容器: px-8 md:px-12 lg:px-20
卡片: p-8 md:p-10
小间距: gap-4 md:gap-6
中间距: gap-8 md:gap-12
大间距: gap-12 md:gap-20
```

### 颜色角色
```
背景主色: bg-[#fafaf8]
背景辅色: bg-white
背景强调色: bg-[#64b5f6], bg-[#98d8c8], bg-[#ffb7c5], bg-[#b8d4e3]
正文主色: text-[#4a5568]
正文辅色: text-[#7a8a9e]
正文弱化色: text-[#b0b8c4]
按钮主色: bg-[#64b5f6]/90 text-white
按钮辅色: bg-white text-[#7a8a9e] border-[#d4d4cf]
```

---

## [FORBIDDEN] 绝对禁止

以下 class 在本风格中**绝对禁止使用**，生成时必须检查并避免：

### 禁止的 Class
- `rounded-none`
- `rounded-sm`
- `border-2`
- `border-4`
- `font-bold`
- `font-black`
- `font-extrabold`
- `bg-[#0f0f1a]`
- `bg-black`
- `bg-[#1a1a1a]`
- `shadow-[0_0_`
- `text-[#ff006e]`
- `uppercase`
- `shadow-lg`
- `shadow-xl`
- `shadow-2xl`

### 禁止的模式
- 匹配 `^rounded-(?:none|sm)$`
- 匹配 `^border-[2-9]$`
- 匹配 `^font-(?:bold|black|extrabold|semibold)$`
- 匹配 `^bg-(?:black|\[#0)`
- 匹配 `^uppercase$`
- 匹配 `^shadow-(?:lg|xl|2xl)$`

---

## [REQUIRED] 必须包含

### 按钮必须包含
```
rounded-lg
font-sans font-light
border border-[#d4d4cf]/40
transition-all duration-500 ease-in-out
```

### 卡片必须包含
```
bg-white
rounded-xl
border border-[#d4d4cf]/30
```

### 输入框必须包含
```
border-b border-[#d4d4cf]
bg-transparent
font-sans font-light
focus:outline-none
transition-all duration-500 ease-in-out
```

```html
<div class="relative">
  <input
    id="field"
    type="text"
    placeholder=" "
    class="peer w-full border-b border-[#d4d4cf] bg-transparent px-0 py-3 font-sans font-light text-[#4a5568] transition-all duration-500 ease-in-out focus:border-[#64b5f6]/50 focus:outline-none"
  />
  <label
    for="field"
    class="pointer-events-none absolute left-0 -top-4 font-sans font-light text-xs text-[#7a8a9e] transition-all duration-500 ease-in-out peer-placeholder-shown:top-3 peer-placeholder-shown:text-base peer-focus:-top-4 peer-focus:text-xs peer-focus:text-[#64b5f6]"
  >
    标签
  </label>
</div>
```

---

# 模块二：暖色仪表盘 (Warm Dashboard) 规范

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

---

# 模块三：拼贴艺术风 (Collage Art) 规范

STYLEKIT_STYLE_REFERENCE
style_name: 拼贴艺术风
style_slug: collage-art
style_source: /styles/collage-art

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

你是一位专精于拼贴艺术风格（Collage Art）的前端开发专家。生成的所有代码都必须严格遵循以下规范：

## 绝对禁止

- 禁止使用平滑渐变（bg-gradient-to-*）
- 禁止使用柔和圆角（rounded-lg 以上）
- 禁止使用毛玻璃效果（backdrop-blur）
- 禁止使用统一整齐的对齐方式
- 禁止对有 hover/group-hover Tailwind 变换的元素使用 style={{ transform }} 内联属性（会导致 transform 冲突）

## 必须遵守

- 使用混合字体（衬线 font-serif + 无衬线 font-sans + 等宽 font-mono 交替）
- 元素使用 Tailwind 任意值旋转 rotate-[Ndeg] 而非内联 style transform（避免与 hover 冲突）
- 使用硬偏移阴影 shadow-[Npx_Npx_0px_color] 营造层叠深度
- 添加 washi tape 装饰：repeating-linear-gradient 条纹色块
- 使用 polygon clip-path 创造撕纸边缘效果
- 保持陈旧纸张色 bg-[#f5f0e8] 作为底色
- 大胆使用对比色块（红/蓝/黄/紫）
- 使用实线和虚线边框模拟剪切痕迹
- hover 时纸片上浮 -translate-y-2 + 旋转变化 + 阴影扩张，active 时阴影骤减模拟按压
- 使用 group + group-hover:* 让胶带装饰响应卡片悬停，产生视差效果

## 配色方案

主色：
- 深炭灰：#2d2d2d
- 陈旧纸张：#f5f0e8
- 剪切红：#e74c3c
- 杂志蓝：#3498db
- 粘贴黄：#f39c12
- 碎片紫：#9b59b6

## 动效与交互规则

- 纸片掀起（Paper Lift）：hover 时元素应带有被实际掀起的物理感。使用 hover:scale-[1.02]，配合旋转角度变化（例如从 rotate-[1.5deg] 变为 group-hover:-rotate-[1deg]）和阴影扩张（shadow-[5px_5px] → shadow-[12px_12px]）。这模拟了一张纸片被从桌面上捏起的效果。
- 胶带视差（Tape Parallax）：卡片上的和纸胶带装饰应与卡片本身产生略微不同的反应。将整个组件包裹在 group 容器中：胶带 div 使用 group-hover:-translate-y-1 group-hover:rotate-[6deg]，卡片则使用 group-hover:-translate-y-2 group-hover:-rotate-[1deg]。胶带看起来是独立移动的，从而强化多层纸片叠加的物理错觉。
- 按压桌面（Desk Press）：:active 状态下阴影必须骤然收缩（shadow-[12px_12px] → shadow-[2px_2px]），元素同时略微下移（active:translate-y-1），模拟把纸片牢牢按压到软木板上的动作。
- 干脆缓动（Snappy Easing）：所有纸片交互都使用 duration-200 ease-out 或 duration-300 ease-out。纸张很轻，动作要干净利落。
- 变换规则（Transform Rules）：初始旋转必须始终使用 Tailwind 的 rotate-[Xdeg] 任意值类。凡是同时使用了 Tailwind hover/group-hover transform 的元素，禁止再用 style={{ transform: "rotate(Xdeg)" }}——两者会产生冲突。

## 独特元素（拼贴专属）

1. 随机旋转：rotate-[0.7deg]、-rotate-[1.5deg]、rotate-[2deg] 等（使用 Tailwind 任意值，而非内联样式）
2. 和纸胶带：repeating-linear-gradient(90deg, color 0px, color 3px, rgba(255,255,255,0.3) 3px, rgba(255,255,255,0.3) 6px) 条纹，置于响应 group-hover 的 div 中
3. 混搭字体：标题、标签、正文交替使用 font-serif、font-sans、font-mono
4. 撕纸边缘：使用带不规则锯齿点的 polygon clip-path
5. 虚线边框：用 border-dashed 表现邮戳/剪切线效果

## 自检清单

生成代码后请确认：
1. 所有初始旋转都使用 rotate-[Xdeg] 这个 Tailwind 类，而非内联样式（当存在 hover transform 时）
2. 可交互卡片已包裹在 group 容器中，以实现胶带视差
3. hover 状态：scale-105 + 旋转变化 + 阴影扩张
4. active 状态：阴影收缩 + 轻微下移
5. 时长为 200-300ms ease-out

---

# Collage Art (拼贴艺术风) Design System

> 杂志拼贴和混合材料美学，纸片剪切、多层叠加、撕纸边缘和混搭字体，营造充满创意和手工感的视觉冲击。

## 核心理念

拼贴艺术风格源于达达主义和波普艺术的混合媒材传统，强调不同材料、字体和图像的碰撞与融合。

核心理念：
- 随机旋转：每个元素都有细微的 rotate transform（0.5-2deg），模拟手工粘贴的不精确感
- 和纸胶带装饰：使用 repeating-linear-gradient 条纹伪元素模拟半透明和纸胶带
- 混搭字体：同一页面交替使用 font-serif、font-sans、font-mono 营造杂志剪报感
- 撕纸边缘：polygon clip-path 创造不规则的锯齿状撕纸边缘
- 硬偏移阴影：shadow-[Npx_Npx_0px] 纯色偏移阴影创造纸片层叠的物理深度
- 纸张物理感：hover 时纸片被掀起（scale-105 + 旋转微调），active 时被按压在桌面（阴影骤减）

---

## Token 字典（精确 Class 映射）

### 边框
```
宽度: border-2
颜色: border-[#2d2d2d]
圆角: rounded-none
```

### 阴影
```
小: shadow-[3px_3px_0px_#2d2d2d]
中: shadow-[5px_5px_0px_#2d2d2d]
大: shadow-[7px_7px_0px_#2d2d2d]
悬停: hover:shadow-[7px_7px_0px_#2d2d2d]
聚焦: focus:shadow-[3px_3px_0px_#2d2d2d]
```

### 交互效果
```
悬停位移: hover:translate-x-[1px] hover:translate-y-[1px]
悬停缩放: （无）
悬停透明度: （无）
过渡动画: transition-all duration-200 ease-in-out
按下状态: active:translate-x-[3px] active:translate-y-[3px] active:shadow-none
```

### 字体
```
标题: font-serif font-bold uppercase tracking-wider
正文: font-sans
等宽: font-mono text-xs uppercase tracking-[0.2em]
```

### 字号
```
Hero: text-5xl md:text-7xl lg:text-8xl
H1: text-3xl md:text-5xl
H2: text-2xl md:text-4xl
H3: text-xl md:text-2xl
正文: text-sm md:text-base
小字: text-xs md:text-sm
```

### 间距
```
Section: py-12 md:py-20 lg:py-28
容器: px-4 md:px-8 lg:px-12
卡片: p-5 md:p-8
小间距: gap-3 md:gap-4
中间距: gap-4 md:gap-6
大间距: gap-6 md:gap-10
```

### 颜色角色
```
背景主色: bg-[#f5f0e8]
背景辅色: bg-[#ebe4d8]
背景强调色: bg-[#e74c3c], bg-[#3498db], bg-[#f39c12], bg-[#9b59b6]
正文主色: text-[#2d2d2d]
正文辅色: text-[#e74c3c]
正文弱化色: text-[#2d2d2d]/50
按钮主色: bg-[#e74c3c] text-white border-2 border-[#2d2d2d] shadow-[4px_4px_0px_#2d2d2d]
按钮辅色: bg-[#3498db] text-white border-2 border-[#2d2d2d] shadow-[4px_4px_0px_#2d2d2d]
```

---

## [FORBIDDEN] 绝对禁止

以下 class 在本风格中**绝对禁止使用**，生成时必须检查并避免：

### 禁止的 Class
- `rounded-lg`
- `rounded-xl`
- `rounded-2xl`
- `rounded-3xl`
- `rounded-full`
- `bg-gradient-to-r`
- `bg-gradient-to-b`
- `bg-gradient-to-br`
- `backdrop-blur`
- `backdrop-blur-sm`
- `backdrop-blur-md`
- `shadow-[0_`

### 禁止的模式
- 匹配 `^rounded-(?:lg|xl|2xl|3xl|full)$`
- 匹配 `^bg-gradient-`
- 匹配 `^backdrop-blur`
- 匹配 `^shadow-\[0_`

### 禁止原因
- `rounded-full`: Collage Art uses sharp corners (rounded-sm/rounded-none) for cut-paper feel
- `rounded-lg`: Collage Art uses rounded-sm or rounded-none, never soft corners
- `bg-gradient-to-r`: Collage Art uses flat solid color blocks, not smooth gradients
- `backdrop-blur`: Collage Art is opaque and layered paper, not translucent glass
- `shadow-[0_`: Collage Art uses hard offset shadows (Npx_Npx_0px), not soft blur shadows

> WARNING: 如果你的代码中包含以上任何 class，必须立即替换。

---

## [REQUIRED] 必须包含

### 按钮必须包含
```
rounded-sm
font-bold uppercase
border-2 border-[#2d2d2d]
transition-all duration-200 ease-in-out
```

### 卡片必须包含
```
rounded-none
bg-[#f5f0e8]
border-2 border-[#2d2d2d]
```

### 输入框必须包含
```
rounded-none
border-2 border-[#2d2d2d]
bg-[#f5f0e8]
focus:outline-none
```

---

## [COMPARE] Collage Art 错误 vs 正确对比

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
<button class="rounded-sm font-bold uppercase border-2 border-[#2d2d2d] transition-all duration-200 ease-in-out bg-[#e74c3c] text-white border-2 border-[#2d2d2d] shadow-[4px_4px_0px_#2d2d2d]">
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
<div class="rounded-none bg-[#f5f0e8] border-2 border-[#2d2d2d] p-5 md:p-8">
  <h3 class="font-serif font-bold uppercase tracking-wider text-xl md:text-2xl">{TITLE}</h3>
</div>
```

### 输入框

[WRONG] **错误示例**（未经当前风格适配的通用输入框）：
```html
<input class="{GENERIC_LIBRARY_INPUT_DEFAULT}" />
```

[CORRECT] **正确示例**（使用当前风格的 input token）：
```html
<input class="rounded-none border-2 border-[#2d2d2d] bg-[#f5f0e8] focus:outline-none" placeholder="{PLACEHOLDER}" />
```

---

## [TEMPLATES] Collage Art 页面骨架模板

以下骨架只使用当前风格的 token。替换 `{PLACEHOLDER}` 时，不要移除或替换这些 token：

### 导航栏骨架
```html
<nav class="bg-[#f5f0e8] text-[#2d2d2d] border-2 border-[#2d2d2d] px-4 md:px-8 lg:px-12">
  <div class="flex items-center justify-between max-w-6xl mx-auto gap-4 md:gap-6">
    <a href="/" class="font-serif font-bold uppercase tracking-wider text-xl md:text-2xl">
      {LOGO_TEXT}
    </a>
    <div class="flex gap-4 md:gap-6 font-sans text-xs md:text-sm">
      {NAV_LINKS}
    </div>
  </div>
</nav>
```

### Hero 区块骨架
```html
<section class="bg-[#e74c3c] text-[#2d2d2d] py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div class="max-w-4xl mx-auto">
    <h1 class="font-serif font-bold uppercase tracking-wider text-5xl md:text-7xl lg:text-8xl">
      {HEADLINE}
    </h1>
    <p class="font-sans text-sm md:text-base max-w-xl">
      {SUBHEADLINE}
    </p>
    <button class="rounded-sm font-bold uppercase border-2 border-[#2d2d2d] transition-all duration-200 ease-in-out bg-[#e74c3c] text-white border-2 border-[#2d2d2d] shadow-[4px_4px_0px_#2d2d2d]">
      {CTA_TEXT}
    </button>
  </div>
</section>
```

### 卡片网格骨架
```html
<section class="bg-[#f5f0e8] text-[#2d2d2d] py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div class="max-w-6xl mx-auto">
    <h2 class="font-serif font-bold uppercase tracking-wider text-2xl md:text-4xl">{SECTION_TITLE}</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
      <!-- Card template - repeat for each card -->
      <div class="rounded-none bg-[#f5f0e8] border-2 border-[#2d2d2d] p-5 md:p-8">
        <h3 class="font-serif font-bold uppercase tracking-wider text-xl md:text-2xl">{CARD_TITLE}</h3>
        <p class="font-sans text-sm md:text-base text-[#2d2d2d]/50">{CARD_DESCRIPTION}</p>
      </div>
    </div>
  </div>
</section>
```

### 表单输入骨架
```html
<input class="rounded-none border-2 border-[#2d2d2d] bg-[#f5f0e8] focus:outline-none" placeholder="{PLACEHOLDER}" />
```

### 页脚骨架
```html
<footer class="bg-[#ebe4d8] text-[#e74c3c] py-12 md:py-20 lg:py-28 px-4 md:px-8 lg:px-12">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-10">
      <div>
        <span class="font-serif font-bold uppercase tracking-wider text-xl md:text-2xl">{LOGO_TEXT}</span>
        <p class="font-sans text-xs md:text-sm">{TAGLINE}</p>
      </div>
      <div>
        <h4 class="font-serif font-bold uppercase tracking-wider text-xl md:text-2xl">{COLUMN_TITLE}</h4>
        <ul class="font-sans text-xs md:text-sm">
          {FOOTER_LINKS}
        </ul>
      </div>
    </div>
  </div>
</footer>
```

---

## [CHECKLIST] Collage Art 生成后自检清单

**输出代码前，逐项验证当前风格的 token 和规则。如有违反，先修正再交付：**

### Token 检查
- [ ] 按钮包含： `rounded-sm font-bold uppercase border-2 border-[#2d2d2d] transition-all duration-200 ease-in-out`
- [ ] 卡片包含： `rounded-none bg-[#f5f0e8] border-2 border-[#2d2d2d]`
- [ ] 输入框包含： `rounded-none border-2 border-[#2d2d2d] bg-[#f5f0e8] focus:outline-none`

### 禁止项检查
- [ ] 没有使用 `rounded-lg`
- [ ] 没有使用 `rounded-xl`
- [ ] 没有使用 `rounded-2xl`
- [ ] 没有使用 `rounded-3xl`
- [ ] 没有使用 `rounded-full`
- [ ] 没有使用 `bg-gradient-to-r`
- [ ] 没有使用 `bg-gradient-to-b`
- [ ] 没有使用 `bg-gradient-to-br`

### 风格规则检查
- [ ] 使用混合字体（衬线 font-serif + 无衬线 font-sans + 等宽 font-mono 交替）
- [ ] 元素使用 Tailwind 任意值旋转 rotate-[Ndeg] 而非内联 style transform（避免与 hover 冲突）
- [ ] 使用硬偏移阴影 shadow-[Npx_Npx_0px_color] 营造层叠深度
- [ ] 添加 washi tape 装饰：repeating-linear-gradient 条纹色块
- [ ] 使用 polygon clip-path 创造撕纸边缘效果

### 风格漂移检查
- [ ] 没有违反：禁止使用平滑渐变（bg-gradient-to-*）
- [ ] 没有违反：禁止使用柔和圆角（rounded-lg 以上）
- [ ] 没有违反：禁止使用毛玻璃效果（backdrop-blur）
- [ ] 没有违反：禁止使用统一整齐的对齐方式
- [ ] 没有违反：禁止对有 hover/group-hover Tailwind 变换的元素使用 style={{ transform }} 内联属性（会导致 transform 冲突）

### 通用交付检查
- [ ] 响应式布局在手机、平板和桌面下稳定，没有横向溢出
- [ ] 所有交互元素有清晰焦点、可访问名称和 reduced-motion 方案
- [ ] 文本对比度达到 WCAG AA，且没有用颜色单独传递状态
- [ ] 结果仍然能够一眼识别为 Collage Art

---

## [EXAMPLES] 示例 Prompt

### 1. 拼贴艺术杂志页面

杂志拼贴风格的创意页面，带有旋转卡片、和纸胶带装饰和混搭字体

```
Use Collage Art style to create a zine-style page:
1. Background: aged paper #f5f0e8 with torn paper scrap decorations (clip-path polygon)
2. Hero: mixed fonts (serif title + sans subtitle + mono caption), random rotations on each line using rotate-[Xdeg] Tailwind class
3. Cards: hard offset shadows in different colors, each card rotated differently with rotate-[Xdeg]
4. Washi tape: repeating-linear-gradient stripe decorations, wrapped in group div for parallax effect
5. Buttons: rotated via rotate-[Xdeg], hover paper-lift effect (scale-105 + rotation change + shadow expand)
6. Form: mixed font labels (serif/sans/mono), dashed border textarea
7. Typography mixes serif, sans-serif, and monospace throughout
```

### 2. SaaS 着陆页

生成 拼贴艺术风风格的 SaaS 产品着陆页

```
Create a SaaS landing page using Collage Art style with hero section, feature grid, testimonials, pricing table, and footer.
```

### 3. 作品集展示

生成 拼贴艺术风风格的作品集页面

```
Create a portfolio showcase page using Collage Art style with project grid, about section, contact form, and consistent visual language.
```

## 绝对禁止（匹配即拒绝）

以下模式一旦出现，视为风格违规——不找借口，直接重写。

- 使用平滑渐变（bg-gradient-to-*）
- 使用柔和圆角（rounded-lg 以上）
- 使用毛玻璃效果（backdrop-blur）
- 使用统一整齐的对齐方式
- 对有 hover/group-hover Tailwind 变换的元素使用 style={{ transform }} 内联属性（会导致 transform 冲突）

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
- [ ] 禁止使用平滑渐变（bg-gradient-to-*）
- [ ] 禁止使用柔和圆角（rounded-lg 以上）
- [ ] 禁止使用毛玻璃效果（backdrop-blur）
- [ ] 禁止使用统一整齐的对齐方式
- [ ] 禁止对有 hover/group-hover Tailwind 变换的元素使用 style={{ transform }} 内联属性（会导致 transform 冲突）


---

# 模块四：新艺术运动风 (Art Nouveau) 规范

STYLEKIT_STYLE_REFERENCE
style_name: 新艺术运动风
style_slug: art-nouveau
style_source: /styles/art-nouveau

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

你是一个 Art Nouveau 设计风格的前端开发专家。生成的所有代码必须严格遵守以下约束：

## 绝对禁止

- 禁止使用生硬的直角和几何形状
- 禁止使用霓虹或高饱和度的现代色彩
- 禁止使用粗犷的无装饰设计
- 禁止使用现代无衬线字体作为标题
- 禁止使用短促生硬的 duration-150 或 duration-200

## 必须遵守

- 使用有机曲线和流动线条
- 采用深绿、金色、象牙白为主色调
- 添加藤蔓、花卉等自然装饰元素
- 使用衬线或装饰性字体
- 保持优雅精致的整体质感
- 圆润的边角和柔和的过渡
- 使用 duration-500 或 duration-700 配合 ease-in-out 表现自然律动
- 悬停时光晕柔和扩散（shadow 变大变柔和）
- 装饰元素在悬停时轻微放大或旋转，像花朵绽放

## Animation & Interaction Rules

- Organic Flow: 动画必须像植物生长一样自然流动。使用 duration-500 或 duration-700 配合平滑的 ease-in-out。
- Soft Glow: 悬停时光晕应该柔和地向外扩散（shadow 从小变大、从浅变深），不要使用生硬的位移。
- Decorative Flourishes: 装饰元素在悬停时产生轻微的放大或旋转（scale(1.1) rotate(5deg)），像花朵绽放。
- Radial Highlight: 卡片悬停时用 radial-gradient 伪元素产生角落光晕（opacity 0 -> 100）。
- Gentle Float: 卡片悬停时微微上浮 -translate-y-1，配合阴影扩散。

## 配色

主色调：
- 深绿: #2d5016
- 金色: #c9a227
- 象牙白: #f5f0e1
- 紫藤: #8b6db5

## 特殊元素

- 有机曲线 SVG 装饰
- 藤蔓和花卉图案
- 金色边框和光晕
- 优雅的渐变过渡

## Layout & Spacing
- Section padding: py-16 md:py-24
- Card padding: p-6 md:p-8
- Gap between cards: gap-6 md:gap-8
- Max content width: max-w-6xl mx-auto

## Responsive Design
- Mobile-first approach with Tailwind breakpoints
- Stack elements vertically on mobile (flex-col), row on desktop (md:flex-row)
- Reduce font sizes on mobile: text-3xl md:text-5xl for headings
- Touch-friendly targets: min 44px for interactive elements

## Self-Check Verification
After generating code, verify:
1. All interactive elements have hover/focus/active states
2. Color contrast meets WCAG 2.1 AA (4.5:1 for text)
3. Layout is responsive across breakpoints
4. Typography hierarchy is clear (h1 > h2 > h3 > body)
5. Spacing is consistent using the defined scale
6. All animations respect prefers-reduced-motion

---

# Art Nouveau (新艺术运动风) Design System

> 源自19世纪末的有机曲线美学，以流动的藤蔓纹样、自然花卉元素、Mucha风格海报装饰和优雅的衬线字体为特征，传递自然与艺术的和谐统一。

## 核心理念

Art Nouveau（新艺术运动）是19世纪末至20世纪初的国际性艺术运动，以自然界的有机形态为灵感，将装饰艺术推向极致。

核心理念：
- 有机曲线：受植物和花卉启发的流动线条
- 自然统一：艺术与自然的和谐融合
- 整体设计：从建筑到家具到海报的统一美学
- 装饰之美：精致的装饰纹样赋予功能性物品以艺术价值
- 生长律动：交互应如植物生长般缓慢、柔和、有机

设计原则：
- 视觉一致性：所有组件必须遵循统一的视觉语言，从色彩到字体到间距保持谐调
- 层次分明：通过颜色深浅、字号大小、留白空间建立清晰的信息层级
- 交互反馈：每个可交互元素都必须有明确的 hover、active、focus 状态反馈
- 响应式适配：设计必须在移动端、平板、桌面端上保持一致的体验
- 无障碍性：确保色彩对比度符合 WCAG 2.1 AA 标准，所有交互元素可键盘访问

---

## Token 字典（精确 Class 映射）

### 边框
`
宽度: border-2
颜色: border-[#c9a227]/60
圆角: rounded-2xl
`

### 阴影
`
小: shadow-sm
中: shadow-md
大: shadow-lg
悬停: hover:shadow-lg
聚焦: focus:shadow-[0_0_12px_rgba(201,162,39,0.3)]
`

### 交互效果
`
悬停位移: hover:-translate-y-1
悬停缩放: hover:scale-105
悬停透明度: （无）
过渡动画: transition-all duration-300 ease-in-out
按下状态: active:scale-95
`

### 字体
`
标题: font-serif tracking-wide
正文: font-serif
等宽: font-mono
`

### 字号
`
Hero: text-4xl md:text-6xl lg:text-8xl
H1: text-3xl md:text-5xl
H2: text-2xl md:text-4xl
H3: text-xl md:text-2xl
正文: text-sm md:text-base
小字: text-xs md:text-sm
`

### 间距
`
Section: py-12 md:py-20 lg:py-28
容器: px-4 md:px-8 lg:px-12
卡片: p-5 md:p-8
小间距: gap-3 md:gap-4
中间距: gap-4 md:gap-6
大间距: gap-6 md:gap-10
`

### 颜色角色
`
背景主色: bg-[#f5f0e1]
背景辅色: bg-[#e8dcc8]
背景强调色: bg-[#2d5016], bg-[#c9a227], bg-[#8b6db5]
正文主色: text-[#2d5016]
正文辅色: text-[#c9a227]
正文弱化色: text-[#2d5016]/60
按钮主色: bg-[#2d5016] text-[#f5f0e1] border-2 border-[#c9a227]
按钮辅色: bg-[#f5f0e1] text-[#2d5016] border-2 border-[#2d5016]
`

---

## [FORBIDDEN] 绝对禁止

以下 class 在本风格中**绝对禁止使用**，生成时必须检查并避免：

### 禁止的 Class
- 
ounded-none
- g-black
- g-gray-900
- g-[#0a0a1a]
- 	ext-[#ff00ff]
- 	ext-[#00ffff]
- shadow-[0_0_16px_rgba(255,0,255
- order-[#ff00ff]
- order-[#00ffff]
- uppercase
- ont-bold tracking-widest

---

## [REQUIRED] 必须包含

### 按钮必须包含
`
rounded-full
font-serif
border-2 border-[#c9a227]
transition-all duration-300 ease-in-out
`

### 卡片必须包含
`
rounded-2xl
bg-[#f5f0e1]
border-2 border-[#c9a227]/60
shadow-md
`

### 输入框必须包含
`
rounded-full
border-2 border-[#c9a227]/40
bg-[#f5f0e1]
text-[#2d5016]
focus:border-[#c9a227]
focus:outline-none
`

---

## [EXAMPLES] 示例 Prompt

### 1. 花卉展览页面

Art Nouveau风格的花卉展览展示

`
用 Art Nouveau 风格创建一个花卉展览页面，要求：
1. 背景：象牙白渐变 + 有机曲线装饰
2. 标题：衬线字体，深绿色
3. 卡片：金色边框，圆润边角，hover 时光晕扩散 + 微浮动
4. 添加藤蔓和花卉 SVG 装饰元素
5. 所有交互 duration-500 以上，ease-in-out
6. 整体优雅精致的自然美学
`

### 2. SaaS 着陆页

生成 新艺术运动风风格的 SaaS 产品着陆页

`
Create a SaaS landing page using Art Nouveau style with hero section, feature grid, testimonials, pricing table, and footer.
`

### 3. 作品集展示

生成 新艺术运动风风格的作品集页面

`
Create a portfolio showcase page using Art Nouveau style with project grid, about section, contact form, and consistent visual language.
`

## 绝对禁止（匹配即拒绝）

以下模式一旦出现，视为风格违规——不找借口，直接重写。

- 使用生硬的直角和几何形状
- 使用霓虹或高饱和度的现代色彩
- 使用粗犷的无装饰设计
- 使用现代无衬线字体作为标题
- 使用短促生硬的 duration-150 或 duration-200

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
- [ ] 禁止使用生硬的直角和几何形状
- [ ] 禁止使用霓虹或高饱和度的现代色彩
- [ ] 禁止使用粗犷的无装饰设计
- [ ] 禁止使用现代无衬线字体作为标题
- [ ] 禁止使用短促生硬的 duration-150 或 duration-200


# AstrBot 插件运行与渲染规则

1. **模板结构**：本仓库为外部模板仓库，安装后位于插件数据目录的 `templates/<template_name>/` 下。
2. **必需文件**：`image_template.html`, `html_template.html`, `topic_item.html`, `user_title_item.html`, `quote_item.html`, `activity_chart.html`, `chat_quality_item.html`, `template.json`, `preview.jpg`。
3. **资源内联要求**：渲染通过 Headless T2I，HTML 中所有资源必须为内联 SVG、Base64 或有效公网 CDN 绝对路径。
4. **安全转义**：`topic.detail` 与 `quote.reason` 包含插件预生成的安全富文本胶囊，必须使用 `| safe`。
