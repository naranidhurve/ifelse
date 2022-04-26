
size=int(input("enter the size:"))
a=[]
for i in range(list):
    b=int(input("enter the num:"))
    a.append(b)
    j=0
for i in range(size):
    for j in range (0,size-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted list is:")
print(a)



# size=int(input("enter the size:"))
# i=0
# a=[]
# while i<=(size):
#     if i in  range(size):
#        b=int(input("enter the num:"))
#        a.append(b)
#     if i in range(size):
#         j=0
#         if j in range (0,size-i-1):
#          t=a[j]
#          a=[j+1]
#          b=[j+1]
# print("sorted list is:")
# print(b)
