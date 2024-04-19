from collections import deque

myQueue = deque([10,20,30])
myQueue.append(40)
myQueue.appendleft(50)

print(myQueue)
print(myQueue.pop())
print(myQueue.popleft()) #dequeue랑 Queue = []

for now in range(1,4):
    myQueue.append(now)
print(myQueue)

'''while myQueue:
    print(myQueue.pop(0)) #queue'''