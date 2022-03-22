a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
arr=[]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j][1]>a[j+1][1]:
            l=a[j]
            a[j]=a[j+1]
            a[j+1]=l
print(a)