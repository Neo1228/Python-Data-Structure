stack = []

for i in range(1,4):
    stack.append(i)
while stack:
    #stack이  존재할 때가지 스택을 뽑아라.
    print(stack.pop(-1))
    #맨마지막부터 뽑기때문에 3, 2, 1 순서로 뽑힌다.