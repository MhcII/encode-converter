#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
from src.converter import convert
import sys

if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else None
    source_encode = sys.argv[2] if len(sys.argv) > 2 else None
    target_encode = sys.argv[3] if len(sys.argv) > 3 else None
    convert(source=source, generate='target.txt', source_encode=source_encode, generate_encode=target_encode)
