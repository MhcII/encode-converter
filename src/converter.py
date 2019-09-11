#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
import os


def format_path(source, generate):
    if not source:
        raise ValueError('目标文件 "%s" 无效！' % source)
    elif not os.path.exists(source):
        raise ValueError('源文件 "%s" 不存在！' % source)
    elif not generate:
        raise ValueError('目标文件 "%s" 无效！' % generate)
    elif os.path.abspath(source) == os.path.abspath(generate):
        raise ValueError('源文件和目标文件不能相同！')
    return os.path.abspath(source), os.path.abspath(generate)


def format_encode(source, generate):
    source = source if source else 'GB18030'
    generate = generate if generate else 'UTF-8'
    return source, generate


def convert_file(source, generate, source_encode, generate_encode):
    with open(file=generate, mode='w', encoding=generate_encode) as generate_file:
        with open(file=source, mode='r', encoding=source_encode) as source_file:
            for line_content in source_file:
                # 每读取一行，转码后放入新文件中
                generate_file.write(line_content)


def convert(source, generate, source_encode='GB18030', generate_encode='UTF-8'):
    source, generate = format_path(source, generate)
    source_encode, generate_encode = format_encode(source_encode, generate_encode)
    convert_file(source, generate, source_encode, generate_encode)
