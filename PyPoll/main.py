#import dependencies
import os
import csv
csvpath = os.path.join('..', 'election_data.csv')

#change

#how to read csv file
with open(csvpath, newline = '') as csvfile:

    #skip header line
    csv_header = next(csvfile)

    #track variables
    number_votes = 0
    candidates = []
    vote_count = []


    #count votes
    for row in csvfile:
        number_votes = number_votes + 1

    #create candidate list
        candidate = row[2]
    #if candidate has votes, add to tally    
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1

        else 
            candidates.append(candidate)
            vote_count.append(1)
    
    
    #calculate percentage of votes
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    #find percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/num_votes*100
        percentages.append(vote_percentage)
            if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# creating the new txt file
new_file = open("Output/PyPoll_analysis.txt", "w")

# writing the text file
new_file.write("Election Results")
new_file.write("--------------------------")
new_file.write(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    new_file.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
new_file.write("---------------------------")
new_file.write(f"Winner: {winner}")
new_file.write("---------------------------")
