# 미로탐색
from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(N)]

dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        y, x = q.popleft()

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                q.append((ny, nx))
                arr[ny][nx] = arr[y][x] + 1

bfs(0, 0)
print(arr[N-1][M-1])

# 유기농 배추

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

dir = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        y, x = q.popleft()

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append((ny, nx))


for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # M이 가로(열) N이 세로(행) K는 배추 위치의 개수
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                bfs(i, j)
    print(cnt)



# 치킨 배달

# 1. itertools combination 사용
from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
houses = []  # 집
chickens = [] # 치킨집

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))
        elif arr[i][j] == 1:
            houses.append((i, j))

for chicken in combinations(chickens, M):
    temp = 0  # 치킨거리 초기화
    for house in houses:
        chicken_len = float('inf')
        for j in range(M):
            chicken_len = min(chicken_len, abs(house[0] - chicken[j][0]) + abs(house[1] - chicken[j][1]))
        temp += chicken_len
    result = min(result, temp)


print(result)




# 2. 재귀 dfs로 combinations 구현


import sys
input = sys.stdin.readline


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
houses = []  # 집
chickens = [] # 치킨집

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chickens.append((i, j))  # 치킨집 좌표 저장
        elif arr[i][j] == 1:
            houses.append((i, j))    # 집 좌표 저장

def dfs(start, path):
    global result
    if len(path) == M:  # 뽑은 치킨집 개수가 최대 개수인 M에 도달하면
        temp = 0  # 구하는 치킨거리를 저장하는 변수 temp 초기화
        for house in houses:  # 각 집에 대해
            chicken_len = float('inf')  # 집과 치킨집 사이의 거리 초기화
            for chicken in path: # 내가 고른 치킨집 들 중 하나랑
                # 집과 치킨간 거리를 계산해서 더 작은 걸로 새로 저장함
                chicken_len = min(chicken_len,  abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
            temp += chicken_len # 그걸 계속 더해줌
        result = min(result, temp)  # 결과를 계속 최소거리로 업데이트
        return  # 다 수행했으면 돌아가기

    for i in range(start, len(chickens)):  # 치킨집들 중 가게를 뽑아서
        dfs(i+1, path + [chickens[i]])     # path에 더해서 재귀 호출

dfs(0, [])  # 아무것도 없는 빈 리스트 path로 시작

print(result)