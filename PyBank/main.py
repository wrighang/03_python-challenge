# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# final script should both print the analysis to the terminal and export a text file with the results.

#######################################

# -*- coding: UTF-8 -*-
#PyBank code

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
# file_to_load = os.path.join("/Users/Angelina/Desktop/DA_Course/classwork_Spot/challenges/03.04-Challenge-Starter_Code/03_python-challenge/PyBank/Resources", "budget_data.csv")  # Input file path
# file_to_output = os.path.join("/Users/Angelina/Desktop/DA_Course/classwork_Spot/challenges/03.04-Challenge-Starter_Code/03_python-challenge/PyBank/analysis", "budget_analysis.txt")  # Output file path
file_to_load = os.path.join(".", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join(".", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track 
months = [] #list that will store months
net_change = [] #list that will store the changes between current and previous profit/loss values
previous_profit_loss = None  #set to NONE since no previous value in the first row

# Variables to track financial data
total_months = 0  #starts counter month at 0, and tracks total months 
pl_total = 0  #starts total net count at 0, and tracks the sum of profit/loss valuies

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader: #loops over each row, starting from 2nd row

 # --- calculate total number of months ---
        months.append(row[0])  #appends each row's month, column 0, to the months [] list

        #calculate total number of months by counting the list length
        total_months = len(months)
        
# --- calculate total profit/loss ---
        profit_loss_column = int(row[1])  #convert the profit/loss column, index 1, of current row to an integer
        pl_total += profit_loss_column #increment the total profit/loss 

# --- calculate the net change ---
        #calcualte net change
        if previous_profit_loss is not None:  #if pervious revious_profit_loss is NOT empty THEN
            net_change_value = profit_loss_column - previous_profit_loss  #subtract the current month's profit/loss value from the previous month's profit/loss
            net_change.append(net_change_value) #appends the calculated net_change_value to the net_change list

        #update previous_profit_loss to hold current month's profit/lofss for the next loop iteration
        previous_profit_loss = profit_loss_column
    
# --- calculate the average change, greatest increase, and greatest decrease  ---
        if net_change: #if there are net_change values THEN

# --- calculate the average change ---
            average_change = sum(net_change) / len(net_change)
            greatest_increase = max(net_change)
            greatest_decrease = min(net_change)

# --- find the greatest increase and decrease in profits ---
            greatest_increase_date = months[net_change.index(greatest_increase) + 1]  #find postition of greatest_increase_date and shift the index to the next month +1 in the months[] list,
            greatest_decrease_date = months[net_change.index(greatest_decrease) + 1]

        else:
            average_change = 0  #if the net change is empty, it sets the avereage change to 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${pl_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)