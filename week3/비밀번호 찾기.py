N, M = map(int, input().split())
PW = {}
for _ in range(N):
    site, password = input().split()
    PW[site] = password
for _ in range(M):
    find = input()
    print(PW[find])