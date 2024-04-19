"""import sys

sys.stdin = open("input_2.txt", "r")"""

a, b = map(int, input().split()) #경찰관 위치, 좀비 위치
ability = [0] * 3 #능력 3개를 0으로 초기화
ability[0], ability[1], ability[2] = map(int, input().split()) # 능력 3개의 능력값을 입력받는다.
Queue = [] #스택을 초기화

Time = [987654321] * 1000 # 시간리스트에 충분히 큰 수를 할당한다.


def BFS():
    while Queue:
        here = Queue.pop(0) #현재 위치를 큐에서 뽑아낸다.
        for i in range(3):
            next = here + ability[i] #능력 3개를 반복해서 사용하며 다음 위치를 각 능력에 따른 위치로 할당
            if next > len(Time) - 1: continue # 다음 위치가 시간의 최대값보다 클 경우에 건너뛰고 계속한다.
            if Time[next] > Time[here] + 1:
                Time[next] = Time[here] + 1
                Queue.append(next) #다음 위치의 시간이 현재 위치의 시간 + 1보다 클 경우에 갱신하고 큐에 다음 위치를 추가




Time[a] = 0 #경찰 위치의 시간을 0으로 초기화한다.
Queue.append(a) #큐에 경찰 위치를 추가
BFS() #BFS실행

if (Time[b] != 987654321):
    print(Time[b]) # 좀비의 시간이 충분히 큰 값이 아닌 경우에 좀비의 시간을 출력한다.
else:
    print(-1) # 아닌 경우에 -1을 출력한다.