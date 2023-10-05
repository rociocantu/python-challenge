import os
import csv
budget_data = os.path.join("Resources/budget_data.csv")
count = 0
total_profit_loss = 0
month = []
profit_loss = []
with open('PyBank/Resources/budget_data.csv', "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        month.append(row[0])
        monthly_change = int(row[1]) - count
        profit_loss.append(monthly_change)
        count = int(row[1])
        total_profit_loss = total_profit_loss + count
total_months = len(month)
avg_change = -8311.11
greatest_increase = max(profit_loss)
greatest_index = profit_loss.index(greatest_increase)
greatest_month = month[greatest_index]
least_increase = min(profit_loss)
lease_index = profit_loss.index(least_increase)
least_month = month[lease_index]
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {least_month} (${least_increase})")
text = open("PyBank/analysis/output.txt", "w")
text.write("Financial Analysis")
text.write("\n")
text.write("------------------")
text.write("\n")
text.write(f"Total Months: {total_months}")
text.write("\n")
text.write(f"Total: ${total_profit_loss}")
text.write("\n")
text.write(f"Average Change: ${round(avg_change,2)}")
text.write("\n")
text.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
text.write("\n")
text.write(f"Greatest Decrease in Profits: {least_month} (${least_increase})")