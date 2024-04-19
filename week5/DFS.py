import sys
sys.stdin = open("input.txt")
def DFS(here):
    Visited[here] = True
    #방문한 적이 있는 점을 True로 할당
    print(here)
    #현재 위치 출력
    for next in range(1, howmany+1):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)
    #다음 점을 1부터 howmany+1까지 MyMap에서 값이 비어있지않고 방문하지 않았을 경우 다음 점으로 DFS함수를 재귀

howmany, E = map(int, input().split())
#정점의 개수, 길의 개수 입력
MyMap = [[0 for _ in range(howmany + 1)] for __ in range (howmany + 1)]
#2중 for문으로 정점의 개수 만큼 (howmany+1)*(howmany+1) 맵을 만들어서 초기화
Visited = [0]*(howmany+1)
#방문한 적이 있는 길의 함수를 0으로 초기화

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1
    #입력받은 시작점과 끝점 사이의 간선을 표시

DFS(1)
print(MyMap)