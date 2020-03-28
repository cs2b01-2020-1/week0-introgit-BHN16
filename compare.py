import os
import glob
import numpy as np

def comparacion(a, b):
    coincidence = 0
    size = None
    if(len(a) == len(b)):
        size = len(a)
    else:
        size = min(len(a), len(b))
    for i in range(0, size):
        if(a[i] == b[i]):
            coincidence += 1
    return round(((coincidence/size)*100),2)             
        
                

files = glob.glob(os.getcwd()+"/genomas/*.txt")
read = None
arr = None
size = None
for file in files:
    read = open(file, "r")
    arr = read.readlines()
    size = len(arr)
    chart = np.zeros((size,size))
    for i in range(1, size):
        for j in range(1, size):
            if(j != i):
                chart[i][j] = comparacion(arr[i], arr[j]) 
    arr.clear()
    read.close()
    print(chart)
