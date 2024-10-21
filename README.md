# Daily_algo


# N과 M(2)
```
N, M = map(int, input().split())
path = []
visited = [False] * (N + 1)  # 중복없이

def dfs(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        if visited[i] == True: continue
        visited[i] = True
        path.append(i)
        dfs(i+1, level + 1)
        path.pop()
        visited[i] = False


dfs(1, 0)
```
# N과 M (4)
```
N, M = map(int, input().split())

path = []

def dfs(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        path.append(i)
        dfs(i, level+1)
        path.pop()


dfs(1, 0)
```
# N과 M (5)
```
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

path = []
visited = [False] * (N+1)
def dfs(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if visited[i] == True: continue
        visited[i] = True
        path.append(lst[i])
        dfs(level+1)
        path.pop()
        visited[i] = False

dfs(0)
```

# 헌내기는 친구가 필요해
```
from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
visited = [[False] * (M+1) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            start_i, start_j = i, j


def bfs():
    global cnt
    q = deque()
    q.append((start_i, start_j))
    visited[start_i][start_j] = True

    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False:
                if arr[ny][nx] == 'P':
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
                elif arr[ny][nx] == 'O':
                    visited[ny][nx] = True
                    q.append((ny, nx))

bfs()
print('TT' if cnt == 0 else cnt)
```
