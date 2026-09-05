"""生成模板预览图：渲染 image_template.html → 无头浏览器截图 → 底部背景裁剪 → JPEG。

用法:
    python generate_preview.py

输出: assets/gda_warm_dashboard-demo.jpg
依赖: 无头浏览器（Chrome/Edge），可选 PIL（环境无 PIL 时保留 PNG）。
"""
import base64
import shutil
import subprocess
import tempfile
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent
TPL = ROOT / "gda_warm_dashboard"
OUT_DIR = ROOT / "assets"
OUT_JPG = OUT_DIR / "gda_warm_dashboard-demo.jpg"
OUT_THUMB = OUT_DIR / "gda_warm_dashboard-demo-thumb.jpg"
OUT_PNG = OUT_DIR / "gda_warm_dashboard-demo.png"

# ---------- 1) 构造更精美、富有个性与温度的示例头像 ----------
def rich_svg_avatar(bg_color: str, skin_color: str, hair_color: str, hair_type: int = 1) -> str:
    """生成带有暖色温润插画风格的 SVG 头像"""
    hair_path = (
        f'<path d="M26 38 Q48 14 70 38 Q78 52 74 62 Q68 44 48 42 Q28 44 22 62 Q18 52 26 38 Z" fill="{hair_color}"/>'
        if hair_type == 1
        else f'<path d="M22 36 Q48 12 74 36 Q78 68 68 76 Q60 48 48 44 Q36 48 28 76 Q18 68 22 36 Z" fill="{hair_color}"/>'
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" width="96" height="96">'
        f'<rect width="96" height="96" rx="48" fill="{bg_color}"/>'
        f'<circle cx="48" cy="46" r="21" fill="{skin_color}"/>'
        f'<path d="M22 88 C24 66 35 60 48 60 C61 60 72 66 74 88 Z" fill="{hair_color}" opacity="0.9"/>'
        f'{hair_path}'
        f'<circle cx="41" cy="46" r="2.5" fill="#2d3748"/>'
        f'<circle cx="55" cy="46" r="2.5" fill="#2d3748"/>'
        f'<path d="M44 54 Q48 57 52 54" stroke="#c17767" stroke-width="2" fill="none" stroke-linecap="round"/>'
        f'<circle cx="36" cy="50" r="3" fill="#fca5a5" opacity="0.5"/>'
        f'<circle cx="60" cy="50" r="3" fill="#fca5a5" opacity="0.5"/>'
        f'</svg>'
    )
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


env = Environment(
    loader=FileSystemLoader(str(TPL)),
    autoescape=True,
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=StrictUndefined,
)
common = {
    "hide_user_names": False,
    "t2i_font_source": "Mainland",
    "t2i_google_fonts_mirror": "https://fonts.googleapis.com",
    "t2i_gstatic_mirror": "https://fonts.gstatic.com",
    "t2i_atri_font_mirror": "",
}

avatar_ming = rich_svg_avatar("#d1ecea", "#fed7aa", "#4a9d9a", 1)
avatar_hong = rich_svg_avatar("#fef08a", "#fed7aa", "#b57a1e", 2)
avatar_wei = rich_svg_avatar("#fed7aa", "#ffedd5", "#c17767", 1)

sub_ctx = {
    "topics": [
        {
            "index": 1,
            "topic": {"topic": "今晚吃什么？群里热聊 40 分钟美食规划"},
            "contributors": "小明、小红、阿伟",
            "detail": "最终决定去吃铜锅涮肉，<b>人均 85</b>，周五晚八点老地方集合～阿伟负责订包间，小红带自制杨梅气泡饮！",
        },
        {
            "index": 2,
            "topic": {"topic": "新版本功能与暖色仪表盘设计提案"},
            "contributors": "阿伟、小美、小明",
            "detail": "建议把群聊日常报告全面重构为 <b>Warm Dashboard</b> 风格：赤陶暖色大底 + 奶油白卡片 + 漫射柔和阴影，方案已获全票通过！",
        },
        {
            "index": 3,
            "topic": {"topic": "周末摄影约拍与器材交流"},
            "contributors": "小红、阿伟",
            "detail": "讨论了秋季银杏大道的拍摄路线与光线布局，提醒大家注意周末气温变化与防风保暖。",
        },
    ],
    "titles": [
        {
            "name": "小明",
            "title": "话题发动机",
            "mbti": "ENFP",
            "reason": "几乎每个热门话题都由 TA 率先开启，是群里不可或缺的气氛担当与活力源泉。",
            "avatar_data": avatar_ming,
            "profile_display": "ENFP 竞选者",
        },
        {
            "name": "小红",
            "title": "深夜守望者",
            "mbti": "ISTP",
            "reason": "凌晨 1 点的群聊里总能看到 TA 治愈系的金句回复，默默守望着大家的碎碎念。",
            "avatar_data": avatar_hong,
            "profile_display": "ISTP 鉴赏家",
        },
        {
            "name": "阿伟",
            "title": "冷场急救星",
            "mbti": "INFJ",
            "reason": "擅长在群聊冷却时抛出让人会心一笑的新奇讨论点，瞬间拉满全员互动热情。",
            "avatar_data": avatar_wei,
            "profile_display": "INFJ 提倡者",
        },
    ],
    "quotes": [
        {
            "content": "今天真开心，感觉自己又变聪明了一点点！",
            "sender": "小红",
            "reason": "典型的“学到新知识就疯狂膨胀”式自我鼓励，已成为全群今日的开心催化剂。",
            "avatar_url": avatar_hong,
        },
        {
            "content": "猫又踩我键盘发了一串乱码，但仔细一瞧居然有理有据。",
            "sender": "阿伟",
            "reason": "猫猫特工队代班发言，群友纷纷表示赞同并强烈要求给猫猫颁发管理员职位。",
            "avatar_url": avatar_wei,
        },
    ],
    "chart_data": [{"hour": i, "count": (i * 7 + 3) % 24 + 4, "percentage": min(100, int(((i * 7 + 3) % 24 + 4) * 3.8))} for i in range(24)],
    "title": "今日群聊质量锐评",
    "subtitle": "氛围融洽度 A+",
    "summary": "全群保持高热度良性互动，赤陶暖阳般亲和温暖。话题发散自然，有深度交流亦有生动斗图，群聊活力指数拉满！",
    "dimensions": [
        {"name": "活跃热度", "percentage": 94, "comment": "全天无冷场，高频交流自然"},
        {"name": "话题深度", "percentage": 82, "comment": "技术讨论与生活闲聊并存"},
        {"name": "含梗趣味", "percentage": 88, "comment": "金句频现，表情包恰到好处"},
    ],
}
topics_html = env.get_template("topic_item.html").render(**common, **sub_ctx)
titles_html = env.get_template("user_title_item.html").render(**common, **sub_ctx)
quotes_html = env.get_template("quote_item.html").render(**common, **sub_ctx)
hourly_chart_html = env.get_template("activity_chart.html").render(**common, **sub_ctx)
chat_quality_html = env.get_template("chat_quality_item.html").render(**common, **sub_ctx)
main_ctx = {
    **common,
    "topics_html": topics_html,
    "titles_html": titles_html,
    "quotes_html": quotes_html,
    "hourly_chart_html": hourly_chart_html,
    "chat_quality_html": chat_quality_html,
    "message_count": 1428,
    "participant_count": 42,
    "total_characters": 36890,
    "emoji_count": 316,
    "most_active_period": "20:00 - 22:00",
    "current_date": "2026年09月05日",
    "current_datetime": "2026-09-05 22:30:15",
    "total_tokens": 5820,
    "prompt_tokens": 4210,
    "completion_tokens": 1610,
}
rendered_html = env.get_template("image_template.html").render(**main_ctx)

