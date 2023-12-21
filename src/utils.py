import os
import qrcode
import cairosvg
from PIL import Image, ImageDraw, ImageFont


TMP_CONVERT_PNG = "./tmp/tmp_convert.png"
TITLE_FONT = "./font/Kollektif.ttf"


def is_svg_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == ".svg"


def convert_svg_to_png(file_path):
    if is_svg_file(file_path):
        cairosvg.svg2png(
            url=file_path,
            write_to=TMP_CONVERT_PNG,
        )
        image = Image.open(TMP_CONVERT_PNG).convert("RGBA")
    else:
        image = Image.open(file_path).convert("RGBA")
    return image


def auto_title_lines(txt: str, size:int, max_width: float, line_height: int = 30):
    txt_lines = []
    _tmp_line = []
    w = 0
    y = 0
    
    title_font = ImageFont.truetype(TITLE_FONT, size=int(size))

    if isinstance(txt, str):
        if "\n" in txt:
            arr = txt.split("\n")
        else:
            arr = txt.split()
        for _string in arr:
            (left, top, right, bottom) = title_font.getbbox(_string)
            _w = right - left
            if w + _w >= max_width:
                txt_lines.append((" ".join(_tmp_line), (max_width - w) / 2, y, title_font))
                w = 0
                y += bottom - top + line_height
                _tmp_line = []

            w += _w
            _tmp_line.append(_string)

            if _string == arr[-1]:
                txt_lines.append((" ".join(_tmp_line), (max_width - w) / 2, y, title_font))
    else:
        for _string_data in txt:
            title_font = ImageFont.truetype(TITLE_FONT, size=int(size * _string_data["size_scale"]))
            _string = _string_data["txt"]
            (left, top, right, bottom) = title_font.getbbox(_string)
            w = right - left
            txt_lines.append((_string, (max_width - w) / 2, y, title_font))
            y += bottom - top + line_height

    return txt_lines
