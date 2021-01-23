import os
import csv
import math

csvpath = os.path.join('Resources', 'budget_data.csv')
text = os.path.join('analysis', "Output.txt")
mydict = {}
with open(text, "w+") as file: 
    def Budget(budget_data):
        # total_profit = sum(budget_data[1])
        profit_losses = int(budget_data[1])

        print(profit_losses)
        file.write(profit_losses)


    with open(csvpath) as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        budget_dict = {rows[0]:int(rows[1]) for rows in csvreader}
        #print(csvreader)
        # print(budget_dict)

        switch = False
        previous = 0
        total_change = 0
        change_counter = 0
        increase = 0
        increase_month = ""
        decrease = 0
        decrease_month = ""

        for month  in budget_dict:
            value = budget_dict[month]
            if switch == True:

                dif = value - previous
                total_change = total_change + dif
                change_counter += 1
                if increase < dif:
                    increase = dif
                    increase_month = month
                if decrease > dif:
                    decrease = dif
                    decrease_month = month
            # print(value)
            total_profit = sum(budget_dict.values())
            # print(total_profit)
            switch = True
            previous = value
    print("Financial Analysis")
    file.write("Financial Analysis")
    print("-----------------------")
    file.write("-----------------------")
    print(f"Total Months: {len(budget_dict)}")
    file.write(f'Total Months: {len(budget_dict)}')
    print(f"Total: {total_profit}")
    file.write(f'Total: {total_profit}')
    avg_change = total_change / change_counter
    avg_change = round(avg_change, 2)
    print(f'Average Change: {avg_change}')
    file.write(f'Average Change: {avg_change}')
    print(f"Greatest Increase in Profits: {increase_month} (${increase})")
    file.write(f"Greatest Increase in Profits: {increase_month} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")
    file.write(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")
    #print(increase)


