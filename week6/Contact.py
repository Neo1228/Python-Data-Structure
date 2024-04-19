import sys

sys.stdin = open("input_3", "r")


def BFS(start):
    Queue = [start] #큐에 시작점을 리스트로 만들어서 할당
    Distance[start] = 0 # 시작점의 거리를 0으로 초기화

    while Queue:
        here = Queue.pop(0) #현재 위치를 큐의 첫번째 값으로 할당
        for next in myMap[here]:
            if Distance[next] == -1:
                Queue.append(next)
                Distance[next] = Distance[here] + 1
                #현재 맵에서 이동가능한 다음 위치를 next 함수에 할당하고 다음 위치의 거리가 -1 일때 큐에 다음 위치를 추가하고 다음 위치의 거리를 현재 위치거리 + 1로 할당

T = 10
for tc in range(1, T + 1):
    howmany, start = map(int, input().split()) #숫자의 개수, 시작 값
    Data = list(map(int, input().split()))# 데이터 리스트에 간선 추가
    myMap = [[] for _ in range(101)] # 100개의 빈 리스트를 만듬
    for i in range(0, len(Data), 2):
        _from, _to = Data[i], Data[i + 1]
        myMap[_from].append(_to) # 0부터 데이터 개수까지 데이터 리스트의 값을 2개씩 _from과 _to에 할당하고 myMap의 출발점에 목적점을 저장한다.

    Distance = [-1] * 101 # 거리 리스트를 -1로 101개 할당
    BFS(start)
    max = Distance[0] # 최대값을 거리 배열의 첫번째 값으로 초기화
    for i in range(len(Distance)):
        if Distance[i] >= max:
            max = Distance[i]
            ans = i #거리 배열의 크기 만큼 반복할때 최대값보다 거리 배열의 i번째 값이 더 클 경우에 최대값을 이 값으로 할당하고 ans 변수를 i로 할당한다.
    print(f'#{tc} {ans}')
