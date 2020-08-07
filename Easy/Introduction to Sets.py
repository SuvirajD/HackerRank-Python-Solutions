def average(array):
    myset = set(array)
    mylist = list(myset)
    length = len(mylist)
    sum = 0
    for i in mylist:
        sum = sum + i

    avg = sum/length
    return avg

