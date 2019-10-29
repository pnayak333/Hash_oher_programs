from functools import reduce
def Find_Zero(mat1):
    for i in range(0,len(mat1)):
        for j in  range(0,len(mat1[0])):
            if mat1[i][j] == 0:
                mat1[i][0] = 0
                mat1[0][j] = 0

def Row_Zero(mat1, j):
    for j in range(0,len(mat1[0])):
        mat1[0][j] = 0

def Col_Zero(mat1, i):
    for i in range(0,len(mat1)):
        mat1[i][0] = 0


mat1 = [[0,2,3,19],
         [4,5,6,12],
         [43,51,0,123],
        [7,8,9,11]]
r = len(mat1)
c = len(mat1[0])
print("Row:",r,"Col:",c)


Zero_Has_Row = False
Zero_Has_Col = False

for i in range(0,len(mat1)):
    if mat1[i][0]:
        Zero_Has_Row = True
        break
for j in range(0,len(mat1[0])):
    if mat1[0][j]:
        Zero_Has_Col =True
        break

Find_Zero(mat1)

for i in range(1,len(mat1)):
    #print(row[i])
    if mat1[i][0] == 0:
        Row_Zero(mat1,i)
for j in range(1,len(mat1[0])):
    #print(col[j])
    if mat1[0][j] == 0:
        Col_Zero(mat1,j)

if Zero_Has_Row:
    Row_Zero(mat1,0)
if Zero_Has_Col:
    Col_Zero(mat1,0)

#Print the
for i in range(0,len(mat1)):
    print(mat1[i])


#mat1  = reduce(lambda x: x+x,mat1)




