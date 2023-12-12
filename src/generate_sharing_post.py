import os
import qrcode
import cairosvg
from PIL import Image, ImageDraw, ImageFont

from .utils import auto_title_lines, convert_svg_to_png


BG_DIR = "./img/sharing_post_bg.png"
DEFAULT_LOGO_DIR = "./img/share_to_earn.png"

TITLE_FONT = "./font/Kollektif.ttf"
INFO_FONT = "./font/Montserrat-VariableFont_wght.ttf"

BG_COLOR = "#101E3F"


def generate_sharing_post(
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
    poster = Image.open(BG_DIR)
    draw = ImageDraw.Draw(poster)

    padding = 120
    content_width = poster.width - padding * 2

    # title
    title_font = ImageFont.truetype(TITLE_FONT, size=140)
    title_position_x = padding
    title_position_y = 480
    text_color = "#A6FBF6"  # 或者使用RGB颜色，如(255, 255, 255)

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

    # info
    info_position_x = padding
    info_position_y = 1015

    info_lines = [f"Presented by: {presenter}"]
    if twitter != "":
        info_lines.append(f"Twitter: {twitter}")
    if language != "":
        info_lines.append(f"Language: {language}")
    else:
        info_lines.append("Language: Chinese")
    if project != "":
        info_lines.append(f"Project: {project}")

    info_lines.reverse()

    info_font = ImageFont.truetype(INFO_FONT, size=52)
    info_top = info_position_y
    for _info in info_lines:
        (left, top, right, bottom) = info_font.getbbox(_info)
        _w = right - left
        _h = bottom - top
        draw.text(
            (info_position_x + (content_width - _w) // 2, info_top),
            _info,
            font=info_font,
            fill=text_color,
            align="center",
            stroke_width=1,
        )
        info_top -= _h + 16

    # meeting info
    meeting_position_x = padding
    meeting_position_y = 1220

    meeting_lines = [
        f"TIME: {time_str}",
        f"{meeting_type.upper()} MEETING: {meeting_number}",
    ]

    meeting_font = ImageFont.truetype(TITLE_FONT, size=56)
    meeting_top = meeting_position_y
    for _info in meeting_lines:
        (left, top, right, bottom) = meeting_font.getbbox(_info)
        _w = right - left
        _h = bottom - top
        draw.text(
            (meeting_position_x + (content_width - _w) // 2, meeting_top),
            _info,
            font=meeting_font,
            fill="#81A8F8",
            align="center",
            stroke_width=1,
        )
        meeting_top += _h + 20

    # right-top logo
    if project_logo != "":
        top_right_logo = convert_svg_to_png(project_logo)
        poster.paste(
            top_right_logo,
            (
                poster.width - 320 - (padding + top_right_logo.width // 2),
                padding + 100 - (top_right_logo.height // 2),
            ),
        )
    else:
        top_right_logo = Image.open(DEFAULT_LOGO_DIR)
        poster.paste(top_right_logo, (poster.width - 640, 140))

    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=1,
    )
    qr.add_data(meeting_link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # meeting link qrcode
    qr_position = (int(220 + qr_img.width / 2), poster.height - qr_img.height - 308)

    # 粘贴二维码到海报
    poster.paste(qr_img, qr_position)

    # 保存或显示最终海报
    poster.save("./output/sharing_post.png")  # 保存海报
    # poster.show()
