#Good Job
def Count_Space(my_str,true_length):
    count_Space = 0
    for char in range(0,len(my_str)):
        if my_str[char] == " ":
            count_Space += 1
    print(count_Space)
    my_Str2 = ""
    c = "%20"
    index = true_length + (count_Space * 2)
    end = len(my_str)-1
    for char in range(0,true_length-1):
        if my_str[char] != " ":
            my_Str2 = my_Str2 + my_str[char]
        else:
            my_Str2 = my_Str2 + c
    print(my_Str2)

my_str = "Mr John Smith    "
l = len(my_str)
print(l)

count = 0
length = 13
print(length)
Count_Space(my_str,length)
#for num in range(0,len(my_str)-1):
    #print(my_str[num])