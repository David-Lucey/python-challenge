import os
import csv
candidate_dict = {}
candidate_name = []
csvpath = os.path.join('Resources', 'election_data.csv')
text = os.path.join('analysis', "Output.txt")
print("Election Results")
with open(text, "w+") as file: 
    file.write("Election Results")
    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}")

        for row in csvreader: 
            candidate_name = row[2]

            if candidate_name in candidate_dict:
                candidate_dict[candidate_name] += 1
            else:
                candidate_dict[candidate_name] = 1
                # print(csvreader)

            total_votes = sum(candidate_dict.values())
        # Read the header row first (skip this step if there is now header)
        #csv_header = next(csvreader)
    print("---------------------")
    file.write("---------------------")
    print(f"Total Votes: {total_votes}")
    file.write(f"Total Votes: {total_votes}")
    print("---------------------")
    file.write("---------------------")
    winner = ''
    winning_total = 0
    for key in candidate_dict:
        if winning_total < candidate_dict[key]:
            winner = key
            winning_total = candidate_dict[key]
        vote_percent = float(candidate_dict[key]) / float(total_votes) * 100
        #print(key)
        #print(candidate_dict[key])
        print(f'{key} = {vote_percent:.3f}% ({candidate_dict[key]})')
        file.write(f'{key} = {vote_percent:.3f}% ({candidate_dict[key]})')


    print("---------------------")
    file.write("---------------------")
    #print(f'{candidate_dict[candidate_name]}')
    print(f"Winner:  {winner}")
    file.write(f"Winner:  {winner}")

    #print(candidate_name[]) 
# text = float(text)
# with open('Output.txt', 'w') as file:    
#     file.write("Election Results")
#     file.write("---------------------")
#     file.write(f"Total Votes: {total_votes}")
#     file.write("---------------------")
#     file.write(f'{key} = {vote_percent:.3f}% ({candidate_dict[key]})')
#     file.write("---------------------")
#     file.write(f"Winner:  {winner}")



