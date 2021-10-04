# encoding: utf-8

# library
import os
import shutil

def fileRemove(listFile: str or list):
    try:
        if type(listFile) == str:
            listFile = [listFile]

        for file in listFile:
            if os.path.exists(file):
                os.remove(file)
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False

def directoryRemove(listDirectory: str or list):
    try:
        if type(listDirectory) == str:
            listDirectory = [listDirectory]

        for directory in listDirectory:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False