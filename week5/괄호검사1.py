import sys
sys.stdin = open('input_1', 'r')

for tc in range(1,4):
    print(f"#{tc}", end = ' ')
    stack=[]
    Data = input()
    howmany = len(Data)
    #howmany = 30
    isCorrect = True
    #isCorrect를 True로 초기화
    for now in range(howmany):
        if Data[now] == '(':
        #(이 나왔을 때마다 스택에 추가
                stack.append(Data[now])
        else:
               if not stack or stack[-1] != '(':
                #스택이 비어있거나 스택에서 제일 최근에 추가된 값이 (이 아닌경우에는 isCorrect를 False로 출력하고 중단한다
                   isCorrect = False
                   break
    if not stack and isCorrect:
    #스택이 비어있거나 isCorrect가 True인 경우에는 결과값으로 correct를 출력
        print("Correct")
    else:
    #스택이 비어있지않거나 isCorrect가 False인 경우에는 결과값으로 Wrong을 출력
        print("Wrong")