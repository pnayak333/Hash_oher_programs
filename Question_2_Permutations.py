def Quick_Sort(A,low,high):
    if low < high:
        Pi = Partition_Pivot(A,low,high)
        Quick_Sort(A,low,Pi-1)
        Quick_Sort(A,Pi+1,high)


def Partition_Pivot(A,low,high):
    i = (low -1)
    piv = A[high]
    for j in range(low ,high):
        if A[j] <= piv:
            i+= 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[high] = A[high],A[i+1]
    return (i+1)
#--------------------------------------------------------------------
str1 = "eat"
str1 = str1.lower()
print(str1)
str1 = list(str1)
print(str1)
n = len(str1)
Quick_Sort(str1,0,n-1)
for i in range(len(str1)):
    print(str1[i])
#----------------------------------------------------------------------
str2 = "ate"
str2 = str2.lower()
print(str2)
str2 = list(str2)
print(str2)
n = len(str2)
Quick_Sort(str2,0,n-1)
for i in range(len(str2)):
    print(str2[i])
flag = False
for char in range(0,len(str2)-1):
    if str1[char] == str2[char]:
        flag = True
        #print("Great -Permutation")
    else:
        flag = False
        break
        #print("Oops! Its Not")
if flag == True:
    print("Great")
else:
    print("opps! Not")