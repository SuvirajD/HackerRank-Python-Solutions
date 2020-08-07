def mutate_string(string, position, character):
    mylist = list(string)
    mylist[position] = character
    mystr = ""
    for i in mylist:
        mystr += i
    return mystr


