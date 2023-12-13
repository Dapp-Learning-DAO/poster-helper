import os
import qrcode
import cairosvg
from PIL import Image, ImageDraw, ImageFont


TMP_CONVERT_PNG = "./tmp/tmp_convert.png"
BG_COLOR = "#101E3F"


def is_svg_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == ".svg"


def convert_svg_to_png(file_path, bg_color=BG_COLOR):
    if is_svg_file(file_path):
        cairosvg.svg2png(
            url=file_path,
            write_to=TMP_CONVERT_PNG,
            background_color=bg_color,
        )
        image = Image.open(TMP_CONVERT_PNG).convert("RGBA")
    else:
        image = Image.open(file_path).convert("RGBA")
    return image


def auto_title_lines(txt: str, font: float, max_width: float, line_height: int = 30):
    txt_lines = []
    _tmp_line = []
    w = 0
    y = 0
    arr = txt.split()
    for _string in arr:
        (left, top, right, bottom) = font.getbbox(_string)
        _w = right - left
        if w + _w >= max_width:
            txt_lines.append((" ".join(_tmp_line), (max_width - w) / 2, y))
            w = 0
            y += bottom - top + line_height
            _tmp_line = []

        w += _w
        _tmp_line.append(_string)

        if _string == arr[-1]:
            txt_lines.append((" ".join(_tmp_line), (max_width - w) / 2, y))

    return txt_lines
