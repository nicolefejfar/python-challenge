import os
import csv
py_poll_csv = os.path.join("Resources", "election_data.csv")

# Create variables.
count = 0
candidate_list = []
unique_candidate_list = []
vote_count_list = []
vote_percent_list = []

# Open file and create header.
with open(py_poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    print("\nElection Results\n","-" *50, sep="")

# Loop through each row to find and calculate values.
    for row in csvreader:
        count += 1
        candidate_list.append(row[2])
# Loop through unique candidate list to calculate values.
    for candidate in set(candidate_list):
        unique_candidate_list.append(candidate)
        vote_count = candidate_list.count(candidate)
        vote_count_list.append(vote_count)
        vote_percent = round((vote_count / count) *100, 3)
        vote_percent_list.append(vote_percent)
# Determine winner.
    winning_vote_count = max(vote_count_list)
    winner = unique_candidate_list[vote_count_list.index(winning_vote_count)]

# Print results to terminal.
print('Total Votes: ', str(count), "\n","-" * 50, sep="")
for candidate in range(len(unique_candidate_list)):
            print(unique_candidate_list[candidate] + ": " + str(vote_percent_list[candidate]) +"% (" + str(vote_count_list[candidate])+ ")")
print("-" * 50, "\n", "The winner is: ", winner, "\n","-" * 50, sep="")

# Create and write results to txt file.
output_file = os.path.join("analysis", 'py_poll_analysis.txt')
with open(output_file, "w") as txtFile:
    print("Election Results\n","-" *50, sep="", file = txtFile)
    print('Total Votes: ', str(count), "\n","-" * 50, sep="", file = txtFile)
    for candidate in range(len(unique_candidate_list)):
            print(unique_candidate_list[candidate] + ": " + str(vote_percent_list[candidate]) +"% (" + str(vote_count_list[candidate])+ ")", file = txtFile)
    print("-" * 50, "\n", "The winner is: ", winner, "\n","-" * 50, sep="",  file = txtFile)