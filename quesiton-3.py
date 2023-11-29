#defining the global variables for salary
CAD=56000
USA=45000
COM=7649856
UK=45423
#Assume that the user is currently living in GErmany according to the question

#taking input from the user

current_salary=float(input("What is your current salary in EUR?\n"))
secondcountry=input("which country you want to migrate?\n").upper().lower()
if(secondcountry=="canada" or secondcountry=="United_States" or secondcountry=="Cambodia" or secondcountry=="United_Kingdom"):
     print()
else:
      print("Wrong Country Input")

def pay_conversion(current_salary, secondcountry):
  if(secondcountry=="canada"):
    current_salary=current_salary*0.67
  elif(secondcountry=="United_States"):
    current_salary=current_salary*0.90
  elif(secondcountry=="Cambodia"):
    current_salary=current_salary/4522.59
  elif(secondcountry=="United_Kingdom"):
    current_salary=current_salary/1.16

  return current_salary
if(secondcountry=="canada"):
    print()
    if(current_salary>CAD):
       print("You will be rich in Canada with a salary of $",current_salary,)
    else:
       print("You will be poor in Canada with a salary of $",current_salary,)
elif(secondcountry=="United_States"):
    print()
    if(current_salary>USA):
        print("You will be rich in USA with a salary of $",current_salary,)
    else:
        print("You will be poor in USA with a salary of $",current_salary,)
elif(secondcountry=="Cambodia"):
    print()
    if(current_salary>COM):
        print("You will be rich in Cambodia with a salary of",current_salary,"KHR")
    else:
        print("You will be poor in Cambodia with a salary of ",current_salary,"KHR")
elif(secondcountry=="United_Kingdom"):
    print()
    if(current_salary>UK):
        print("You will be rich in UK with a salary of £",current_salary,)
    else:
        print("You will be poor in UK with a salary of £",current_salary,)
else:
    print("Wrong Country Input")

pay_conversion(current_salary, secondcountry)

 



