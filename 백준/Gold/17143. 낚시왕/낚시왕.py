import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    board[x-1][y-1].append([s, d-1, z])
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 낚시왕이 상어 잡음
def catch(y, board):
    answer = 0      # 잡은 물고기 크기
    for i in range(r):
        if board[i][y]:     # 땅과 제일 가까운 상어
            answer = board[i][y][0][2]
            board[i][y] = []
            break
    return answer, board

# 상어 이동
def move(board):
    # 상어가 이동한 임시배열
    temp = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                x, y = i, j
                s, d, z = board[i][j][0]
                dis = s     # 거리
                while dis:      # 속력만큼 이동할 때까지
                    x, y = x+dx[d], y+dy[d]
                    # 범위 안에서는 거리 1씩 이동
                    if 0 <= x < r and 0 <= y < c:
                        dis -= 1
                    # 범위 벗어나면 다시 빼주고 방향 전환
                    else:
                        x, y = x-dx[d], y-dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                temp[x][y].append([s,d,z])      # 최종위치 업데이트
    for i in range(r):
        for j in range(c):
            # 2개 이상의 상어가 한 칸에 있으면 제일 큰 상어만 남기기
            if len(temp[i][j]) >= 2:
                temp[i][j].sort(key=lambda x: x[2], reverse=True)
                s, d, z = temp[i][j][0]
                temp[i][j] = [[s, d, z]]
    return temp

shark = 0       # 잡은 상어 크기
for i in range(c):
    eat, board = catch(i, board)
    shark += eat
    board = move(board)

print(shark)