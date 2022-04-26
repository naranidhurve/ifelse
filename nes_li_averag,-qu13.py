
elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
even_count=0
odd_count=0
avg1=0
avg2=0
while i<len(elements):
    if elements[i]%2==0:
        even_count=even_count+1
        even_sum=even_sum+elements[i]
        avg1=even_sum/even_count
    else:
        odd_count=odd_count+1
        odd_sum=odd_sum+elements[i]
        avg2=odd_sum/odd_count
    i=i+1
print ("even sum",even_sum)
print("odd sum",odd_sum)
print("count even",even_count)
print("count odd",odd_count)
print("avg even",avg1)
print("avg odd",avg2)