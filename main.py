#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
import os

from app.Converter import Converter

if __name__ == "__main__":
    """
    这个脚本用于转换文本文件的编码
    有2种使用方式：
    1. 转换单个文件，需要输入[源文件名，目标文件名，源编码，目标编码]
    2. 转换一个文件夹,不会转换子文件夹，需要输入[源文件夹，目标文件夹，源编码，目标编码]
    """
    Converter().start_convert(source_path=os.path.join('storage', 'source'), source_encode='GB18030',
                              generate_path=os.path.join('storage', 'encoding_converter_generated'))
