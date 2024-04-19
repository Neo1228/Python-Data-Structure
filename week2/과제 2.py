import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    many, long = map(int, input().split())
    value = list(map(int, input().split()))

    Rangesum = []
    for here in range(many - long + 1):
        Rangesum.append(sum(value[here:here + long]))
    print("#%d" % tc, max(Rangesum) - min(Rangesum))
