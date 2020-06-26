import os
import csv
py_bank_csv = os.path.join("Resources", "budget_data.csv")

# Create variables.
total_months = 0
net_value = 0
value_change = 0
previous_value = 0
sum_value_change = 0
greatest_increase = 0
greatest_decrease = 0

# Open file, update header, calculate data.
with open(py_bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    print("\nFinancial Analysis\n","-" *50, sep="")
    for row in csvreader:
        current_value = int(row[1])
        net_value += current_value
        if (total_months) > 0:
            row[0] = "month"
            value_change = current_value - previous_value
            sum_value_change += value_change
            previous_value = current_value
            if value_change > greatest_increase:
                greatest_increase = value_change
                greatest_increase_month = "month"
            if value_change < greatest_decrease:
                greatest_decrease = value_change
                greatest_decrease_month = "month"
        else:
            previous_value = current_value
        total_months += 1
avg_value_change = sum_value_change / (total_months - 1)

# Print summary to terminal.
print(f'Total Months: {total_months}')
print(f'Total: ${net_value}')
print(f'Average Change: ${round(avg_value_change, 2)}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

# Create & print summary to text file.
output_file = os.path.join('analysis', 'py_bank_analysis.txt')
with open(output_file, "w") as txtFile:
    print("Financial Analysis\n","-" *50, sep="", file = txtFile)
    print(f'Total Months: {total_months}', file = txtFile)
    print(f'Total: ${net_value}', file = txtFile)
    print(f'Average Change: ${round(avg_value_change, 2)}', file = txtFile)
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})', file = txtFile)
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})', file = txtFile)