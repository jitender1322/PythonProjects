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

    elif choice == 7:
        print("Thank you !")
        break



