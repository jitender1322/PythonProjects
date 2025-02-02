import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;


class LibraryDashboard:
    def __init__(self,filepath):
        self.filepath = filepath
        self.dataframe = None

    def loadData(self):
        self.df = pd.read_csv(self.filepath)
        print("Data set is loaded ! \n")

    def calculateStat(self):
        mostBorrowedBook = self.df["Book Title"].value_counts().idxmax()
        avgBorrowingTime = self.df["Borrowing Duration (Days)"].mean()
        busiestDay = self.df["Date"].value_counts().idxmax()

        print(f"Most borrowed book : {mostBorrowedBook}")
        print(f"Average borrowed time : {avgBorrowingTime}")
        print(f"Most busiest day : {busiestDay}")
    
    def filterTransactions(self,genre=None,borrowingDuration = None):
        if genre:
            filterdData = self.df[self.df["Genre"]==genre];
            print(filterdData)
        if borrowingDuration:
            filterdData = self.df[self.df["Borrowing Duration (Days)"]== borrowingDuration];
            print(filterdData)

    def generateReport(self):
        self.calculateStat()
        print(self.df.describe())
        print(self.df.info())
    
    def visualizeDf(self,type):
        if type =="Bar" :
            books = self.df["Book Title"].value_counts().head(5)
            plt.bar(books.index, books.values)
            plt.xlabel("Books Name")
            plt.ylabel("Number of books")
            plt.title("Most borrowed book")
            plt.show()

        if type == "Line" : 
            self.df["Date"] = pd.to_datetime(self.df["Date"])
            borrowing = self.df.groupby(self.df["Date"].dt.month_name())["User ID"].count()
            plt.plot(borrowing.index, borrowing.values)
            plt.show()

        if type == "Pie" :
            genre = self.df["Genre"].value_counts()
            plt.pie(genre, labels=genre.index)
            plt.show()

obj = LibraryDashboard("library_transactions.csv");

obj.loadData()
obj.calculateStat()
obj.filterTransactions(genre="Classic")
obj.visualizeDf(type="Pie")
obj.generateReport()

# Done sir !