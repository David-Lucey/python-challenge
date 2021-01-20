import os
import csv
import math

csvpath = os.path.join('Resources', 'budget_data.csv')

mydict = {}

def Budget(budget_data):
    # total_profit = sum(budget_data[1])
    profit_losses = int(budget_data[1])

    print(profit_losses)


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    budget_dict = {rows[0]:rows[1] for rows in csvreader}
    print(csvreader)
    print(budget_dict)

    for value  in budget_dict.values():
        print(value)
        total_profit = sum(budget_dict.values())
        print(total_profit)
    # # Read the header row first 
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # Months = len(csvfile.readlines())
    # print(Months) 

 