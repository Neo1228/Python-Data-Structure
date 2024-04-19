val = 123

temp = val

howmany = 0
while temp:
    howmany += 1
    temp //= 10

Data = [0] * howmany

while howmany:
    howmany -= 1
    Data[howmany] = str(val % 10)
    val //= 10

print(Data)
