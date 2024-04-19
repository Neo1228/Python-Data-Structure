import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1 , T + 1):
    N = int(input())
    building_h = list(map(int, input().split()))
    vc = 0
    for i in range(2,N-2):
        current_height = building_h[i]
        left_max = max(building_h[i-1], building_h[i-2])
        right_max = max(building_h[i+1], building_h[i+2])

        if current_height > left_max and current_height > right_max:
            vc += min(current_height - left_max, current_height - right_max)
    print("#%d" %tc, vc)
