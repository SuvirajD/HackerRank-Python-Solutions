x = int(input())


mylist = list(map(int,input().split()[:x]))
myset = set(mylist)
mylist2 = list(myset)
mylist2.sort()
print(mylist2[-2])
