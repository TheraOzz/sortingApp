from menu import *


def partition(start, end, randomList, option):
    pivot_index = start
    pivot = randomList[pivot_index].sortBy(option)
    while start < end:
        while start < len(randomList) and randomList[start].sortBy(option) <= pivot:
            start += 1
        while randomList[end].sortBy(option) > pivot:
            end -= 1
        if start < end:
            randomList[start], randomList[end] = randomList[end], randomList[start]
    randomList[end], randomList[pivot_index] = randomList[pivot_index], randomList[end]
    return end


def quickSort(start, end, randomList, option):
    if start < end:
        p = partition(start, end, randomList, option)
        quickSort(start, p-1, randomList, option)
        quickSort(p+1, end, randomList, option)


def bubbleSort(randomList, option):
    n = len(randomList)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if randomList[j].sortBy(option) > randomList[j+1].sortBy(option):
                randomList[j], randomList[j+1] = randomList[j+1], randomList[j]


def bucketSort(randomList, option):
    bucket = []
    for i in range(7):
        bucket.append([])
    for j in randomList:
        index_b = j.sortBy(option)
        bucket[index_b].append(j)
    k = 0
    for i in range(len(bucket)):
        for j in bucket[i]:
            randomList[k] = j
            k +=1


def readTshirts(TshirtList):
    """function for read/view T-shirt list"""
    if len(TshirtList) == 0:
        print(Colors.WARNING + ">> list is empty!" + Colors.ENDC) 
    else:
        for tshirt in TshirtList:
            print(tshirt)

