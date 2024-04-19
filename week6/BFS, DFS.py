import sys

sys.stdin = open("input_1")


def DFS(here):
    visited[here] = True
    print(here, end=' ')  # end=' '는 줄바꿈을 못하게 만드는 변수
    for next in range(howmany + 1):
        if myMap[here][next] and not visited[next]:
            DFS(next)


def BFS(here):
    myQueue.append(here)
    # BFS함수를 실행하기 위해서 현재위치의 값을 큐에 추가한다.
    visited[here] = True
    # 현재위치를 방문한 위치로 설정한다
    while myQueue:
        here = myQueue.pop(0)
        print(here, end=' ')
        for next in range(howmany + 1):
            if myMap[here][next] and not visited[next]:
                myQueue.append(next)
                visited[next] = True


howmany, E, V = map(int, input().split())
myMap = [[0 for _ in range(howmany + 1)] for __ in range(howmany + 1)]
visited = [0] * (howmany + 1)

myQueue = []
for _ in range(E):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1
DFS(V)
print()
visited = [0] * (howmany + 1)
BFS(V)
