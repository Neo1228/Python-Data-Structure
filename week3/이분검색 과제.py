def binary_search(Data, key):
    start = 0
    end = len(Data)-1

    while start <= end:
        mid = (start + end) // 2
        if Data[mid] == key:
            return 1
        elif Data[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
check = list(map(int, input().split()))

for num in check:
    print(binary_search(A, num))
