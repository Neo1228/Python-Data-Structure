Data = list(input())

def howmany(s):
    d = {'대문자': 0, '소문자':0}
    for letter in s:
        if 'a' <= letter <= 'z':
            d['소문자'] += 1
        elif 'A' <= letter <= 'Z':
            d['대문자'] += 1
    print(d)

howmany(Data)