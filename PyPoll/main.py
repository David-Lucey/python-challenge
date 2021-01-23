import os
import csv
candidate_dict = {}
# candidate_name = []
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

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
    print(f"CSV Header: {csv_header}")
    print(candidate_dict)
    print(f"Total Votes: {total_votes}")
     

    # with open(csvpath) as csvfile:

       
        # csvreader = csv.reader(csvfile, delimiter=',')
        # poll_dict = {rows[0]:rows[2] for rows in csvreader}
        # #print(poll_dict)
