import sys

sys.stdin = open("input_2")


def DFS(graph, start, end, visited):
    visited[start] = True
    # 처음 시작값을 이미 방문한 길로 만듬

    if start == end:
        return True
    # 시작점과 마지막점이 서로 동일하다면 True로 반환한다.
    for next in graph[start]:
        if not visited[next]:
            if DFS(graph, next, end, visited):
                return True
    # 다음점이 방문하지 않은 점이라면 그 다음점을 DFS로 반환해서 만족하는지 확인한다.
    return False


T = 10
for i in range(1, T + 1):
    tc, howmany = map(int, input().split())
    # 테스트 케이스 번호와 길의 개수 입력받기
    graph = [[] for _ in range(100)]
    # graph를 빈 그래프로 초기화
    road = list(map(int, input().split()))
    # 서로 연결된 길의 번호 입력받기
    for i in range(0, len(road), 2):
        graph[road[i]].append(road[i + 1])
        # 길을 순서쌍으로 입력받아서 짝지어줘야 하므로 i의 범위를 2개씩 받아서 묶어준다. 그리고 그래프의 정점에 대응하는 이어지는 길을 배열에 대응되게 값을 추가해준다.
    visited = [False] * 100
    # 방문한 길을 100개의 False로 초기화해준다.
    if DFS(graph, 0, 99, visited):
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
