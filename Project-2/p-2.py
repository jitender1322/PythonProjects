print("Welcome to the pattern generator and number analyzer !")

print("Select An Option : ")
print("1. Generate a pattern ") 
print("2. Analyze a number ")
print("3. Exit")

userInput = int(input("Enter Your Choice : "))


if userInput == 1 :
    print("Choose a pattern type"); print("1. Left angle pattern"); print("2. Pyramid"); print("3. Right angle Pattern")

    userInput2 = int(input("Enter Your Choice : "))

    if userInput2 == 1 : 
        for i in range(1,6):
            for j in range(1,i+1):
                print(j, end=" ")
            print()
    elif userInput2 == 2 : 
       for i in range(1,6):
            for j in range(1,i+1):
                print(j, end=" ")
            print()
       for i in range(5,0,-1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()
    elif userInput2 == 3 :
        for i in range(1,6):
            for j in range(i,5):
                print(" ", end=" ")
            for k in range(1,i+1):
                print(k, end=" ")
            print()

elif userInput == 2:
    start= int(input("Enter the start of the range : "))
    end = int(input("Enter the end of the range : "))
    sum=0
    for i in range(start,end +1):
        sum+=i
        if i%2 ==0:
            print(f"{i} is Even")
        else :
            print(f"{i} is Odd")
        
    print(f"Sum of all numbers from {start} to {end} is : {sum}")

elif userInput ==3 :
    print("Exiting the program. Good Bye !")
else :
    print("Your input is not valid")

