import numpy as np

def normal_sort(arr):
    offset = 1
    while (len(arr)-offset > 2):
        for i in range(len(arr)-offset):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                err+=1
            offset+=1
    return arr

def normal_sort(arr):
    offset = 1
    while (len(arr)-offset > 2):
        for i in range(len(arr)-offset):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                err+=1
            offset+=1
    return arr