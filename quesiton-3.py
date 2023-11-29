#defining the global variables for salary
CAD=56000
USA=45000
COM=7649856
UK=45423
#Assume that the user is currently living in GErmany according to the question

#taking input from the user

current_salary=float(input("What is your current salary in EUR?\n"))
secondcountry=input("which country you want to migrate?\n").lower()
if(secondcountry=="canada" or secondcountry=="US" or secondcountry=="Cambodia" or secondcountry=="UK"):
     print()
else:
      print("Wrong Country Input")

def pay_conversion(current_salary, secondcountry):
  if(secondcountry=="canada"):
    current_salary=current_salary*1.49
  elif(secondcountry=="US"):
    current_salary=current_salary*1.10
  elif(secondcountry=="Cambodia"):
    current_salary=current_salary*4522.59
  elif(secondcountry=="UK"):
    current_salary=current_salary*0.86

  return current_salary


sal=pay_conversion(current_salary, secondcountry)

if(secondcountry=="canada"):
    print()
    if(sal>CAD):
       print("You will be rich in Canada with a salary of $",sal,)
    else:
       print("You will be poor in Canada with a salary of $",sal,)
elif(secondcountry=="US"):
    print()
    if(sal>USA):
        print("You will be rich in USA with a salary of $",sal,)
    else:
        print("You will be poor in USA with a salary of $",sal,)
elif(secondcountry=="Cambodia"):
    print()
    if(sal>COM):
        print("You will be rich in Cambodia with a salary of",sal,"KHR")
    else:
        print("You will be poor in Cambodia with a salary of ",sal,"KHR")
elif(secondcountry=="UK"):
    print()
    if(sal>UK):
        print("You will be rich in UK with a salary of £",sal,)
    else:
        print("You will be poor in UK with a salary of £",sal,)
else:
    print("Wrong Country Input")

 



