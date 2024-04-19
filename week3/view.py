for tc in range(1, 11):
    ans = 0
    howmany = int(input())
    Building = list(map(int, input().split()))

    for now in range(howmany -4):
        OnAir = Building[0:5]
        now = max(OnAir.pop(2)), max((OnAir), 0)

    print("#%d" %tc, ans)