from functools import reduce
def Find_Zero(mat1):
    for i in range(0,len(mat1)):
        for j in  range(0,len(mat1[0])):
            if mat1[i][j] == 0:
                row[i] = True
                col[j] = True

def Row_Zero(mat1, row):
    for j in range(0,len(mat1[0])):
        mat1[row][j] = 0

def Col_Zero(mat1, col):
    for i in range(0,len(mat1)):
        mat1[i][col] = 0


mat1 = [[0,2,3,19],
         [4,5,6,12],
         [43,51,0,123],
        [7,8,9,11]]
r = len(mat1)
c = len(mat1[0])
print("Row:",r,"Col:",c)
row = [False] * len(mat1)
col = [False] * len(mat1[0])



Find_Zero(mat1)

for i in range(0,len(row)):
    #print(row[i])
    if row[i]:
        Row_Zero(mat1,i)
for j in range(0,len(col)):
    #print(col[j])
    if col[j]:
        Col_Zero(mat1,j)


#Just to trace the Boolean array for 0
for i in range(len(row)):
    print("Row:",row[i],"Index",i)
    for j in range(len(col)):
        print("Col:",col[j],"Index",j)

#Print the
for i in range(0,len(mat1)):
    print(mat1[i])


#mat1  = reduce(lambda x: x+x,mat1)




