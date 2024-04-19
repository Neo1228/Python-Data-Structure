import math

start = 10
end = 20

for now in range(start, end + 1):
    isPrime = True
    for div in range(2, int(math.sqrt(now) + 1)):
        if(now % div) == 0:
            isPrime = False
            break
    if isPrime:
        print(now)
