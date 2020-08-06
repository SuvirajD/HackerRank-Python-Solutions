input()
hap = 0
a = list(map(int, input().split()))
seta = set(map(int,input().split(' ')))
setb = set(map(int,input().split(' ')))
for i in a:
    if i in seta:
        hap += 1
    elif i in setb:
        hap -= 1
        
print(hap)
