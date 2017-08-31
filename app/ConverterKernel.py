#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-


class ConverterKernel:
    """
    这个类能对一个文件进行编码转换
    """

    def __init__(self, source_path: str, source_encode: str, generate_path: str, generate_encode: str):
        self.__source_path = source_path
        self.__source_encode = source_encode
        self.__generate_path = generate_path
        self.__generate_encode = generate_encode

    def convert(self):
        # 打开写入文件
        generate_file = open(file=self.__generate_path, mode='a+', encoding=self.__generate_encode)
        # 打开源文件，循环读入每一行
        try:
            with open(file=self.__source_path, mode='r', encoding=self.__source_encode) as source_file:
                for text in source_file:
                    # 每读取一行，转码后放入新文件中
                    generate_file.write(text)
        finally:
            # 写入完毕后关闭新文件
            generate_file.close()

    @staticmethod
    def start_convert(source_path: str, source_encode: str, generate_path: str, generate_encode: str):
        ConverterKernel(source_path, source_encode, generate_path, generate_encode).convert()
