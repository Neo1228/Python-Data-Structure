Data = [3, 2, 5, 4, 1, 6]
howmany = len(Data)
def solve(now):
    if now >= howmany - 1: return
    #now가 homany-1 인 5보다 클때 반환값이 없이 반복 중지시킨다.
    where = Data.index(min(Data[now:howmany]))
    #Data의 시작부터 끝까지의 값들 중에 가장 작은 값의 인덱스를 찾아서 where에 할당해준다.
    Data[now], Data[where] = Data[where], Data[now]
    #제일 작은 값의 위치를 바꿔준다.
    solve(now + 1)
    #계속 반복해서 실행해줘야 하므로 now의 값에 1을 더해준다.

solve(0)
print(Data)