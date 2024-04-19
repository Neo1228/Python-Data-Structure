Data = ['1', '2', '3']

val = 0
for i in range(len(Data)):
    val = val * 10 + int(Data[i])

print(val)