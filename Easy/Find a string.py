def count_substring(string, sub_string):
    cnt = 0
    if len(string) >= 1 and len(string) <= 200:
        for i in range(len(string)):
            checkstr = string[i:i+len(sub_string)]
            if checkstr == sub_string:
                cnt += 1
    else:
        pass

    return cnt