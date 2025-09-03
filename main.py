import pandas as pd
import os
import csv
from datetime import datetime


#Creating New CSV File
def init_file():
    if not os.path.exists('Expenses.csv'):
        with open('Expenses.csv',mode='a',newline='') as file:
            writer =csv.writer(file)
            writer.writerow(['Date','Category','Amount','Description'])

#Adding New Expense
def add_expense(date,category,amount,description):
    with open('Expenses.csv',mode='a',newline='') as file:
        writer =csv.writer(file)
        writer.writerow([date,category,amount,description])
    print("Expense Added Successfully!")

#Viewing All Expenses
def view_expenses():
    df=pd.read_csv('Expenses.csv')
    if df.empty:
        print("No expenses recorded.")
    else:
        print(df)

#Expenses Summary
def total_expenses():
    df=pd.read_csv('Expenses.csv')
    total=df['Amount'].sum()
    print(f"Total Expenses: {total}\n")
    by_category=df.groupby('Category')['Amount'].sum()
    print("Expenses by Category:\n")
    print(by_category)

#Export to Excel
def export_to_excel():
    df=pd.read_csv('Expenses.csv')
    df.to_excel('Expenses@.xlsx',index=False)
    print("Data exported to Expenses.xlsx successfully!")

#Main Function
def Menu():
    init_file()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses Summary")
        print("4. Export to Excel")
        print("5. Exit")
        choice=input("Enter your choice (1-5): ")
        
        if choice=='1':
            date=datetime.now().strftime("%Y-%m-%d")
            category=input("Enter Category: ")
            amount=float(input("Enter Amount: "))
            description=input("Enter Description: ")
            add_expense(date,category,amount,description)
        elif choice=='2':
            view_expenses()
        elif choice=='3':
            total_expenses()
        elif choice=='4':
            export_to_excel()
        elif choice=='5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Menu()


