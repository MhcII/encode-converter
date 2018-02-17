#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
import os


def convert(source_path: str = '../storage/source', source_encode: str = 'GB18030',
            generate_path: str = '../storage/output', generate_encode: str = 'UTF-8', include_sub_file: bool = False):
    if not os.path.exists(source_path):
        raise ValueError('无效的路径: "%s"' % source_path)
    elif os.path.abspath(source_path) == os.path.abspath(generate_path):
        raise ValueError('源目录和输出目录不能相同')
    # 如果输出位置是一个文件夹，则删除
    if os.path.exists(generate_path):
        if os.path.isfile(generate_path):
            os.remove(generate_path)
            os.makedirs(generate_path)
    else:
        os.makedirs(generate_path)
    # 进行转换
    if os.path.isfile(source_path):
        __convert_one_file(source_path, source_encode, generate_path, generate_encode)
    elif os.path.isdir(source_path):
        __convert_folder(source_path, source_encode, generate_path, generate_encode, include_sub_file)


def __convert_one_file(source_path, source_encode, generate_path, generate_encode):
    with open(file=generate_path, mode='w', encoding=generate_encode) as generate_file:
        with open(file=source_path, mode='r', encoding=source_encode) as source_file:
            for line_text in source_file:
                # 每读取一行，转码后放入新文件中
                generate_file.write(line_text)


def __convert_folder(source_path, source_encode, generate_path, generate_encode, include_sub_file):
    if not os.path.exists(generate_path):
        os.makedirs(generate_path)
    # 对子文件转码
    for file in __find_txt_file(source_path):
        print('正在转换: %s' % file)
        __convert_one_file(os.path.join(source_path, file), source_encode, os.path.join(generate_path, file),
                           generate_encode)
    # 如果包括子目录，则对子目录也进行转码
    if include_sub_file:
        for folder in __find_sub_folder(source_path):
            __convert_folder(os.path.join(source_path, folder), source_encode, os.path.join(generate_path, folder),
                             generate_encode, include_sub_file)


def __find_txt_file(path):
    return filter(lambda x: x.endswith('.txt'), os.listdir(path))


def __find_sub_folder(path):
    return filter(lambda x: os.path.isdir(os.path.join(path, x)), os.listdir(path))
