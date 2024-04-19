'''import sys
sys.stdin = open("input.txt", "r")'''

def GetSome(here):
    if here > Zombie: return #현재 위치가 좀비보다 클 경우에 반환
    for i in range(3):
        next = here + ability[i]
        if Time[next] > Time[here] + 1:
            Time[next] = Time[here] + 1
            GetSome(next) # 다음 위치의 시간이 현재 위치의 시간 + 1보다 클때 그 값을 갱신하고 다음 위치에 따른 GetSome 함수를 실행
ability = [0] * 3 #3개의 능력 초기화
Time = [987654321] * 100000 #시간을 충분히 큰 값으로 초기화
Shalala, Zombie = map(int, input().split())
ability[0], ability[1], ability[2] = map(int, input().split())
Time[Shalala] = 0 #경찰 위치의 시간을 0으로 초기화

if Shalala == Zombie:
    print(0) #경찰과 좀비가 동일하면 0을 출력
else:
    GetSome(Shalala) #아닌 경우에는 경찰의 위치에 따른 DFS를 실행

if Time[Zombie] != 987654321: #좀비 위치의 시간이 최솟값을 가지므로 그 시간을 출력
    print(Time[Zombie])
else:
    print(-1) #아닌 경우에 -1을 출력