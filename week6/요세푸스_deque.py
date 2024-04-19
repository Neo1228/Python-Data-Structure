from collections import deque

N, K = map(int,input().split()) #사람의 수, 뽑아야 되는 번째 수를 N, K에 할당
Queue = deque(range(1, N+1)) #큐에 1부터 N까지의 번호를 매긴 사람들을 deque로 할당한다.

print('<', end='')

while len(Queue) > 1:
    for _ in range(K-1):
        Queue.append(Queue.popleft())#큐 안에 사람이 한명이 존재할때까지 큐의 가장 왼쪽에 존재하는 수를 K-1번 뽑아서 큐의 마지막 위치에 추가한다.
    print(Queue.popleft(), end = ', ')#K-1번까지 뽑은 후에 K번째의 값을 뽑아서 출력
print(Queue.popleft(), end='') #큐 안에 남은 한명으 뽑아서 출력
print('>')