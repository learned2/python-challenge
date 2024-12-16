# -*- coding: UTF-8 -*-
"""
PyPoll Main Script

Author: Stan Usovicz
Created 12/11/2024

Description: returns total votes, vote counts and % for each candidate, and the winner and outputs in election_analysis.txt

"""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidates_vote = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = None
win_vote_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        ballotID = row[0]
        county = row[1]
        candidate_name = row[2]

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
           candidates.append(candidate_name)
           candidates_vote[candidate_name] = 0
           
        # Add a vote to the candidate's count
        candidates_vote[candidate_name] += 1

    # Print the total vote count (to terminal)
    print(f"--------------------------\n"
          f"Total Votes: {total_votes}\n")

# Generating output 
output = (
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------\n"
)

# Loop through the candidates to determine voting % and add to output
for candidate, votes in candidates_vote.items():
    vote_percentage = (votes / total_votes) * 100  
    output += (f"{candidate}: {vote_percentage:.2f}% ({votes})\n")

    #print each candidate vote count to terminal
    print(f"{candidate}: {vote_percentage:.2f}% ({votes})\n")

    # Determine winning candidate
    if votes > win_vote_count:
        win_vote_count = votes
        winning_candidate = candidate

# Add winning candidate to output
output += (
    f"--------------------------\n"
    f"Winning Candidate: {winning_candidate}\n"
    f"--------------------------\n"
)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
