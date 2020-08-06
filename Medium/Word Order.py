from collections import Counter

x = int(input())
mylist = []
for i in range(x):
    word = input()
    mylist.append(word)
str1 = " "
str1 = str1.join(mylist)
mylist1 = str1.split()
mylist1 = str1.split()
count = Counter(mylist1)
mydict = dict(count)
myset = set(count)
total_unique = len(myset)
print(total_unique)
print(*list(mydict.values()))
