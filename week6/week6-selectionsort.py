while 1:
    s = input('list? ')
    arr = s.split(' ')
    for ptr in range(len(arr)):
        minPtr = ptr
        for i in range(ptr + 1, len(arr), 1):
            if arr[i] < arr[minPtr]:
                minPtr = i
        tmp = arr[minPtr]
        del arr[minPtr]
        arr.insert(ptr, tmp)
    print(arr)

