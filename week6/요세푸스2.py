Queue = []

peopleno = 41

for who in range(1, peopleno + 1):
    Queue.append(who)

while len(Queue) != 3:
    Queue.append(Queue.pop(0))
    Queue.append(Queue.pop(0))
    dead = Queue.pop(0)
print(Queue.pop(0), Queue.pop(0))
