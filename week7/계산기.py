Data = "1+2*3+(4+5)/6"
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0} #스택 안에 있는 연산자의 우선순위
icp = {'*': 2, '/': 2, '+': 1, '-': 3, '(': 3} #스택에 들어갈 때의 연산자의 우선순위

stack = []
postFix = []

for now in Data:
    if '0' <= now <= '9':
        postFix.append(now) # 현재의 값이 숫자일 경우에 postFix에 추가
    elif now == ')':
        while stack[-1] != '(':
            postFix.append(stack.pop()) # 스택의 첫번째 값이 열린 괄호가 아닐 경우에 postFix의 배열에서 뽑아낸다.
        stack.pop() # 현재의 값이 닫힌 괄호일 경우에 스택에서 뽑아낸다.
    else:
        if not stack: # 현재의 값이 숫자도 아니고 괄호도 아닌 경우에 스택이 비어있지 않은 경우
            stack.append(now) # 스택에 추가
        elif icp[now] > isp[stack[-1]]:
            stack.append(now) # 현재의 icp가 스택에 이미 쌓여있는 첫번째 값의 isp보다 클 경우에 스택에 추가
        else:
            while stack and icp[now] <= isp[stack[-1]]:
                postFix.append(stack.pop()) # 스택이 비어있고 현재 값의 icp가 스택의 첫번째 값의 isp보다 더 작거나 같을 경우 postFix에 스택에서 뽑아낸 값을 추가
            stack.append(now) # 현재의 값이 숫자도 아니고 괄호도 아닌 경우에 스택에 현재의 값을 추가
while stack : postFix.append(stack.pop())
print(postFix) # 스택이 비어있지 않을때 postFix에 스택의 첫번째 값을 추가하고 postFix를 출력

for now in postFix:
    if now.isdigit():
        stack.append(now)
    else:
        b = int(stack.pop())
        a = int(stack.pop())

        if now == '*':
            stack.append(a * b)
        elif now == '/':
            stack.append(a / b)
        elif now == '-':
            stack.append(a - b)
        elif now == '+':
            stack.append(a + b)
print("결과 값:", stack[0])