from collections import deque


def BFS(map, start, end):
    row = len(map) #행의 개수
    col = len(map[0]) #열의 개수
    visited = [[False] * col for _ in range(row)] #방문한 점을 모두 0으로 초기화
    visited[start[0]][start[1]] = True #시작점을 방문한 점으로 초기화
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start[0], start[1], 1)]) #큐에 [0, 0, 1]리스트를 추가

    while queue:
        X, Y, count = queue.pop() #x, y, count의 값을 큐의 0, 1, 2번째 값으로 할당
        if (X, Y) == end:
            return count#x, y좌표가 도착지점에 도달하면 움직인 수를 반환
        for i in range(4):
            dx_1, dy_1 = X + dx[i], Y + dy[i] # 다음 x좌표와 다음 y좌표를 상하좌우의 좌표로 할당
            if 0 <= dx_1 < row and 0 <= dy_1 < col and map[dx_1][dy_1] == 1 and not visited[dx_1][dy_1]:
                visited[dx_1][dy_1] = True
                queue.append((dx_1, dy_1, count + 1))
                # 다음 x좌표와 y좌표가 행렬의 범위를 나가지 않고 안에서 존재하며 맵에 간선이 존재하며 방문하지 않은 점인 경우에 방문한 점으로 초기화하고 큐에 이 값들을 추가


def ans(N, M, map):
    start = (0, 0)
    end = (N - 1, M - 1)
    return BFS(map, start, end)


N, M = map(int, input().split())# N 행의 개수, M 열의 개수
myMap = []
for _ in range(N):
    myMap.append(list(map(int, input()))) # 행의 개수 만큼 리스트를 만들어서 빈 맵에 추가한다.

print(ans(N, M, myMap))
