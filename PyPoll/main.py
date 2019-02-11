import csv
import os 
import numpy as np
import operator

#The path to the CSV file
electionDataFilePath = "Resources/election_data.csv"

# Read in the CSV file
with open(electionDataFilePath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    candidateVotedFor = []
    for row in csvreader:
        candidateVotedFor.append(row[2])
numberOfVotes = len(candidateVotedFor)
print(f"The total number of votes are {numberOfVotes}")
#A list holding the candidates who recieved votes
uniqueCandidatesNames = np.unique(candidateVotedFor)
from collections import Counter
countedVotes = Counter(candidateVotedFor)

for key, value in countedVotes.items():
    print(f"Candidate {key} got {value} votes = {value/numberOfVotes*100}%")
