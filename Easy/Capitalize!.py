def solve(s):
    finalstr = []
    mystr = " "
    newstr = s.split(' ')
    for i in newstr:
        finalstr.append(i.capitalize())
    mystr = mystr.join(finalstr)
    return mystr

