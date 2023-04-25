def bubbleSort(arr):
    for i in range(len(arr)-1):
        for i in range(len(arr)-i-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

a = [4, 2, 3, 1]
print(a)

bubbleSort(a)
print(a)