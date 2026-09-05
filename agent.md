# agent.md — AstrBot 报告视觉模板开发守则（暖色仪表盘 Warm Dashboard）

本仓库是 AstrBot「群聊日常分析」插件的**报告视觉模板**仓库。
本模板基于 **Warm Dashboard（暖色仪表盘）** 视觉系统构建。
以下规则适用于本仓库内的模板开发与维护，AI 辅助修改时必须以本文件为准。

---

# Hard Prompt & Style Rules

你是一个 Warm Dashboard（暖色仪表盘）设计风格的前端开发专家。

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

---

## [FORBIDDEN] 绝对禁止

以下规范在本风格中**绝对禁止使用**，生成与修改时必须严格检查：

- **禁止使用冷色背景**（蓝色、紫色，如 `bg-blue-500`, `bg-purple-500` 等）
- **禁止使用纯黑文字** `text-black` 或 `#000000`
- **禁止使用硬边阴影**（如 `shadow-[0px_0px_0px]`）
- **禁止使用高饱和度霓虹色**（如 `#00ffff`, `#ff00ff`）
- **禁止使用粗边框** `border-2` 及以上
- **禁止使用小圆角或无圆角** `rounded-none`, `rounded-sm`
- **禁止紫色到蓝色的渐变**
- **禁止嵌套卡片（卡片里面套大卡片）**
- **禁止在彩色背景上放低对比度灰色文字**

---

## [REQUIRED] 必须遵守

- **背景主色**：使用暖色调 `bg-[#d4a088]`（珊瑚/赤陶色）或 `bg-[#c9967a]`
- **卡片底色**：使用奶油白 `bg-[#faf8f5]` 或 `bg-white`
- **卡片圆角**：使用大圆角 `rounded-2xl` (16px) 或 `rounded-3xl` (24px)
- **卡片阴影**：使用柔和漫射阴影 `shadow-xl shadow-black/8` 或 `shadow-2xl shadow-black/10`
- **图表配色**：图表与强调使用青绿 `#4a9d9a` 和金黄 `#e8b86d`
- **文字配色**：文字使用深灰 `text-gray-800` (`#1f2937`) 或 `text-gray-600` (`#4b5563`)；暖色底色上使用纯白 `text-white`
- **微交互与光晕**：悬停时轻微上浮 `hover:-translate-y-0.5`，散发同色系柔和光晕 `hover:shadow-[0_8px_20px_rgba(74,157,154,0.25)]`

---

## Token 字典

| 维度 | Token / Class | 说明 |
| --- | --- | --- |
| **背景主色** | `bg-[#d4a088]` / `#c9967a` | 珊瑚/赤陶温暖底色 |
| **卡片主色** | `bg-[#faf8f5]` / `#ffffff` | 奶油白卡片 |
| **青绿主要强调** | `#4a9d9a` | 主按钮、正向数据高亮、标题修饰条 |
| **金黄图表色** | `#e8b86d` | 24h 轨迹图表、数据重点高亮 |
| **珊瑚次要强调** | `#c17767` | 警告、负向数据、锐评标签 |
| **灰绿辅助** | `#6b8e8e` | 次要元素、辅助装饰 |
| **正文主色** | `text-gray-800` (`#1f2937`) | 一级标题与重点文字 |
| **正文次色** | `text-gray-600` (`#4b5563`) | 正文内容与描述 |
| **弱化文字** | `text-gray-400` (`#9ca3af`) | 时间、次要统计标签 |
| **边框** | `border border-gray-200/50` | 单像素细边框 |
| **圆角** | `rounded-2xl` / `rounded-3xl` | 大圆角柔和轮廓 |
| **阴影** | `shadow-xl shadow-black/8` | 柔和漫射扩散阴影 |

---

## AstrBot 插件渲染契约

### 1. 模板目录结构
```
gda_warm_dashboard/
├── image_template.html  # 长图海报主骨架（固定宽 750px）
├── html_template.html   # 网页主骨架（响应式）
├── topic_item.html      # 话题列表子模块
├── user_title_item.html # 群友称号子模块
├── quote_item.html      # 金句子模块
├── activity_chart.html  # 24h 活跃图表子模块
├── chat_quality_item.html # 质量锐评子模块
├── template.json        # 模板显示元信息
└── preview.jpg          # 随包预览图
```

### 2. 渲染变量
- **主骨架**：`topics_html`, `titles_html`, `quotes_html`, `hourly_chart_html`, `chat_quality_html`（可选）, `message_count`, `participant_count`, `total_characters`, `emoji_count`, `most_active_period`, `current_date`, `current_datetime`, `total_tokens`, `prompt_tokens`, `completion_tokens`, `hide_user_names`, `t2i_*`。
- **子模块**：
  - `topic_item.html` -> `topics`（`topic.detail` 含 safe HTML）
  - `user_title_item.html` -> `titles`
  - `quote_item.html` -> `quotes`（`quote.reason` 含 safe HTML）
  - `activity_chart.html` -> `chart_data`
  - `chat_quality_item.html` -> `title`, `subtitle`, `summary`, `dimensions`

### 3. 资源约束
- HTML 交给远程 T2I 渲染服务，**没有本地文件上下文**：
  - ✅ 绝对 URL 或内联 `data:` URI / `<svg>`
  - ❌ 相对路径（`src="assets/bg.png"`）渲染时必然 404

---

## 修改工作流

1. **语法与渲染校验**：运行 `python verify_demo.py`（StrictUndefined 实际渲染 7 个文件）。
2. **预览图生成**：运行 `python generate_preview.py` 刷新 `assets/` 与 `gda_warm_dashboard/preview.jpg`。
3. **提交与推送**：Conventional Commits 中文规范提交。
