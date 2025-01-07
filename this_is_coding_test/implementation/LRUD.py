n = int(input())
plans = input().split()
x, y = 1, 1

movements = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(4):
        if plan == movements[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)