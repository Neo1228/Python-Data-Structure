def is_safe(y, x):
    return 0 <= x < 5 and 0 <= y < 5


def my_abs(a):
    return a if a > 0 else -a


Data = [[1, 1, 1, 1, 1],

        [1, 0, 0, 0, 1],

        [1, 0, 0, 0, 1],

        [1, 0, 0, 0, 1],

        [1, 1, 1, 1, 1]]

dy = [-1, 1, 0, 0]

dx = [0, 0, -1, 1]  # 상하좌우

sum = 0

for y in range(5):

    for x in range(5):

        for dir in range(4):

            new_y = y + dy[dir]

            new_x = x + dx[dir]

            if is_safe(new_y, new_x):
                sum += my_abs(Data[y][x] - Data[new_y][new_x])

print(f"sum = {sum}")