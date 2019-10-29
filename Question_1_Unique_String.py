my_str = "Helo"
flag= False
count = 0
for i in range(0,len(my_str)-1):
    j=i
    for j in range(0,len(my_str)-1):
        if my_str[i] == my_str[j+1] in my_str:
            count += 1
            flag = True
            #print("True")
        else:
            flag = False
            #print("False")
if count > 2:
    print("This Not NOT NOTString Unique ")
else:
    print("Unique")