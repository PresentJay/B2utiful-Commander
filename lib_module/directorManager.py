import os.path
from lib_module.statics import IGNORE_FILES as ignore

""" DirectoryManager.py """
# Directory를 이용한 Function을 정의합니다.


""" Function getFiles """
# 특정 Directory의 File목록을 반환합니다.
# config의 IGNOREFILE_DEFAULT 목록을 무시합니다.
# (1) 첫 번째 매개변수로 기준 Directory를 결정합니다. (기본값 : 현재 폴더)
# (2) 두 번째 매개변수로 확장자를 결정합니다. (기본값 : 모든 파일)
# (3) 세 번째 매개변수로 절대경로/상대경로를 결정합니다. (기본값 : 절대경로)


def getFiles(_dir=os.getcwd(), extension="*", absolute=True):
    files = []
    for _file in os.listdir(_dir):  # (1)
        if _file in ignore:
            continue  # (2)
        if extension != "*" and _file.split(".")[1] != extension:
            continue  # (3)
        if absolute:
            _file = os.path.join(_dir, _file)
        files.append(_file)
    return files


def check_directory(dirname):
    current = "."
    for item in dirname.split("\\"):
        current += "\\" + item
        if os.path.exists(current) is False:
            os.mkdir(current)
            print("create directory > {}".format(current))