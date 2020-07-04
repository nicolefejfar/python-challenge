import os
import csv
py_poll_csv = os.path.join("Resources", "election_data.csv")

# Create variables.
vote_count = {}
total_votes = 0
max_vote_count = 0
winner = ""

# Open file and skip header.
with open(py_poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)

    # Loop through each row to find candidate and vote count per candidate.
    for row in csvreader:
        candidate_name = row[2]
        total_votes += 1
        if candidate_name not in vote_count:
            vote_count[candidate_name] = 1
        else:
            vote_count[candidate_name] += 1

# Create text file to write print statements to.
output_file = os.path.join("analysis", 'py_poll_analysis.txt')
with open(output_file, "w") as txtFile:

    # Print header and total vote counts to terminal and txt file.
    print("Election Results\n","-" *50, sep="")
    print("Election Results\n","-" *50, sep="", file = txtFile)
    print('Total Votes: ', str(total_votes), "\n","-" * 50, sep="")
    print('Total Votes: ', str(total_votes), "\n","-" * 50, sep="", file = txtFile)
    
    # Calculate candidate counts, percentages and winner, print to terminal and txt file.
    for candidate_name, vote_count in vote_count.items():
        vote_percent = round((vote_count / total_votes * 100), 3)
        print(f'{candidate_name}: {vote_percent}% ({vote_count})')
        print(f'{candidate_name}: {vote_percent}% ({vote_count})', file = txtFile)
        if vote_count > max_vote_count:
            winner = candidate_name
            max_vote_count = vote_count
    print("-" * 50, "\n", "The winner is: ", winner, "\n","-" * 50, sep="")
    print("-" * 50, "\n", "The winner is: ", winner, "\n","-" * 50, sep="", file = txtFile)