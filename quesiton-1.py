#Taking input from the user
 
month=int(input("Enter the month:"))
day=int(input("Enter the day:"))
year=int(input("Enter the year:"))

if(month>12):
    print("Invalid month")
if(day>30):
    print("Invalid day")
if(year>99):
    print("Invalid year")

if(month==2):
   if(year%4==0):
      if(day>29):
        print("Invalid day")
else:
    print("You have entered",month,"/",day,"/",year)

if(month==1, month==5,month==7, month==8, month==10, month==12 ):
    if(30>day<32):
        print("You have entered",month,"/",day,"/",year)
else:
    print("Invalid month and day")       

       