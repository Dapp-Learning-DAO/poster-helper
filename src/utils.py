import os
import qrcode
import cairosvg
from PIL import Image, ImageDraw, ImageFont


TMP_CONVERT_PNG = "./tmp/tmp_convert.png"
TITLE_FONT = "./font/SourceHanSansCN-Bold.otf"


def is_svg_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == ".svg"


def convert_svg_to_png(file_path, target_size=None):
    """
    转换SVG到PNG
    
    Args:
        file_path: SVG文件路径
        target_size: 目标尺寸(width, height)，如果提供则自动计算缩放比例
    """
    if is_svg_file(file_path):
        if target_size:
            # 获取SVG原始尺寸并计算缩放比例
            import xml.etree.ElementTree as ET
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # 尝试从SVG中获取width和height
            width = root.get('width')
            height = root.get('height')
            
            if width and height:
                # 移除可能的单位（如px, pt等）
                import re
                width_match = re.search(r'[\d.]+', width)
                height_match = re.search(r'[\d.]+', height)
                
                if width_match and height_match:
                    original_width = float(width_match.group())
                    original_height = float(height_match.group())
                    
                    target_width, target_height = target_size
                    
                    # 计算缩放比例，保持长宽比
                    scale_x = target_width / original_width
                    scale_y = target_height / original_height
                    scale = min(scale_x, scale_y)  # 使用较小的缩放比例保持长宽比
                    
                    output_width = int(original_width * scale)
                    output_height = int(original_height * scale)
                    
                    cairosvg.svg2png(
                        url=file_path,
                        write_to=TMP_CONVERT_PNG,
                        output_width=output_width,
                        output_height=output_height,
                    )
                else:
                    # 无法解析尺寸，使用默认转换
                    cairosvg.svg2png(
                        url=file_path,
                        write_to=TMP_CONVERT_PNG,
                    )
            else:
                # 无法获取尺寸，使用默认转换
                cairosvg.svg2png(
                    url=file_path,
                    write_to=TMP_CONVERT_PNG,
                )
        else:
            cairosvg.svg2png(
                url=file_path,
                write_to=TMP_CONVERT_PNG,
            )
        image = Image.open(TMP_CONVERT_PNG).convert("RGBA")
    else:
        image = Image.open(file_path).convert("RGBA")
        if target_size:
            # 对于非SVG图片，计算缩放比例
            target_width, target_height = target_size
            scale_x = target_width / image.width
            scale_y = target_height / image.height
            scale = min(scale_x, scale_y)  # 保持长宽比
            
            new_width = int(image.width * scale)
            new_height = int(image.height * scale)
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
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
