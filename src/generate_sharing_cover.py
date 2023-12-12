import os
from turtle import bgcolor
import qrcode
from PIL import Image, ImageDraw, ImageFont
from .utils import auto_title_lines, convert_svg_to_png


COVER_BG_DIR = "./img/sharing_cover_bg.png"
COVER_BG_DIR_2 = "./img/sharing_cover_bg_2.png"
DEFAULT_LOGO_DIR = "./img/share_to_earn.png"

TITLE_FONT = "./font/Kollektif.ttf"
INFO_FONT = "./font/Montserrat-VariableFont_wght.ttf"


def generate_sharing_cover(
    title: str,
    presenter: str,
    meeting_number: str,
    time_str: str,
    meeting_link: str,
    language: str = "Chinese",
    twitter: str = "",
    project: str = "",
    project_logo: str = "",
    meeting_type: str = "tencent",  # "tencent" | "zoom"
):
    # 加载海报图片
    if project_logo != "":
        poster = Image.open(COVER_BG_DIR_2)
    else:
        poster = Image.open(COVER_BG_DIR)

    draw = ImageDraw.Draw(poster)

    padding = 120
    content_width = poster.width - padding * 2

    # title
    title_font = ImageFont.truetype(TITLE_FONT, size=120)
    title_position_x = padding
    title_position_y = 400
    text_color = "#FFFFFF"

    title_lines = auto_title_lines(title, title_font, content_width)
    # add title
    for _title, _left, _top in title_lines:
        draw.text(
            (title_position_x + _left, title_position_y + _top),
            _title,
            font=title_font,
            fill=text_color,
            align="center",
        )

    # DATE info
    date_position_x = padding
    date_position_y = 650

    date_lines = [f"DATE   {time_str}"]

    date_font = ImageFont.truetype(TITLE_FONT, size=50)
    date_top = date_position_y
    for _info in date_lines:
        (left, top, right, bottom) = date_font.getbbox(_info)
        _w = right - left
        _h = bottom - top
        draw.text(
            (date_position_x + (content_width - _w) // 2 + 2, date_top),
            _info,
            font=date_font,
            fill="#ffffff",
            align="center",
        )
        date_top += _h + 20
    
    # presenter info
    presenter_font = ImageFont.truetype(TITLE_FONT, size=50)

    (left, top, right, bottom) = presenter_font.getbbox(presenter)
    _w = right - left
    draw.text(
        (padding + (content_width - _w) // 2 + 128, 754),
        presenter,
        font=presenter_font,
        fill="#ffffff",
        align="center",
    )

    (left, top, right, bottom) = presenter_font.getbbox(presenter)
    _w = right - left
    draw.text(
        (padding + 768, 852),
        twitter,
        font=presenter_font,
        fill="#ffffff",
        align="center",
    )

    # right-top logo
    if project_logo != "":
        top_right_logo = convert_svg_to_png(project_logo, bg_color="#300480")
        poster.paste(
            top_right_logo,
            (
                poster.width - 300 - (padding + top_right_logo.width // 2),
                padding + 100 - (top_right_logo.height // 2),
            ),
        )
    else:
        top_right_logo = Image.open(DEFAULT_LOGO_DIR)
        poster.paste(top_right_logo, (poster.width - 640, 140))

    poster.save("./output/sharing_cover.png")
    # poster.show()


if __name__ == "__main__":
    meeting_link = "https://us06web.zoom.us/j/84222261147"

    generate_sharing_cover(
        title="Reqeust Network XXXX",
        presenter="David",
        twitter="@David",
        language="English",
        project="Reqeust Network",
        project_logo="./ethereum_foundation_logo.svg",
        time_str="2023-12-14",
        meeting_number="842-222-61147",
        meeting_link=meeting_link,
        meeting_type="zoom",
    )
