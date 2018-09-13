#import dependencies
import os
import csv
csvpath = os.path.join('..', 'budget_data.csv')

#how to read csv file
with open('budget_data.csv', newline = ',') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header line
    csv_header = next(csvfile)

    #track variables
    total_months = 0
    total_profit_loss = 0
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_month_increase = ''
    greatest_month_decrease = ''

    #count months and profit/losses
    for row in csvfile:
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row[1])

        if int(row[1]) >= greatest_increase:
            greatest_increase = int(row[1])
            greatest_month_increase = row[0]

        if int(row[1]) <= greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_month_decrease = row[0]
    
    #calculate average change
    average_change = round(total_profit_loss / total_months,2)

print("Financial Analysis")
print("--------------------------------------------")    
print("Total Months: " + str(total_months))
print(f"Total: " + str(total_profit_loss))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + greatest_month_increase + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Revenue: " + greatest_month_decrease + " ($" + str(greatest_decrease) + ")")

# creating the new txt file
new_file = open("Output/PyBank_analysis.txt", "w")

# writing the text file
new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write("Total Months: " + str(total_months) + "\n")
new_file.write("Total Revenue: $" + str(total_revenue) + "\n")
new_file.write("Average Revenue Change: $" + str(average_change) + "\n")
new_file.write("Greatest Increase in Revenue: " + greatest_month_increase + " ($" + str(greatest_increase) + ")" + "\n")
new_file.write("Greatest Decrease in Revenue: " + greatest_month_decrease + " ($" + str(greatest_decrease) + ")" + "\n")

