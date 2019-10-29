def Count_Number_of_Char(my_Str):
    length = len(my_Str)
    print(length)
    count = 0
    result = []
    char = 0
    c = 0
    while (char < len(my_Str)-1):

        if my_Str[char] == my_Str[char+1]:
            count = count +1
            char += 1
        elif my_Str[char] != my_Str[char+1]:
            count += 1
            result.append(my_Str[char])
            result.append(count)
            count = 0
            char += 1
    while length > 0:
        if my_Str[length-1] == my_Str[length-2]:
            c = c +1
            length = length -1
        else:
            c = c + 1
            result.append(my_Str[length-1])
            result.append(c)

            count = 0
            break
    return result


my_Str ="aaabbbccddexxz"


#print(length)

res =""


res = ''.join(map(str,Count_Number_of_Char(my_Str)) )

print(res)
