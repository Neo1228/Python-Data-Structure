#lambda 예시
xlist = ('1', '2', '3', '4')

xlist1 = []
xlist1 = list(map(int, xlist))
print(xlist1)
xlist2 =[]
lambda x : x + 1
xlist2 = list(map(lambda x : x + 1, xlist1))
print(xlist2)

#map 예시
slist = ('1', '2', '3')
slist1 = []

slist = list(map(int, slist))
print(slist)

#def 예시
def 예시():
    return print('예시')
예시()

