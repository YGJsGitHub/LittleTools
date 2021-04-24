# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# author:ygj time:2021/3/7


import os, datetime, re


def fileDateRename(rootpath):
    fileNameMatch(rootpath)
    files = os.listdir(mypath)

    for file in files:
        oldname = mypath + r'\\' + file
        t = datetime.datetime.fromtimestamp(os.path.getmtime(oldname)).date()
        newname = str(t) + '-' + file
        oldpath = os.path.join(mypath, file)
        newpath = os.path.join(mypath, newname)
        os.rename(oldpath, newpath)
        print(newpath)


def fileNameMatch(rootpath):
    pat = r"(\d{4}-\d{1,2}-\d{1,2})"
    files = os.listdir(mypath)

    for file in files:
        mat = re.search(pat, file)
        if mat:
            oldname = mypath + r'\\' + file
            t = datetime.datetime.fromtimestamp(os.path.getmtime(oldname)).date()
            newname = file.replace(mat.group(0) + '-', '')
            oldpath = os.path.join(mypath, file)
            newpath = os.path.join(mypath, newname)
            
            os.rename(oldpath, newpath)
            print(oldpath)
            print(newpath)
            print()

import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-p', dest='path', help='Target path')
args = parse.parse_args()
mypath = args.path


if __name__ == "__main__":
    if not mypath:
        print('Call this program with a parse')
    else:
        path = mypath
        fileDateRename(path)
