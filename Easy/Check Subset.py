T = int(input())
for i in range(T):
    input()
    seta = set(map(int,input().split()))
    input()
    setb = set(map(int,input().split()))
    if seta.issubset(setb):
        print('True')
    else:
        print('False')
