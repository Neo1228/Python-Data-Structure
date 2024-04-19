import sys

sys.stdin = open('input_2', 'r')


def BFS():
    while myQueue:  # myQueue가 존재할 때까지 반복
        here = myQueue.pop(0)  # 현재 위치를 myQueue의 첫번째 값으로 할당
        Visited[here] = True  # 현재 위치를 방문한 점으로 만듬
        print(here)
        for next in range(howmany + 1):  # 모든 점을 돌면서 간선 여부를 확인
            if myMap[here][next] and not Visited[next]:
                myQueue.append(next)
                Visited[next] = True
                # TODO 맵의 현재위치와 다음위치 간의 간선이 존재하고 다음 위치가 방문하지 않은 점인 경우에 큐에 다음 위치를 추가하고 다음 위치를 방문한 점으로 만듬


howmany, E = map(int, input().split())  # 정점, 간선의 개수
myMap = [[0 for _ in range(howmany + 1)] for __ in range(howmany + 1)]  # myMap을 0으로 초기화
myQueue = []  # myQueue를 빈 배열로 초기화
Visited = [0] * (howmany + 1)  # 방문한 점을 0으로 초기화

for _ in range(E):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1
    # start, stop 좌표 사이의 간선을 표시

myQueue.append(1)
# myQueue를 시작하기 위해서 1을 추가
BFS()
