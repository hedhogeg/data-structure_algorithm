def countBoard(board):
    B_row = 'BWBWBWBW'
    W_row = 'WBWBWBWB'

    step = 0
    count_B = 0
    count_W = 0
    for row in board:
        for c, b in zip(row, B_row):
            if c != b:
                if step % 2 == 0:
                    count_B += 1
                else:
                    count_W += 1
        
        for c, w in zip(row, W_row):
            if c != w:
                if step % 2 == 0:
                    count_W += 1
                else:
                    count_B += 1
        step += 1

    counted = count_B if count_B < count_W else count_W

    return counted

N, M = map(int, input().split())

board = []
for _ in range(N):
    row = input()
    board.append(row)

min = 64
for i in range(N-7):
    for j in range(M-7):
        current_board = board[i:i+8]
        for idx, row in enumerate(current_board):
            current_board[idx] = row[j:j+8]
        current_counted = countBoard(current_board)
        if min > current_counted:
            min = current_counted

print(min)