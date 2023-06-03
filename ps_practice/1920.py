N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
check_nums = list(map(int, input().split()))

def search(num, arr):
    start = 0
    end = N-1
    while True:
        mid = int((start+end) / 2)
        if num < arr[mid]:
            if start > end:
                result = 0
                break
            end = mid-1
        elif num > arr[mid]:
            if start > end:
                result = 0
                break
            start = mid+1
        else:
            result = 1
            break

    return result

r_list = []
for num in check_nums:
    r_list.append(search(num, nums))

for r in r_list:
    print(r)
