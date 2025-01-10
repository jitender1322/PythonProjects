import numpy as np

def summary(data):
    print("Data Summary")
    print(f"Total elements : {len(data)}")
    print(f"Maximum value : {max(data)}")
    print(f"Minimum value : {min(data)}")
    print(f"Sum of all value : {sum(data)}")
    
   
numList = []


while True:
    print("Welcome to data analyzer and transformer program. \n")

    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program \n")
    

    choice = int(input("Please enter your choice: "))
    if choice == 1:
        num = input("Enter data for a 1D array (seprated by spaces): ")
        numList = [int(num) for num in num.split(" ")]
        print(f"Data stored succesfully ! ")

    elif choice == 2:
        summary(numList)
    elif choice == 3:
        a=1
        number= int(input("Enter a number to calculate factorial : "))
        for i in range(1,number+1) :
            a *= i
        print(a)
    elif choice == 4:
        number= int(input("Enter a number to filter out data below this value : "))
        filtered = []
        for i in range(len(numList)):
            if numList[i]>=number:
                filtered.append(numList[i])
            else:
                pass
        print(filtered)

    elif choice == 5:
        print("Choose sorting method :")
        print("1. Ascending")
        print("2. Descending")
        number= int(input("Enter your choice : "))
        if number == 1 :
            numList.sort()
        elif number == 2 :
            numList.sort(reverse=True)
        print(numList)

    elif choice == 6:
        print("Dataset Statistics :")
        print(f"Minimum Value : {min(numList)}")
        print(f"Maximum Value : {max(numList)}")
        print(f"Sum of all Values : {sum(numList)}")
        print(f"Average Values : {np.mean(numList)}")

    elif choice == 7:
        print("Thank you !")
        break



