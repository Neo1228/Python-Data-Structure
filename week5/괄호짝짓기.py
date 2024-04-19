import sys
sys.stdin = open("input")
pare = {'>' : '<', ')':'(', ']':'[', '}':'{'}

T = 10
for tc in range(1,T+1):
    print(f"#{tc}", end = ' ')
    #테스트케이스를 1부터 10까지 받음
    stack = []
    #스택을 초기화
    length = int(input())
    #괄호의 길이를 입력받음
    Data = list(input())
    #Data리스트안에 괄호를 입력받음
    howmany = len(Data)
    #괄호의 길이를 howmany에 할당함
    isCorrect = True
    #isCorrect를 True로 초기화함
    for i in range(howmany):
        if Data[i] == '(' or Data[i] == '{' or Data[i] == '[' or Data[i] == '<':
            stack.append(Data[i])
            #열린괄호를 만났을 때 이 열린괄호를 빈 스택에 추가함
        else:
            if not stack or pare[Data[i]] != stack[-1]:
                isCorrect = False
                break
                #스택이 비어있지 않거나 괄호의 짝이 스택에 가장 최근에 추가된 괄호와 일치하지 않는 경우 반복문을 멈춘다.
            else:
                stack.pop()
                #그러지 않은 경우에는 스택에서 뺀다.

    if not stack and isCorrect:
        print("1")
        #스택이 비어있지 않고 서로의 짝이 맞는다면 1을 출력
    else:
        print("0")
        #스택이 비어있고 서로의 짝이 맞지 않는다면 0을 출력