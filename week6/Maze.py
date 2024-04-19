import sys
sys.stdin = open("input", "r")
from collections import deque


def BFS(map, start, end):
    row = len(map) #map의 행의 개수
    col = len(map[0]) #map의 열의 개수
    visited = [[False] * col for _ in range(row)] #행의 개수만큼 반복하여 0으로 열에 0으로 모두 초기화하여 map을 만든다.
    visited[start[0]][start[1]] = True #시작 지점인 visited[0][0]을 방문한 점으로 초기화한다.
    dx = [-1, 1, 0, 0] #상하좌우 입력
    dy = [0, 0, -1, 1]
    queue = deque([(start[0], start[1], 1)])
    #큐에 deque[0, 0, 1] 리스트를 할당한다. 이러한 이유로는 큐에 다음으로 움직일 좌표를 찾는 반복문을 수행할때 초기 x, y, count가 필요하므로 이 값을 큐스택에 넣는다.

    while queue:
        X, Y, count = queue.pop() #X, Y, count(움직인 횟수)에 첫번째 값을 할당한다.
        if (X, Y) == end: #X, Y가 목적지값과 동일하면 움직인 횟수를 반환한다.
            return count
        for i in range(4):
            dx_1, dy_1 = X + dx[i], Y + dy[i] #다음 x좌표와 y좌표를 상하좌우로 움직인 좌표로 할당한다.
            if 0 <= dx_1 < row and 0 <= dy_1 < col and map[dx_1][dy_1] == 1 and not visited[dx_1][dy_1]:
                # 다음 x좌표와 y좌표가 0보다 크고 행과 열보다 작으며, 이 좌표가 장애물이 존재하지 않고 방문하지 않음 좌표일 경우에
                visited[dx_1][dy_1] = True # 다음 x,y 좌표를 방문한 점으로 초기화한다.
                queue.append((dx_1, dy_1, count + 1)) #큐스택에 (다음 x, y좌표, 횟수 + 1)을 추가한다.


def ans(N, M, map):
    start = (0, 0) #처음 출발점
    end = (N - 1, M - 1) #도착지점
    return BFS(map, start, end) #BFS함수에 맵과 출발점, 도착지점의 값을 반환한다.


N, M = map(int, input().split())
myMap = [] #맵을 빈 리스트로 초기화한다.
for _ in range(N):
    myMap.append(list(map(int, input())))
    #행의 개수만큼 반복하면서 비어있는 맵에 열의 리스트 값을 추가한다.

          #열
    '''****** 행
       ******
       ******'''

print(ans(N, M, myMap))
