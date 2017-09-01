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

    def __init__(self, source_path: str = os.path.join('storage', 'source'), source_encode: str = 'GBK',
                 generate_path: str = os.path.join('storage', 'encoding_converter_generated'),
                 generate_encode: str = 'UTF-8', include_sub_file: bool = False):
        self.__source_path = source_path
        self.__source_encode = source_encode
        self.__generate_path = generate_path
        self.__generate_encode = generate_encode
        self.__include_sub_file = include_sub_file

    def convert(self):
        # 检测路径是否存在
        self.__check_source_path()
        self.__check_generate_folder()
        # 判断要转换的是文件夹还是文件，执行不同的流程
        if os.path.isdir(self.__source_path):
            self.__convert_folder()
        else:
            self.__convert_file()

    def __convert_file(self):
        ConverterKernel.start_convert(source_path=self.__source_path, source_encode=self.__source_encode,
                                      generate_path=os.path.join(self.__generate_path,
                                                                 os.path.basename(self.__source_path)),
                                      generate_encode=self.__generate_encode)

    def __convert_folder(self):
        # 对所有子文件进行转换
        for filename in os.listdir(self.__source_path):
            if os.path.isfile(os.path.join(self.__source_path, filename)):
                # 进行转码
                ConverterKernel.start_convert(source_path=os.path.join(self.__source_path, filename),
                                              source_encode=self.__source_encode,
                                              generate_path=os.path.join(self.__generate_path, filename),
                                              generate_encode=self.__generate_encode)
            else:
                # 如果还是目录，我可不知道咋整了
                pass

    def __check_source_path(self):
        if not os.path.exists(self.__source_path):
            raise Exception('源地址不存在')

    def __check_generate_folder(self):
        if not os.path.exists(self.__generate_path):
            os.mkdir(self.__generate_path)

    @staticmethod
    def start_convert(source_path: str = os.path.join('storage', 'source'), source_encode: str = 'GBK',
                      generate_path: str = os.path.join('storage', 'encoding_converter_generated'),
                      generate_encode: str = 'UTF-8', include_sub_file: bool = False):
        Converter(source_path, source_encode, generate_path, generate_encode, include_sub_file).convert()
