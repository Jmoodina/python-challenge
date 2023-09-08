"""
PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
Your task is to create a Python script that analyzes the votes and calculates each of the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote
"""

# Import Dependancies
import os
import csv

# Set csv Filepath
PyPollcsv = "Resources\\election_data.csv"

# Create variables and lists to use
votes = []
vote_per_candidate = []
cadidates = []
unique_candidate = []

count = 0

# Open the CSV using the set path PyPollcsv

with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

# Calculate the total number of votes and append
    for row in csvreader:
        count = count + 1
        cadidates.append(row[2])
        
# Calculate and create a set to find all the unique candidates
    for z in set(cadidates):
        unique_candidate.append(z)
        total_votes = cadidates.count(z)
        votes.append(total_votes)
        votes_percent = (total_votes/count)*100
        vote_per_candidate.append(votes_percent)

# Assign the winner
    winning_votes = max(votes)
    winner = unique_candidate[votes.index(winning_votes)]
    
# Print and compare the results
print("Election Results")   
print("-------------------------")
print(f"Total Votes :{count}")    
print("-------------------------")
for x in range(len(unique_candidate)):
            print(unique_candidate[x] + ": " + str(vote_per_candidate[x]) +"% (" + str(votes[x])+ ")")
print("-------------------------")
print(f"The winner is: {winner}")
print("-------------------------")

# Create a text file to place the results
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes :{count} \n")
    text.write("-------------------------\n")
    for x in range(len(unique_candidate)):
        text.write(unique_candidate[x] + ": " + str(vote_per_candidate[x]) +"% (" + str(votes[x])+ ")\n")
    text.write("-------------------------\n")
    text.write(f"The winner is: {winner} \n")
    text.write("-------------------------\n")