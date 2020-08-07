if __name__ == '__main__':
    N = int(input())
    mylist1 = []
    for i in range(N):
        mylist = list(map(str,input().split()[:N])) 
        if mylist[0] == 'insert':
            a = int(mylist[1])
            b = int(mylist[2])
            mylist1.insert(a,b)

        elif mylist[0] == 'append':
            a = int(mylist[1])
            mylist1.append(a)

        elif mylist[0] == 'remove':
            a = int(mylist[1])
            mylist1.remove(a)
        
        elif mylist[0] == 'pop':
            mylist1.pop()
            
        elif mylist[0] == 'reverse':
            mylist1.reverse()

        elif mylist[0] == 'print':
            print(mylist1)
        
        elif mylist[0] == 'sort':
            mylist1.sort()


