def GetSome(count):
    if count == 0: return
    GetSome(count-1)
    #GetSome(3)~GetSome(0)까지 반복하다가 if문에 0이 걸리므로 이때 return을 통해서 스택을 해제한다.
    print("재귀호출 %d" % count)
    #스택을 해제하면서 1~3까지 순서대로 count에 대입된다.
GetSome(3)
