"""验证 demo 模板仓库：Jinja2 语法 + 运行时渲染 + 安装器端到端（打包→安装→卸载）。

用法:
    python verify_demo.py [插件仓库路径]

插件仓库路径也可以不传，通过环境变量 PLUGIN_ROOT 指定；
不指定时仅执行模板自身的语法与渲染校验，跳过安装器端到端部分。
"""
import io
import json
import os
import sys
import tempfile
import zipfile
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent
PLUGIN_ROOT = (sys.argv[1] if len(sys.argv) > 1 else "") or os.environ.get(
    "PLUGIN_ROOT", ""
)

# 查找所有包含 template.json 的模板目录
tpl_dirs = [d for d in ROOT.iterdir() if d.is_dir() and (d / "template.json").exists()]
if not tpl_dirs:
    print("[error] 未找到包含 template.json 的模板目录")
    sys.exit(1)

common = {
    "hide_user_names": False,
    "t2i_font_source": "Mainland",
    "t2i_google_fonts_mirror": "https://fonts.googleapis.com",
    "t2i_gstatic_mirror": "https://fonts.gstatic.com",
    "t2i_atri_font_mirror": "",
}
sub_ctx = {
    "topics": [
        {
            "index": 1,
            "topic": {"topic": "测试话题"},
            "contributors": "小明、小红",
            "detail": "这是<b>详情</b>（含头像）",
        }
    ],
    "titles": [
        {
            "name": "小明",
            "title": "话题王",
            "mbti": "ENFP",
            "reason": "理由文本",
            "avatar_data": "https://example.com/a.png",
            "profile_display": "ENFP",
        }
    ],
    "quotes": [
        {
            "content": "今天真开心",
            "sender": "小红",
            "reason": "这是<b>锐评</b>",
            "avatar_url": "https://example.com/q.png",
        }
    ],
    "chart_data": [{"hour": i, "count": i, "percentage": i * 4} for i in range(24)],
    "title": "群聊质量",
    "subtitle": "锐评",
    "summary": "质量总结文本",
    "dimensions": [{"name": "活跃度", "percentage": 80, "comment": "很好"}],
}

for tpl_dir in sorted(tpl_dirs, key=lambda p: p.name):
    print(f"\n===== 正在校验模板: {tpl_dir.name} =====")
    # 1) Jinja2 语法检查
    env = Environment(
        loader=FileSystemLoader(str(tpl_dir)),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    for f in sorted(tpl_dir.glob("*.html")):
        env.parse(f.read_text(encoding="utf-8"))
        print(f"[{tpl_dir.name}] [syntax OK] {f.name}")

    # 2) 运行时渲染检查（StrictUndefined：任何变量缺失/类型错误立即抛错）
    rt_env = Environment(
        loader=FileSystemLoader(str(tpl_dir)),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined,
    )
    topics_html = rt_env.get_template("topic_item.html").render(**common, **sub_ctx)
    titles_html = rt_env.get_template("user_title_item.html").render(**common, **sub_ctx)
    quotes_html = rt_env.get_template("quote_item.html").render(**common, **sub_ctx)
    hourly_chart_html = rt_env.get_template("activity_chart.html").render(
        **common, **sub_ctx
    )
    chat_quality_html = rt_env.get_template("chat_quality_item.html").render(
        **common, **sub_ctx
    )
    main_ctx = {
        **common,
        "topics_html": topics_html,
        "titles_html": titles_html,
        "quotes_html": quotes_html,
        "hourly_chart_html": hourly_chart_html,
        "chat_quality_html": chat_quality_html,
        "message_count": 100,
        "participant_count": 20,
        "total_characters": 3000,
        "emoji_count": 10,
        "most_active_period": "20:00-22:00",
        "current_date": "2026年09月05日",
        "current_datetime": "2026-09-05 20:00:00",
        "total_tokens": 1000,
        "prompt_tokens": 500,
        "completion_tokens": 500,
    }
    for name in ("image_template.html", "html_template.html"):
        html = rt_env.get_template(name).render(**main_ctx)
        assert len(html) > 500
        # 语义断言：验证关键数据与结构插值正确
        assert "2026年09月05日" in html
        assert "测试话题" in html
        assert "20:00-22:00" in html
        if tpl_dir.name == "gda_warm_dashboard":
            assert "群聊日常分析" in html and "今日话题" in html and "金句" in html
        elif tpl_dir.name == "gda_japanese_fresh":
            assert "时间的轨迹" in html and "话题的交织" in html
        print(f"[{tpl_dir.name}] [render OK] {name} ({len(html)} bytes)")

if not PLUGIN_ROOT or not (Path(PLUGIN_ROOT) / "src").is_dir():
    print(
        "[skip] 未指定插件仓库路径，跳过安装器端到端检查。\n"
        "       用法: python verify_demo.py <插件仓库路径>  （或设置环境变量 PLUGIN_ROOT）",
        file=sys.stderr,
    )
    sys.exit(0)

sys.path.insert(0, PLUGIN_ROOT)

# 与插件 tests/conftest.py 一致的 astrbot mock（本机未安装 astrbot 包）
import logging  # noqa: E402
import types  # noqa: E402

if "astrbot.api" not in sys.modules:
    astrbot_module = types.ModuleType("astrbot")
    astrbot_api_module = types.ModuleType("astrbot.api")
    astrbot_star_module = types.ModuleType("astrbot.api.star")

    class StarTools:  # noqa: D101
        pass

    astrbot_api_module.logger = logging.getLogger("astrbot-demo")
    astrbot_api_module.AstrBotConfig = dict
    astrbot_star_module.StarTools = StarTools
    astrbot_module.api = astrbot_api_module
    sys.modules.setdefault("astrbot", astrbot_module)
    sys.modules.setdefault("astrbot.api", astrbot_api_module)
    sys.modules.setdefault("astrbot.api.star", astrbot_star_module)

from src.infrastructure.reporting.template_installer import (  # noqa: E402
    install_template_from_zip,
    uninstall_template,
)

for tpl_dir in sorted(tpl_dirs, key=lambda p: p.name):
    # 打包 zip（模拟仓库下载后的结构）
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(tpl_dir.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(ROOT).as_posix())

    with tempfile.TemporaryDirectory() as td:
        installed_root = Path(td)
        res = install_template_from_zip(
            buf.getvalue(),
            store_dir=installed_root,
        )
        print(f"[install {tpl_dir.name}]", json.dumps(res, ensure_ascii=False))
        assert res["name"] == tpl_dir.name
        assert (installed_root / tpl_dir.name / "image_template.html").is_file()

        un_res = uninstall_template(tpl_dir.name, store_dir=installed_root)
        print(f"[uninstall {tpl_dir.name}]", un_res)
        assert un_res["removed"] is True

print("\nALL OK")
