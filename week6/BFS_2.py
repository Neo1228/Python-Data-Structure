import sys

sys.stdin = open('input_2', 'r')


def BFS():
    while myQueue:
        here = myQueue.pop(0)
        Visited[here] = True
        print(here)
        for next in range(howmany + 1):
            if myMap[here][next] and not Visited[next]:
                myQueue.append(next)
                Visited[next] = True
                Parent[next] = here
                Distance[next] = Distance[here] + 1
        '''모든 정점을 돌면서 간선이 존재하는지 확인하면서 만약에 다음 점과 현재 점 사이의 간선이 존재하고 다음 점이 방문하지 않은 점인 경우
        큐에 다음 점을 추가하고 부모노드의 다음위치를 현재 위치로 할당하고, 거리노드의 다음위치를 현재 거리노드의 위치 +1 값으로 할당한다.'''


howmany, E = map(int, input().split())
myMap = [[0 for _ in range(howmany + 1)] for __ in range(howmany + 1)]
myQueue = []
Visited = [0] * (howmany + 1)
Parent = [0] * (howmany + 1)
Distance = [0] * (howmany + 1)
# 방문한 위치, 부모 노드, 거리 노드를 0으로 초기화
for _ in range(E):
    start, stop = map(int, input().split())
    myMap[start][stop] = 1
    myMap[stop][start] = 1
    # 간선 표시를 위한 반복문
myQueue.append(1)
Parent[1] = -1
# 부모노드 배열의 1번째 값을 -1로 할당
Distance[1] = 1
# 거리노드 배열의 1번째 값을 1로 할당
BFS()
print(Distance)
print(Parent)
