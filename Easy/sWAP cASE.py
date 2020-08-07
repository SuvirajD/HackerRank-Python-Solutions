def swap_case(s):
    s1 = list(s)
    list1 = []
    mystr = ""
    for letter in s1:
        if letter.isupper() == True:
            letter = letter.lower()
            list1.append(letter)

        elif letter == ' ' or letter == '"' or letter == '.':
            list1.append(letter)

        else:
            letter = letter.upper()
            list1.append(letter)
            

    for i in list1:
        mystr += i
        
    return mystr


