def insertionSort(arr):
    for i in range(1, len(arr)):
        insert = arr[i]
        minimum = False
        for j in range(i-1, -1, -1):
            if arr[j] > insert:
                arr[j+1] = arr[j]
                if j == 0:
                    minimum = True
            else:
                break
        if minimum:
            arr[j] = insert
        else:
            arr[j+1] = insert
        print(arr)

a = [4, 1, 5, 3, 6, 2]
print(a)
insertionSort(a)
print(a)