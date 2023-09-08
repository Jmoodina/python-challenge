"""
PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company.
You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period
"""

# Import dependencies
import os
import csv

#Set budget_data filepath
filepath = "Resources\\budget_data.csv"

# Create the Variables and List for future use. 
count = 0
total_profit = 0
total_change = 0
profit = 0
profitorloss = []
monthly_changes = []
date = []

#Open CSV
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

# Calculate the number of months in filepath
    for row in csvreader:    
      count = count + 1 

# Append the Profit/Loss information and calculate the total
      date.append(row[0])
      profitorloss.append(row[1])
      total_profit = total_profit + int(row[1])

# Calculate the average change in months and profit/loss.
      final_profit = int(row[1])
      profit_changes = final_profit - profit
      monthly_changes.append(profit_changes)
      total_change = total_change + profit_changes
      profit = final_profit

# Calculate the average
    average_changes = (total_change/count)

# Calculate the greatest increase and decrease along with the dates associated with the value. 
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    greatest_increase_date = date[monthly_changes.index(greatest_increase)]
    greatest_decrease_date = date[monthly_changes.index(greatest_decrease)]
      
#  Print with the assignment's template and compare with the assignments values.
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total Profits: ${total_profit}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Create a text file to place the results
with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("----------------------------\n")
    text.write(f"Total Months: {count}\n")
    text.write(f"Total Profits: ${total_profit}\n")
    text.write(f"Average Change: ${average_changes}\n")
    text.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
    text.write("----------------------------\n")








    