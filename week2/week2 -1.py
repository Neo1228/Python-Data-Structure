Data = [i for i in range (1,7)]
#Data라는 함수의 리스트 요소인 i에 1부터 6까지의 값을 할당한다.
howmany = len(Data)
#Data의 길이는 1부터 6까지의 6개이므로 howmany는 정수 6과 같다고 볼 수 있다.
for i in range(howmany//2):
#i라는 함수에 howmany를 2로 나눈 3 0부터 까지의 수를 할당한다.
    Data[i], Data[howmany -1 -i] = Data[howmany -1 -i], Data[i]
#첫번째로 i에 0을 대입하면 Data[0], Data[6 -1 -0] = Data[5], Data[0]으로서 순서를 뒤바꾼다.
print(Data)