import numpy as np
import time as tm
import backcall

#None of Libraries are necessary

def callbackFunc(s):
    print('Length of the text file is : ', s)

def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    printFileLength("/storage/emulated/0/Python/sample.txt", callbackFunc)
    #File Path