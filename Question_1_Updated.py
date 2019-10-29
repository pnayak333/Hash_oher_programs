def merge(A):
    if len(A)-1 <= 1:
        return A
    mid = len(A) //2
    left = merge(A[:mid])
    right = merge(A[mid:])
    return Merge_Sort(A,left,right)

def Merge_Sort(A,left , right):
    i=0
    j=0
    result = []
    while(i<len(left) and j< len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


my_str = "abcvMMxzn"
new_lst = []
my_str = my_str.lower()
#my_lst = ['z','a','x','c','v','b','n']
my_lst = list(my_str)
#print(my_lst)
new_lst = merge(my_lst)
print(new_lst)
flag = False
c = 0
for i in range(len(new_lst)-1):
    if new_lst[i] == new_lst[i+1]:
        c = c + 1
        flag = True
        #print("Not a Unique String")

    else:
        flag = False
        #print("Unique")
if c >= 1:
    print("Not Unique String")
else:
    print("Unique String")


