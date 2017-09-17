def insertionSort(arr):
    n=len(arr)
    if n == 1:
        return arr
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minPtr = i
        for j in range(i+1, n):
            if arr[j] < arr[minPtr]:
                minPtr = j
        arr[i], arr[minPtr] = arr[minPtr], arr[i]
    
    return arr

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

while 1:
    l = [int(ll) for ll in input('Please sort list: ').split(' ')]
    
    print('Selection Sort:')
    print(' '.join([str(ll) for ll in selectionSort(list(l))]))
    print('Insertion Sort:')
    print(' '.join([str(ll) for ll in insertionSort(list(l))]))
    print('Bubble Sort:')
    print(' '.join([str(ll) for ll in bubbleSort(list(l))]))
    print('-------------------------------')

