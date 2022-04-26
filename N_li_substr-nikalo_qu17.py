
mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
str=mainStr.split()
i=0
while i<len(str):
    if str[i]=="over":
        del str[i]
    else:
        print(str[i],end=" ")
    i=i+1
x=mainStr.replace("over","on")
print(x)


