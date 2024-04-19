pare = {'>': '<', ')': '(', ']': '[', '}': '{'}
# 짝 딕셔너리에 열린괄호와 닫힌괄호끼리 맞는 것들을 추가
Data = ['<', '{', '}', '<']

stack = []
ans = 0

while Data:
    # Data가 존재할 때까지 while 문을 반복
    now = Data.pop(0)
    # now 함수에 Data의 맨 첫번째 값을 뽑아낸 값을 추가
    if now in pare.values():
        stack.append(now)
        # now 함수 안에 짝의 함수가 존재하면 빈 스택에 now 함수의 값을 추가
    elif stack and stack[-1] == pare[now]:
        stack.pop()
        # 스택이 비어있지 않고 스택에 가장 마지막에 추가된 값이 괄호 짝과 맞다면 스택에 존재하는 값을 뽑아낸다.
    else:
        break

    if not stack:
        ans = 1
# 스택이 비어있는 경우에는 ans의 값을 1로 할당
print(ans)
