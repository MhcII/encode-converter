#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
import os

from app.ConverterKernel import ConverterKernel


class Converter:
    """
    要转换的内容分为如下几种情况
    [!重要]源地址和目标地址不能相同的，无论是文件还是文件夹

    如果不指定源格式，源格式则为gbk，如果不指定目标格式，目标格式则为utf-8
    如果不指定目标文件夹，则为encoding_converter_generated文件夹
    如果不指定源文件夹，则为source文件夹

    文件
    直接生成就行啦
    检测源文件是否存在
    监测目标文件是否可写
    文件夹
    是否 遍历子文件夹

    """

    def __init__(self, source_path: str = 'storage/source', source_encode: str = 'GBK',
                 generate_path: str = 'storage/encoding_converter_generated', generate_encode: str = 'UTF-8',
                 include_sub_file: bool = False):
        self.__source_path = source_path
        self.__source_encode = source_encode
        self.__generate_path = generate_path
        self.__generate_encode = generate_encode
        self.__include_sub_file = include_sub_file

    def convert(self):
        if os.path.isdir(self.__source_path):
            self.__convert_file()
        else:
            self.__convert_folder()

    def __convert_file(self):
        pass
        ConverterKernel.start_convert(source_path=self.__source_path, source_encode=self.__source_encode,
                                      generate_path=self.__generate_path, generate_encode=self.__generate_encode)

    def __convert_folder(self):
        # 对所有子文件进行转换
        for filename in os.listdir(self.__source_path):
            if os.path.isfile(os.path.join(self.__source_path, filename)):
                # 进行转码
                # 如果 generate_path 指定了，则把文件名加入 generate_path
                generate_path = self.__generate_path if (self.__generate_path is None) else os.path.join(
                    self.__generate_path, filename)
                ConverterKernel.start_convert(source_path=os.path.join(self.__source_path, filename),
                                              source_encode=self.__source_encode, generate_path=generate_path,
                                              generate_encode=self.__generate_encode)
            else:
                # 如果还是目录，我可不知道咋整了
                pass
