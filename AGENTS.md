# AGENTS.md — AstrBot 报告视觉模板开发守则

本仓库支持两套核心设计风格规范：
1. **日系清新风 (Japanese Fresh)** (`gda_japanese_fresh`)
2. **暖色仪表盘 (Warm Dashboard)** (`gda_warm_dashboard`)

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
Section: py-24 md:py-32 lg:py-40
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
```

---

# 模块二：暖色仪表盘 (Warm Dashboard) 规范

STYLEKIT_STYLE_REFERENCE
style_name: 暖色仪表盘
style_slug: warm-dashboard
style_source: /styles/warm-dashboard

## Style Rules
- 背景：bg-[#d4a088] 珊瑚/赤陶色
- 卡片：bg-[#faf8f5] 奶油白
- 圆角：rounded-2xl 或 rounded-3xl
- 阴影：shadow-xl shadow-black/8（柔和漫射）
- 图表：青绿 #4a9d9a 和金黄 #e8b86d 配色
- 文字：深灰 text-gray-800、正文 text-gray-600、暖背景上 text-white

---

# AstrBot 插件运行与渲染规则

1. **模板结构**：本仓库为外部模板仓库，安装后位于插件数据目录的 `templates/<template_name>/` 下。
2. **必需文件**：`image_template.html`, `html_template.html`, `topic_item.html`, `user_title_item.html`, `quote_item.html`, `activity_chart.html`, `chat_quality_item.html`, `template.json`, `preview.jpg`。
3. **资源内联要求**：渲染通过 Headless T2I，HTML 中所有资源必须为内联 SVG、Base64 或有效公网 CDN 绝对路径。
4. **安全转义**：`topic.detail` 与 `quote.reason` 包含插件预生成的安全富文本胶囊，必须使用 `| safe`。
