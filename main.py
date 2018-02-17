#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*- coding: UTF-8 -*-
from app.converter import convert

if __name__ == "__main__":
    convert(source_path='storage/source', generate_path='storage/output', include_sub_file=True)
