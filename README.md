# 03_python-challenge
[PyBank.py Completed Assignment](https://github.com/wrighang/03_python-challenge/blob/main/PyBank/main.py)

[PyPoll.py Completed Assignment](https://github.com/wrighang/03_python-challenge/blob/main/PyPoll/main.py)

## PyBank Instructions

In this challenge, you are tasked with creating a Python script to analyze the financial records of your company.
You will be given a financial dataset called `budget_data.csv`. The dataset is composed of two columns:
- "Date"
- "Profit/Losses"

Your task is to create a Python script that analyzes the records to calculate each of the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

## PyBank Instructions

In this challenge, you are tasked with creating a Python script to analyze the financial records of your company.
You will be given a financial dataset called `budget_data.csv`. The dataset is composed of two columns:
- "Date"
- "Profit/Losses"

Your task is to create a Python script that analyzes the records to calculate each of the following values:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

## Requirements

## Correctly Reads in the CSV
Reads in the CSVs for both PyBank and PyPoll using Python:
- Reads and stores header row

## Results Printed to Terminal
Results correctly display for PyBank:
- Total Months
- Total
- Average Change
- Greatest Increase
- Greatest Decrease

Results correctly display for PyPoll:
- Total Votes
- Each candidate’s total votes and percent of votes
- Winner

## Code Runs Error Free
- Runs without errors
- Produces consistent results

## Exports Results to Text File
The text file contains the following for PyBank:
- Total Months
- Total
- Average Change
- Greatest Increase
- Greatest Decrease

The text file contains the following for PyPoll:
- Total Votes
- Each candidate’s total votes and percent of votes
- Winner

## Code is Cleaned and Commented
- Additional tests and debugging removed
- Code is properly commented

------------------------

PyBank- I began with looking at the Excel sheet to see how I would solve for intended results. After I was able to solve it in Excel, I began writing the python code and broke it out into section to follow the path of how I would solve it manually in Excel. I was able to calculate the # number of month, however, i had trouble figuring out how to do the sum of the profit/loss column and used learning assistance for help to better understand the adding of the increments. There were a few other road blocks along the way with how to structure the code and i used learning assistant to explain what i was trying to achieve which helped. I also used it for finding out how to create and write to a text file. The final py doc is the cleaned up version from the various attemps I had made to achieve the correct result. 

PyPoll- I begin looking at Excel to solve this sheet as well, however, it was a bit tricker as I couldn't figure out how to capture unique values. In Thursdays class, it was suggested to create a dictionay which then I applied to my code and with some xpert assistant i was able to figure out how to call out the unique candidates as well as count the votes. 

For both .py docs i created comments throughout to code to illustrate my thought process and understanding of what each line is doing.
