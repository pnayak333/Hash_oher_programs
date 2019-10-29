def insert_Str(str1,str2):
    char= input("Enter The character to be inserted to Str1[Insert_Function]:")
    #leng = len(str1)
    str1 = str1 + char
    print(str1,str2)
    c = 0
    for char in range(0,len(str1)-1):
        print(str1[char],str2[c])
        if str1[char] == str2[char]:
            c = c +1
            print(c)
        else:
            c = c -1
            print(c)
    if c >= len(str2):
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------

def replace_Str(str1,str2):
    char = input("Enter a character to replace from Str2[Replace_Function]:")
    str3 = ""
    count = 0
    for c in range(0,len(str2)):
        if str2[c] != char:
            str3 = str3 + str2[c]
    print(str1,str3)
    #str2 = str2.translate(char)
    i = 0
    j = 0
    while(i < len(str1)):
        if str1[i] == str3[j]:
            i+=1
            j+=1
            count = count + 1
            print(count)
        else:
            i+=1
            count = count - 1
            print(count)
    if count >= 2:
        return True
    else:
        return False
    #print(str3)
#--------------------------------------------------------------------------------------------------
def remove_Str(str1,str2):
    str3 = ""
    char = input("Enter a Character to remove from Str2[Remove_Function]:")
    for c in range(0,len(str2)):
        if str2[c] == char:
            str3 =str2.replace(char,"")
            continue
    print(str3)
    count_Char = 0
    i = 0
    j = 0
    while(i <= len(str1)-1):
        if str1[i] == str3[j]:
            i+=1
            j+=1
            count_Char += 1
            print(count_Char)
            #continue
        else:
            i+=1
            count_Char -=1
            print(count_Char)
    if count_Char <= 0:
        return False
    else:
        return True
        #print(str3[c])
str1 = input("Enter First  the String:")
str2 = input("Enter Second the String:")
#options = input("Please Enter the Options between 1 to 3")
while(True):
    print("1.Replace_String\n"
          "2.Insert_String\n"
          "3.Remove_String\n"
          "4.Exit")
    options = input("Please Enter the Options between 1 to 4:")
    if options == "1":
        print(replace_Str(str1, str2))
    elif options == "2":
        print(insert_Str(str1,str2))
    elif options == "3":
        print(remove_Str(str1, str2))
    else:
        exit()




#print(str1,str2)
#print(replace_Str(str1,str2))
#print(insert_Str(str1,str2))
#print(remove_Str(str1,str2))


