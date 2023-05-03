def divide(arr, left, right):
    pivot = arr[left]
    left_start_idx = left+1
    right_start_idx = right
    while left_start_idx <= right_start_idx:
        while left_start_idx <= right and pivot >= arr[left_start_idx]:
            left_start_idx += 1
        
        while right_start_idx >= left+1 and pivot <= arr[right_start_idx]:
            right_start_idx -= 1

        if left_start_idx <= right_start_idx:
            arr[left_start_idx], arr[right_start_idx] = arr[right_start_idx], arr[left_start_idx]

    arr[left], arr[right_start_idx] = arr[right_start_idx], arr[left]

    return right_start_idx

def quickSort(arr, left, right):
    if left <= right:
        pivot = divide(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)

a = [2, 5, 4, 1, 6, 3, 8, 7]
print(a)
quickSort(a, 0, len(a)-1)
print(a)