from datetime import date

today_date = date.today()

print("Welcome to the interactive personal Data Collector")

name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
height = float(input("Please enter your height in meters : "))
favNum = int(input("Please enter your favourite number : "))

print("Thank you ! here is the information we collected")

print(f"Name : {name} (Type : {type(name)}, Memory Address: {id(name)})")
print(f"Age : {age} (Type : {type(age)}, Memory Address: {id(age)})")
print(f"Height : {height} (Type : {type(height)}, Memory Address: {id(height)})")
print(f"Favourite NUmber : {favNum} (Type : {type(favNum)}, Memory Address: {id(favNum)})")

print(f"Your birth year is approximately: {today_date.year - age } (based on your age of {age})")




