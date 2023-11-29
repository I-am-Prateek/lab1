#defining the global variable according to the quesition
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

#taking input from the user
firstcolor=input("Enter Your First Color:")
secondcolor=input("Enter Your Second Color:")

if(firstcolor==RED or firstcolor==BLUE or firstcolor==YELLOW):
    print()
else:
    print("Invalid color-1")

if(secondcolor==RED or secondcolor==BLUE or secondcolor==YELLOW):
    print()
else:
    print("Invalid color-2")

if(firstcolor==secondcolor):
    print("The two color you entered are the same.")
else:
    print()

#Applying the necessary condiitons

if(firstcolor==RED and secondcolor==BLUE):
    print("The final color is Purple.")
elif(firstcolor==BLUE and secondcolor==RED):
    print("The final color is Purple.")

elif(firstcolor==RED and secondcolor==YELLOW):
    print("The final color is Orange.")
elif(firstcolor==YELLOW, secondcolor==RED):
    print("The final color is Orange.")

elif(firstcolor==BLUE and secondcolor==YELLOW):
    print("The final color is Green.")
elif(firstcolor==YELLOW, secondcolor==BLUE):
      print("The final color is Green.")
else:
    Print("Invalid Color Combination.")


