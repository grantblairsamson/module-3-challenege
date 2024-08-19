import csv

# Absolute path to the CSV file b/c it wouldnt work any other way LOL
file_path = r'C:\Users\User\OneDrive\Desktop\(Copy) bootcamp\Github challenges or Projects\Module 03 Challenge - Due 04-18-2024\PyPoll\Resources\election_data.csv'

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Get the candidate name from each row
        candidate = row[2]

        # Count votes per candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Prepare the election results
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"

results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file = r'C:\Users\User\OneDrive\Desktop\(Copy) bootcamp\Github challenges or Projects\Module 03 Challenge - Due 04-18-2024\PyPoll\Resources\election_results.txt'
with open(output_file, 'w') as txtfile:
    txtfile.write(results)

print(f"Analysis has been exported to {output_file}")
