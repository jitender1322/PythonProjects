import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SalesDataAnalyzer :
    def __init__(self,filePath,data=None):
        self.filePath = filePath
        self.data = data
    
    def loadData(self):
        self.data = pd.read_csv(self.filePath)

    def head(self):
        return self.data.head(5)

    def tail(self):
        return self.data.tail(5)
    
    def colNames(self):
        return self.data.columns

    def datatypes(self):
        return self.data.dtypes

    def basicInfo(self):
        self.data.info()

    def missingRows(self):
        return self.data[self.data.isnull().any(axis=1)]

    def fillRow(self):
        self.data = self.data.fillna(self.data.mean())
        return self.data
    
    def fillSpecific(self,val):
        self.data= self.data.fillna(val)
        return self.data

while True:
    print("=== Data Analysis & Visualization Program ===")
    print("Please select an option :")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Handle Missing Data")
    print("4. Generate Descriptive Statistics")
    print("5. Data Visualization")
    print("6. Save Visualization")
    print("7. Exit")
    print("===============================================")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("===Load Dataset===")
        path = input("Enter the path of tha dataset(csv file) : ")
        obj = SalesDataAnalyzer(path)
        obj.loadData()
        print("Data loaded successfully !")

    elif choice == 2:
        print("===Explore Data===")
        print("1. Display the First 5 row")
        print("2. Display the Last 5 row")
        print("3. Display colmun names")
        print("4. Display data types")
        print("5. Display basic info")

        choice = int(input("Enter your choice : "))

        if choice == 1 : 
            print(obj.head())
        elif choice == 2:
            print(obj.tail())
        elif choice == 3:
            print(obj.colNames())
        elif choice == 4:
            print(obj.datatypes())
        elif choice == 5:
            print(obj.basicInfo())
        else:
            print("Choice is wrong !")
    elif choice ==3:
        print("===Handle Missing Data===")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            if obj.data.isnull().values.any():
                print(obj.missingRows())
            else :
                print("No null data in rows")
        elif choice == 2:
            if obj.data.isnull().values.any():
                print(obj.fillRow())
            else :
                print("No null data in rows")
        elif choice == 3:
            obj.data.dropna()
            print("Empty data row droped")
        elif choice == 4:
            if obj.data.isnull().values.any():
                value = int(input("Enter specific value"))
                print(obj.fillSpecific(value))
            else :
                print("No null data in rows")
        else:
            print("invalid choice !")

        