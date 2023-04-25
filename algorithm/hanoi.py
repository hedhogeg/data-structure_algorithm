def hanoi(count, start, end, temp):
    # 원반의 개수, 시작위치, 목표위치, 이외 사용 가능한 위치
    if count == 0:
        return
    hanoi(count-1, start, temp, end)
    print(f'원반 {count} 을/를 {start} 에서 {end} 로 이동')
    hanoi(count-1, temp, end, start)


hanoi(4, 'A', 'C', 'B') 