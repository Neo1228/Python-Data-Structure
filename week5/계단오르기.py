ans = 0
def GetSome(here):
    global ans
    if here > howmany: return
    if here == howmany:
        ans+=1
        return
    GetSome(here+1)
    GetSome(here+2)

howmany = int(input())
GetSome(0)
print(ans)