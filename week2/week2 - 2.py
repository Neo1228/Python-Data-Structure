Data = [i for i in range (1,7)]
howmany = len(Data)

start = 3; end = 5
dummy = Data[start:end+1]
dummy.reverse()
Data[start:end+1] = dummy
print(Data)