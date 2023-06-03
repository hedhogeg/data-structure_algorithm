T = int(input())

def split(arr, result):
    if len(arr) == 1:
        return result
    if result:
        mid = len(arr) // 2
        left = arr[0:mid]
        right = arr[-1:mid:-1]
        split_mid = len(left) // 2
        if left[split_mid] == right[split_mid]:
            result = False
            return result
        else:
            no = False
            for i in range(len(left)):
                if left[i] == right[i]:
                    no = True
                    break
            if no:
                result = False
            else:
                if len(left) == 1:
                    return result
                else:
                    result1, result2 = split(left, result), split(right, result)
                    if result1 == True and result2 == True:
                        return True
                    else:
                        return False
    else:
        return result

result_list = []
for _ in range(T):
    paper_str = input()
    paper = []
    for c in paper_str:
        paper.append(int(c))

    result = True
    result = split(paper, result)
    if result:
        result_list.append('YES')
    else:
        result_list.append('NO')

for r in result_list:
    print(r)