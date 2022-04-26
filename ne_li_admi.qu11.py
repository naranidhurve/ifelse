
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# while i<len(elements):
#     if elements[i]%2==0:
#      print ("even",elements[i])
#     else:
#      print("odd",elements[i])
#     i=i+1



elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
even_count=0
odd_count=0
while i<len(elements):
    if elements[i]%2==0:
        even_count=even_count+1
        even_sum=even_sum+elements[i]

    else:
        odd_count=odd_count+1
        odd_sum=odd_sum+elements[i]
    i=i+1
print ("even sum",even_sum)
print("odd sum",odd_sum)
print("count even",even_count)
print("count odd",odd_count)
