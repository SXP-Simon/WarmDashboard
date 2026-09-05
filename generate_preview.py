"""生成模板预览图：渲染 image_template.html → 无头浏览器截图 → 底部背景裁剪 → JPEG。

用法:
    python generate_preview.py [模板名称]
    （不传时默认处理所有模板目录）

输出: assets/<template_name>-demo.jpg
依赖: 无头浏览器（Chrome/Edge），可选 PIL（环境无 PIL 时保留 PNG）。
"""
import argparse
import base64
import shutil
import subprocess
import tempfile
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "assets"

# ---------- 1) 构造富有个性与温度的示例头像 ----------
def rich_svg_avatar(bg_color: str, skin_color: str, hair_color: str, hair_type: int = 1) -> str:
    """生成带有插画风格的 SVG 头像"""
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


def render_and_shot(tpl_dir: Path, browser: str):
    print(f"\n>> 正在生成预览: {tpl_dir.name}")
    out_jpg = OUT_DIR / f"{tpl_dir.name}-demo.jpg"
    out_thumb = OUT_DIR / f"{tpl_dir.name}-demo-thumb.jpg"
    out_png = OUT_DIR / f"{tpl_dir.name}-demo.png"

    env = Environment(
        loader=FileSystemLoader(str(tpl_dir)),
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
                "topic": {"topic": "新版本功能与设计提案"},
                "contributors": "阿伟、小美、小明",
                "detail": "建议把群聊日常报告全面重构为清新治愈风格：留白呼吸感 + 发丝边框 + 植物线描，方案已获全票通过！",
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
        "chart_data": [
            {"hour": i, "count": (i * 7 + 3) % 24 + 4, "percentage": min(100, int(((i * 7 + 3) % 24 + 4) * 3.8))}
            for i in range(24)
        ],
        "title": "今日群聊质量锐评",
        "subtitle": "氛围融洽度 A+",
        "summary": "全群保持高热度良性互动，宛若初晨清风般温和沉静。话题发散自然，有深度交流亦有生动斗图，留白与活力兼备！",
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
            print(f"[error] 截图失败: {res.stderr}")
            return

        try:
            from PIL import Image

            img = Image.open(png_tmp)
            w, h = img.size

            # 智能检测底部内容边界
            def is_content_row(image, y, width, step=8):
                for x in range(20, width - 20, step):
                    pixel = image.getpixel((x, y))
                    if len(pixel) >= 3:
                        r, g, b = pixel[:3]
                        if (r < 100 and g < 100 and b < 100) or (r > 250 and g > 250 and b > 250):
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
            img_rgb.save(out_jpg, "JPEG", quality=90)
            print(f"[ok] 预览图: {out_jpg} ({img_rgb.size[0]}x{img_rgb.size[1]})")

            thumb = img_rgb.copy()
            thumb.thumbnail((384, 1500), Image.Resampling.LANCZOS)
            thumb.save(out_thumb, "JPEG", quality=85)
            print(f"[ok] 缩略图: {out_thumb} ({thumb.size[0]}x{thumb.size[1]})")

            shutil.copy2(out_jpg, tpl_dir / "preview.jpg")
            print(f"[ok] 同步模板预览图: {tpl_dir / 'preview.jpg'}")

        except ImportError:
            shutil.copy2(png_tmp, out_png)
            print(f"[ok] 未安装 Pillow，已输出原始 PNG: {out_png}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", nargs="?", help="指定要渲染的模板名称")
    args = parser.parse_args()

    browser = find_browser()
    if not browser:
        print("[skip] 未找到可用浏览器（Chrome / Edge）。")
        return

    if args.template:
        target = ROOT / args.template
        if target.is_dir():
            render_and_shot(target, browser)
        else:
            print(f"[error] 未找到模板目录: {args.template}")
    else:
        tpl_dirs = [d for d in ROOT.iterdir() if d.is_dir() and (d / "template.json").exists()]
        for d in sorted(tpl_dirs, key=lambda p: p.name):
            render_and_shot(d, browser)


if __name__ == "__main__":
    main()
