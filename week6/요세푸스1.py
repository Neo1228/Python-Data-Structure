Queue = []

peopleno = 41

for who in range(1, peopleno + 1):
    Queue.append(who)
    #사람의 수를 1부터 41까지로 부여하고 큐에 추가

while len(Queue) != 3:
    #큐 안에 있는 개수가 3개가 아닌 경우에
    alive1 = Queue.pop(0) #살아있는 첫번째 사람을 큐에서 뽑아서 할당
    alive2 = Queue.pop(0) #살아있는 두번째 사람을 큐에서 뽑아서 할당
    dead = Queue.pop(0) #죽은 사람을 큐에서 뽑아서 할당
    Queue.append(alive1) #살아있는 사람을 큐에 다시 추가
    Queue.append(alive2) #살아있는 사람을 큐에 다시 추가

print(Queue.pop(0), Queue.pop(0)) #큐에 남아있는 사람 두명을 출력한다.
