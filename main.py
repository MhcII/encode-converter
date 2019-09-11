#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
import os
from src.converter import convert
import sys


def generate_name(file):
    if not source:
        return None
    file_name, ext = os.path.splitext(file)
    return '%s_converted%s' % (file_name, ext)


if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else None
    source_encode = sys.argv[2] if len(sys.argv) > 2 else None
    target_encode = sys.argv[3] if len(sys.argv) > 3 else None
    #
    convert(source=source, generate=generate_name(source), source_encode=source_encode, generate_encode=target_encode)
