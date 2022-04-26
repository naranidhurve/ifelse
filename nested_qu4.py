
number1=30
number2 = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
b=[]
while i<len(number2):
    k=[]
    j=0
    while j<len(number2):
        if number2[i]+number2[j]==number1 and number2[j]>number2[i]:
            k.append (number2[i])
            k.append(number2[j])
            b.append(k)
        j=j+1
    i+=1
print(b)





# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]


