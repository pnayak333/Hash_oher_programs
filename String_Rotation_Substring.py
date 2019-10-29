def Check_rotation(s1,s2):
    l = len(s1)
    if ((l == len(s2)) and l > 0):
        s3 = s1 + s1
        print("S3:",s3,"S2:",s2)
        if s2 in s3:
            return True
        else:
            return False
    else:
        return False



s1 ="abcd"

s2 = ""
x = y=""
for char in range(0,len(s1)):
    if char < 3:
        x = x + s1[char]
    else:
        y = y + s1[char]
s2 = y + x

print(s2)

print(Check_rotation(s1,s2))
