x = int(input())

mylist = []
for i in range(x):
    stamp = input()
    mylist.append(stamp)

myset = set(mylist)
print(len(myset))
