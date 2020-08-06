from collections import OrderedDict
mylist = []
lolist = []
setlist = []
finallist = []
def merge_the_tools(string, k):
    for i in string:
        mylist.append(i)
    a = int(len(mylist)/k)
    for m in range(a):
        newlist = mylist[0:k]
        lolist.append(newlist)
        del mylist[0:k]
    for n in lolist:
        newlist = list(OrderedDict.fromkeys(n))
        setlist.append(newlist)
    for v in setlist:
        listToStr = ''.join([str(elem) for elem in v])
        finallist.append(listToStr)
    
    for t in finallist:
        print(t)
    
entry1 = input()
entry2 = int(input())
merge_the_tools(entry1,entry2)