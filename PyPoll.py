# Dependencies
import os
import csv
import pandas as pd
import numpy as np

# Retrieving the file
file = os.path.join('election_data.csv')

# Opening the file
with open(file, newline='') as data:
    election = csv.reader(data, delimiter=',')
    election_header = next(election)
    #print(f"The Headers are: {election_header}")

    # Stores the data into a df via pandas
    election_data = pd.DataFrame([row for row in election])

# Sets the column names to their original names®
election_data = election_data.rename(columns={0: str(election_header[0]),
                                              1: str(election_header[1]),
                                              2: str(election_header[2])})

#print(election_data.head())
print('```')
print('Election Results')
print('--------------------------')

# 1. Total number of votes
total_votes = len(election_data['Voter ID'])
question_1 = f"Total Votes: {total_votes}"

print(question_1)
print('--------------------------')

# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won

candidate_list = list((election_data['Candidate'].value_counts()).index) # No.2
candidate_votes = [] # No.4

for i in election_data['Candidate'].value_counts():
    candidate_votes.append(i)

percent_votes = [round((v / total_votes) * 100, 2) for v in candidate_votes] # No.3

for name, per, num in zip(candidate_list, percent_votes, candidate_votes):
    print(f"{name}: has {per}% of all votes with ({num}) votes")

print('--------------------------')

# 5. The winner of the election based on popular vote

winning_percentage = max(percent_votes)
win_index = percent_votes.index(winning_percentage)
winning_candidate = candidate_list[win_index]

print(f"The winner is: {winning_candidate}")
print('--------------------------')
print('```')

