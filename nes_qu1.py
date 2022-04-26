marks=[78,76,94,86,88,],[91,71,98,65,76],[95,45,78,52,49]
marks1=marks[0]
marks2=marks[1]
marks3=marks[2]
i=0
j=0
k=0
sum=0
sum1=0
sum2=0

while i<len(marks1):
    sum=sum+marks1[i]
    i=i+1
while j<len(marks2):
    sum1=sum1+marks2[j]
    j=j+1
while k<len(marks3):
        sum2=sum2+marks3[k]
        k=k+1
print(sum+sum1+sum2)
