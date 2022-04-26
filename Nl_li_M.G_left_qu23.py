
list=[[2,3,4],[6,7,8],[9,2,3]]
i=0
while i<len(list):
    j=0
    sum=0
    sum1=0
    f =len(list)-1
    while j<len(list):
       sum=sum+(list[i][j])
       sum1=sum1+list[j][f]
       j=j+1
       f=f-1
    i=i+1
print(sum)
print(sum1)

# list=[[2,3,4],[6,7,8],[9,2,3]]
# i=0
# while i<len(list):
#     j=0
#     column=0
#     row=0
#     sum=0
#     sum1=0
#     f =len(list)-1
#     while j<len(list):
#         column=column+list[i][j]
#         row=row+list[j][i]
#         sum=sum+(list[i][j])
#         sum1=sum1+list[j][i]
#         j=j+1
#         f=f+1
#     i=i+1
# print(sum)
# print(sum1)
# print(column)
# print(row)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist) 