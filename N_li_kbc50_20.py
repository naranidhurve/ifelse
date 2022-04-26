
print("Welcome my dear brothers and sisters to KAUN BANEGA CROREPATI!")
question_list=["How many continents are there ?","What is the capital of India ?",
"Which course is being taught in Navgurukul?"]
options_list=[["Four","Nine","Seven","Eight"],
["Chandigarh","Bhopal","Chennai","Delhi"],
["Software Engineering","Counseling","Tourism",
"Agriculture"]]
life_line=[["Seven","Eight"],["Bhopal","Delhi"],["Software Engineering","Counseling"]]
life_solution=[1,2,1]
i=0
count=0
solution_list=[3,4,1]
while i<len(question_list):
   print(i+1,question_list[i])
   j=0
   while j<len(options_list[i]):
      print(j+1,options_list[i][j])
      j+=1
   user=("without lifeline","with lifeline")
   print("choose your choice:")
   print("1.without lifeline")
   print("2.with lifeline")
   choice=int(input("your choice:"))
   if choice==1:
      user1=int(input("enter your answer:"))
      if user1==solution_list[i]: 
         print("WOW! CONGRATULATIONS","\n","Go Ahead")
      
      else:
         print("wrong answer!","\n","you can't move further","\n","restart the game")
         
         break
   elif choice==2:
      if count==0:
         k=0
         while k<len(life_line[i]):
            print(k+1,life_line[i][k])
            k+=1
         count+=1
         user2=int(input("enter your ans:")) 
         if user2==life_solution[i]: 
            print("WOW!! COGRATULATIONS","\n","You Did It ")
            
               
         else:
            print("wrong answer","\n","sorry..please restart")
           
            break
      elif choice==1:
         print("you have used your lifeline")
         if count==1:
            l=0
            while l<len(solution_list[i]):
               print(l+1,solution_list[i][l])
               l=l+1
            count=count+1
            
            user3=input("enter your choice")
            if user3==solution_list[i]:
               print("wow...","\n","just one question left")
               
            else:
               print("SORRY...","\n","PLEASE RETRY..")
               
               break
         

      else:
         print("you have used your lifeline")
         user4=int(input("enter your answer:"))
         if user4==solution_list[i]:
            print("BRAVOO.. YOU'RE AWESOME!")
            
         else:
            print("wrong answer","\n","almost clear.. restart")
            
            break     
   else:
      print("we're so sorry for the inconvenience")
      break
   i+=1

   