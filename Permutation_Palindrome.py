#Brute _Force - Begining

def merge_Sort(my_Str):
    if len(my_Str) <= 1:
        return my_Str
    mid = len(my_Str)//2
    left = merge_Sort(my_Str[:mid])
    right = merge_Sort(my_Str[mid:])
    return merge(left,right)

def merge(left,right):
    i = 0
    j = 0
    result = []
    while(i  < len(left) and j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result

my_Str = "Tact Co"
my_Str = my_Str.lower()
my_Str = my_Str.replace(" ","")
print(my_Str)
#my_Str = list(my_Str)

New_Str = ""
c_e = 0
c_o = 0
i = 0
New_Str = merge_Sort(my_Str)
l = len(New_Str)
print(New_Str)
while i < len(New_Str)-1:
    if New_Str[i] != New_Str[i+1]:
        c_o += 1
        i += 1
        print("Odd - Count - First[Char]", c_o, New_Str[i], New_Str[i+1], i)

    elif New_Str[i] == New_Str[i+1]:
        c_e +=2
        print("Even - Count",c_e,New_Str[i],New_Str[i+1],i)
        i += 1

    elif New_Str[len(New_Str) - 2] != New_Str[len(New_Str) - 1]:
        c_o += 1
        print("Odd - Count - Last[Char]", c_o, New_Str[len(New_Str) - 2], New_Str[len(New_Str) - 1], i)
        i += 1
    elif New_Str[i] != New_Str[i+1] and New_Str[i+1] != New_Str[i+2]:
        c_o+=1
        print("Odd - Count",c_o, New_Str[i],New_Str[i+1],New_Str[i+2], i)
        i += 1

    else:
        i+=1
if (c_e % 2 == 0) and c_o == 1:
    print("Condition - True")
else:
    print("Conditions - False")


    #print(New_Str[char],char)

#print(Permutation_Palindrome(New_Str))

