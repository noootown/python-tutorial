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
    for ptr in range(len(arr)):
        minPtr = ptr
        for i in range(ptr + 1, len(arr), 1):
            if arr[i] < arr[minPtr]:
                minPtr = i
        tmp = arr[minPtr]
        del arr[minPtr]
        arr.insert(ptr, tmp)
    return arr

def bubbleSort(arr):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

while 1:
    l = [int(ll) for ll in input('Please sort list: ').split(' ')]
    
    print('Selection Sort:')
    print(' '.join(selectionSort([str(ll) for ll in selectionSort(l)])))
    print('Insertion Sort:')
    print(' '.join(insertionSort([str(ll) for ll in insertionSort(l)])))
    print('Bubble Sort:')
    print(' '.join(bubbleSort([str(ll) for ll in bubbleSort(l)])))
    print('-------------------------------')

