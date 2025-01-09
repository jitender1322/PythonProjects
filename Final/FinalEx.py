import pandas as pd
import matplotlib.pyplot as plt

fileName = input("Enter the file name(.csv) : ")

data = pd.read_csv(fileName)
print("Data added")

class retail_analyzer :
    def __init__(self,data):
        self.data = data

    def analyizeData(self):
        totalSales = self.data['Total Sales'].sum()
        avgSales = self.data['Total Sales'].mean()
        mostPopularProduct = self.data.groupby('Product')['Quantity Sold'].sum().max()

        print(f"Total sale : {totalSales}")
        print(f"Average sale : {avgSales}")
        print(f"Popular product : {mostPopularProduct}")

    def visualize(self):
        saleTrend = data['Total Sales']


dataAnalyze = retail_analyzer(data)
dataAnalyze.analyizeData()