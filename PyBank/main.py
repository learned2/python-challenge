# -*- coding: UTF-8 -*-
"""
PyBank Main Script

Author: Stan Usovicz
Created 12/11/2024

Description: returns  Total Month, Total P/L, Average Change, Greatest increase, and Greatest Decrease for budget_data.csv and outputs budget_analysis.txt

Resources consulted: 
https://stackoverflow.com/questions/31489377/working-of-n-in-python

"""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank","Resources", "budget_data.csv")  # Input file path
print(f"Looking for file at: {file_to_load}")

file_to_output = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
changes = []
previous_profit = None
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

# Open and read the csv
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data, delimiter= ",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    previous_profit = int(first_row[1])

    # Process each row of data
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Track the total
        total_months += 1
        total_net += profit_loss

        # Track the net change
        if previous_profit is not None: 
            change = profit_loss - previous_profit
            changes.append(change)

            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date

            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        #reset for next iteration
        previous_profit = profit_loss
        
    
    #average change monthly with rounded decimal
    if len(changes) > 0: 
        average_change = round(sum(changes)/len(changes), 2)
    else:
        average_change = 0 

    #output sum
    print(f"Total Months: {total_months}")
    print(f"Total Net Profit/Loss: {total_net}")
    print(f"Average change: {average_change}")    
    print(f"Greatest increase: {greatest_increase}")

    if greatest_decrease["date"] is not None:
        print(f"Greatest decrease: {greatest_decrease}")
    else: 
        print("No Decrease")

#output
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Net Profit/Loss: ${total_net}\n"
    f"Average change: ${average_change}\n"
    f"Greatest increase: {greatest_increase}\n"
    f"Greatest decrease: {greatest_decrease}\n"
)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
