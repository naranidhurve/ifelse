

q=["variable ko use kar kar doosra question print karo"]
options= ["ka use kar kar doosre question ke chaaron options ko print karo doosre question."]
"What is the capital of India?"

options=["Chandigarh","Bhopal","Chennai","Delhi"]
solution=[4]
i=0
j=0
while i<len(q) and j<len(solution):
    print(q[i])
    k=0
    while k<(len(options)):
            print(k+1,options[j][k])
            k+=1
    a=int(input("enter your choices:"))
    if a==solution[i]:
        print("yes")
    else:
        print("no")
        print("sorry try again")
        break
        j+=1
    i=i+1
print()