# ---------- 2) 寻找可用浏览器 ----------
def find_browser() -> str | None:
    for name in ("chrome", "google-chrome", "chromium", "msedge"):
        p = shutil.which(name)
        if p:
            return p
    for path in (
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ):
        if Path(path).exists():
            return path
    return None


browser = find_browser()
if not browser:
    print("[skip] 未找到可用浏览器（Chrome / Edge），请手动在浏览器中查看渲染效果。")
    exit(0)

# ---------- 3) 无头截图 ----------
OUT_DIR.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory() as td:
    html_path = Path(td) / "render.html"
    png_tmp = Path(td) / "shot.png"
    html_path.write_text(rendered_html, encoding="utf-8")

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-sandbox",
        "--disable-extensions",
        "--disable-sync",
        "--disable-background-networking",
        "--disable-default-apps",
        "--metrics-recording-only",
        "--virtual-time-budget=2000",
        "--force-device-scale-factor=1",
        "--window-size=750,8000",
        f"--screenshot={png_tmp}",
        str(html_path),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if res.returncode != 0:
        print("[error] 浏览器截图失败:", res.stderr)
        exit(1)

    if not png_tmp.exists() or png_tmp.stat().st_size == 0:
        print("[error] 截图文件未生成")
        exit(1)

    # ---------- 4) 智能裁剪与转换 ----------
    try:
        from PIL import Image

        img = Image.open(png_tmp)
        w, h = img.size

        # 智能检测底部内容边界：
        # 背景（包括点阵与渐变）：RGB大致在 r: 180~235, g: 130~190, b: 100~170，且不会有高对比度的白字或深灰字
        # 内容区域（卡片/页脚）：存在真正的白字 (r>250, g>250, b>250 且不透明) 或 奶油白卡片 (#faf8f5) 或 深色字 (r<80)
        def is_content_row(image, y, width, step=8):
            for x in range(20, width - 20, step):
                pixel = image.getpixel((x, y))
                if len(pixel) >= 3:
                    r, g, b = pixel[:3]
                    # 卡片主体奶油白或者深灰文字
                    if (r > 245 and g > 240 and b > 235) or (r < 90 and g < 90 and b < 90):
                        return True
                    # 页脚的高亮纯白文字
                    if r >= 254 and g >= 254 and b >= 254:
                        return True
            return False

        content_bottom = h
        for y in range(h - 1, 0, -4):
            if is_content_row(img, y, w):
                content_bottom = min(h, y + 60)
                break

        if content_bottom < h and content_bottom > 500:
            img = img.crop((0, 0, w, content_bottom))

        img_rgb = img.convert("RGB")
        img_rgb.save(OUT_JPG, "JPEG", quality=90)
        print(f"[ok] 预览图: {OUT_JPG} ({img_rgb.size[0]}x{img_rgb.size[1]})")

        # 生成缩略图
        thumb = img_rgb.copy()
        thumb.thumbnail((384, 1500), Image.Resampling.LANCZOS)
        thumb.save(OUT_THUMB, "JPEG", quality=85)
        print(f"[ok] 缩略图: {OUT_THUMB} ({thumb.size[0]}x{thumb.size[1]})")

        # 同步更新模板内置 preview.jpg
        shutil.copy2(OUT_JPG, TPL / "preview.jpg")
        print(f"[ok] 同步模板目录预览图: {TPL / 'preview.jpg'}")

    except ImportError:
        shutil.copy2(png_tmp, OUT_PNG)
        print(f"[ok] 未安装 Pillow，已输出原始 PNG: {OUT_PNG}")
