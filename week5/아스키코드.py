import sys
sys.stdin = open('input_1.txt', 'r') # 파일에서 읽을 때 사용
Pare = [0] * 128
Pare[ord(')')] = '('
Pare[ord(']')] = '['
Pare[ord('}')] = '{'
Pare[ord('>')] = '<'

for tc in range(1,4):
    print(f"#{tc}", end=' ')
    stack = []
    Data = input()

    howmany = len(Data)
    isCorrect = True
    for i in range(howmany):
           if Data[i] == '(' or Data[i] == '{' or Data[i] == '['  or Data[i] == '<' :
               stack.append(Data[i])
           else :
               if not stack or Pare[ord(Data[i])] != stack[-1]:
                    isCorrect = False
                    break
               else : stack.pop()

    if not stack and isCorrect: print("RIGHT")
    else : print("WRONG")