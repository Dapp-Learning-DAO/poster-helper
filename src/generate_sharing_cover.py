import os
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageOps
from .utils import auto_title_lines, convert_svg_to_png


COVER_BG_DIR = "./img/sharing_cover_bg.png"
COVER_BG_DIR_2 = "./img/sharing_cover_bg_2.png"
DEFAULT_LOGO_DIR = "./img/share_to_earn.png"

TITLE_FONT = "./font/SourceHanSansCN-Bold.otf"
INFO_FONT = "./font/SourceHanSansCN-Normal.otf"

RIGHT_TOP_LOGO_SIZE = (300, 200)


def generate_sharing_cover(
    title: str,
    title_size: int,
    presenter: str,
    meeting_number: str,
    time_str: str,
    meeting_link: str,
    language: str = "Chinese",
    presenter_avatar: str = "",
    twitter: str = "",
    project: str = "",
    project_logo: str = "",
    project_log_max_size = RIGHT_TOP_LOGO_SIZE,
    meeting_type: str = "tencent",  # "tencent" | "zoom"
):
    # 加载海报图片
    if project_logo != "":
        poster = Image.open(COVER_BG_DIR_2).convert("RGBA")
    else:
        poster = Image.open(COVER_BG_DIR).convert("RGBA")

    draw = ImageDraw.Draw(poster)

    padding = 150
    content_width = poster.width - padding * 2

    # title
    title_position_x = padding
    title_position_y = 320
    text_color = "#FFFFFF"

    title_lines = auto_title_lines(title, title_size, content_width, line_height=40)
    # add title
    for _title, _left, _top, _font in title_lines:
        draw.text(
            (title_position_x + _left, title_position_y + _top),
            _title,
            font=_font,
            fill=text_color,
            align="center",
        )

    # DATE info
    # date_position_x = padding
    # date_position_y = 650

    # date_lines = [f"TIME   {time_str}"]

    # date_font = ImageFont.truetype(TITLE_FONT, size=50)
    # date_top = date_position_y
    # for _info in date_lines:
    #     (left, top, right, bottom) = date_font.getbbox(_info)
    #     _w = right - left
    #     _h = bottom - top
    #     draw.text(
    #         (date_position_x + (content_width - _w) // 2 + 50, date_top),
    #         _info,
    #         font=date_font,
    #         fill="#ffffff",
    #         align="center",
    #     )
    #     date_top += _h + 20

    # presenter info
    presenter_font = ImageFont.truetype(INFO_FONT, size=45)

    (left, top, right, bottom) = presenter_font.getbbox(presenter)
    _w = right - left
    draw.text(
        (padding + (content_width - _w) // 2 + 128, 748),
        presenter,
        font=presenter_font,
        fill="#ffffff",
        align="center",
    )

    if twitter:
        (left, top, right, bottom) = presenter_font.getbbox(presenter)
        _w = right - left
        draw.text(
            (padding + 768, 844),
            twitter,
            font=presenter_font,
            fill="#ffffff",
            align="center",
        )

    # right-top logo
    if project_logo != "":
        top_right_logo = convert_svg_to_png(project_logo, target_size=project_log_max_size)
        poster.paste(
            top_right_logo,
            (
                poster.width - 320 - (padding + top_right_logo.width // 2),
                padding + 20 - (top_right_logo.height // 2),
            ),
            top_right_logo,  # alpha mask
        )

    # Avatar
    if presenter_avatar != "":
        avatar_image = Image.open(presenter_avatar).convert("RGBA")
        avatar_image = avatar_image.resize((172, 172))
        # create avatar mask
        mask = Image.new("L", avatar_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + avatar_image.size, fill=255)

        # use mask on avatar
        rounded_avatar = ImageOps.fit(avatar_image, mask.size, centering=(0.5, 0.5))
        rounded_avatar.putalpha(mask)

        avatar_position = (590, 735)
        poster.paste(rounded_avatar, avatar_position, rounded_avatar)

    poster.save("./output/sharing_cover.png")
    # poster.show()
