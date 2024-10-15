# Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# final script should both print the analysis to the terminal and export a text file with the results. 
 
#######################################

#  -*- coding: UTF-8 -*-

#' Import necessary modules
import csv
import os

#' Files to load and output (update with correct file paths)
# file_to_load = os.path.join("/Users/Angelina/Desktop/DA_Course/classwork_Spot/challenges/03.04-Challenge-Starter_Code/03_python-challenge/PyPoll/Resources", "election_data.csv")  # Input absolute file path
# file_to_output = os.path.join("/Users/Angelina/Desktop/DA_Course/classwork_Spot/challenges/03.04-Challenge-Starter_Code/03_python-challenge/PyPoll/analysis", "election_analysis.txt")  # Output file path
file_to_load = os.path.join(".", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(".", "analysis", "election_analysis.txt")  # Output file path

#' Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}  #dictionary to store canditiates name and their vote count 


# Winning Candidate and Winning Count Tracker
winning_candidate = "" #variable will store the name of the candidate with the most votes.
winning_count = 0 #store the highest number of votes received by any candidate.


#'Open the CSV file and process it
with open(file_to_load) as election_data: #open csv file and label it election_data
    reader = csv.reader(election_data) #csv file turned into reader object

    # Skip the header row
    header = next(reader) #next(reader) = skips first row, store header row in variable header

    #' Loop through each row of the dataset and process it
    for row in reader: #starts loop at 2nd row
    
    
        #' Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 #for each loop, increment total_votes by 1 starting with 0, keeping a running total

        # Get the candidate's name from the row
        candidate_name = row[2] #extracts candidates name from 3rd column(index 2)

        # If the candidate is not already in the candidate dictionary, add them
        if candidate_name not in candidates: #if the candidate_name is NOT a key in the dictionary THEN
            candidates[candidate_name] = 0  #add new entry with the canditate_name is created with the inital vote count to 0 

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1 #increments the vote count for the candidate by 1

#' Open a text file to save the output
with open(file_to_output, "w") as txt_file: #creates text file in write mode

    # Print the total vote count (to terminal) & write to text file
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    txt_file.write("Election Results\n")  #writes the text and moves to the next line
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates.items(): #loop iterates over each candidate in the candidates dictionary.

        # Calculate the percentage of votes each candidate won
        vote_percentage = (votes / total_votes) * 100 #calculates the percentage of the total votes for each candidate

        # Print and write each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})" #print 3 digits after the decimal 
        print(candidate_results)
        txt_file.write(f"{candidate_results}\n")

        # Update the winning candidate if this one has more votes 
        if votes > winning_count: #if the current candidate has more winning votes than the previous stored (winning_count) THEN
            winning_count = votes #udpate the highest counest
            winning_candidate = candidate #update winner to current candidate 

    # Generate and print the winning candidate summary 
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    # Print and save the winning candidate summary
    print(winning_summary)
    txt_file.write(winning_summary)

print(f'Results written to {file_to_output}')