
question_list = [
"1 How many continents are there?",
"2 What is the capital of India?",
"3 NG mei kaun se course padhaya jaata hai?"
]
options_list  = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],

["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution = [3, 4, 1]
lifeline5050=[["nine","seven"],["chenni","dehli"],["software engering","tourism"]]
lifeans=[2,2,1]
i=0
j=0
while i<len(question_list):
    print(j+1,question_list[i])
    k=0
    while k<len(options_list)+1:
        print(k+1,options_list[j][k])
        k=k+1
    lifeline=input("want 5050 lifeline? enter yes or not")
    if lifeline=="yes":
        count=0
        if count==0:
            l=0
            while l<len(lifeline5050[i]):
                print(l+1,lifeline5050[i][l])
                l=l+1
            count=count+1
            sol=int(input("enter your answer"))
            if sol==lifeans[i]:
                print("congratulation!your answer is right")
            else:
                print("sorry! your answer is wrong")
                break
        else:
            print("your lifeline has been used")
            sol1=int(input("enter the answer"))
            if sol1==solution[i]:
                print("congratulation")
            else:
                print("beter luck next time")
                break
    elif lifeline=="no":
        sol1=int(input("enter the solution"))
        if sol1==solution[i]:
            print ("congratulation!our answer is right")
        else:
            print("beter luck of the next time")
            break    
    print()
    i=i+1
    j=j+1




