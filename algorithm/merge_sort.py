def merge(arr, left_idx, mid_idx, right_idx):
    left_area_idx = left_idx
    right_area_idx = mid_idx+1
    arr_temp = [0] * len(arr)
    temp_idx = left_idx
    while left_area_idx <= mid_idx and right_area_idx <= right_idx:
        if arr[left_area_idx] <= arr[right_area_idx]:
            arr_temp[temp_idx] = arr[left_area_idx]
            left_area_idx += 1
        else:
            arr_temp[temp_idx] = arr[right_area_idx]
            right_area_idx += 1
        temp_idx += 1

    if left_area_idx > mid_idx:
        for i in range(right_area_idx, right_idx+1):
            arr_temp[temp_idx] = arr[i]
            temp_idx += 1
    else:
        for i in range(left_area_idx, mid_idx+1):
            arr_temp[temp_idx] = arr[i]
            temp_idx += 1
    
    for i in range(left_idx, right_idx+1):
        arr[i] = arr_temp[i]

def mergeSort(arr, left_idx, right_idx):
    if left_idx < right_idx:
        mid_idx = int((left_idx+right_idx)/2)
        mergeSort(arr, left_idx, mid_idx)
        mergeSort(arr, mid_idx+1, right_idx)
        merge(arr, left_idx, mid_idx, right_idx)

        
a = [3, 5, 2, 4, 1, 7, 8, 6]
print(a)
mergeSort(a, 0, 7)
print(a)