N, K = map(int,input().split())

Queue = list(range(1, K+1))
#자리 순서를 매기는 리스트를 큐에 할당

print('<', end='')

while len(Queue) > 1: #사람이 한명 남을 때까지 반복
    for _ in range(K-1):
        Queue.append(Queue.pop(0))
        #K번째 사람 이전까지의 사람들을 큐의 마지막으로 옮긴다.
    print(Queue.pop(0), end = ', ')
    #K번째 사람을 제거하고 출력한다.
print(Queue.pop(0), end='')
#마지막으로 남은 사람을 뽑아서 출력
print('>')