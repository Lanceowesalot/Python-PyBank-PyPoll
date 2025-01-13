

# Create a Python script that analyzes the PyBank records to calculate each of the following:
# --1  The total number of months included in the dataset
# --2  The net total amount of "Profit/Losses" over the entire period
# --3  The average of the changes in "Profit/Losses" over the entire period
# --4  The greatest increase in profits (date and amount) over the entire period
# --5  The greatest decrease in losses (date and amount) over the entire period
# --6  Print the analysis to the terminal and export a text file with the results

# Dependencies
import csv
import os

# Define Variables
months = []
profit_losses= []
#average_net_change = 0
total_months = 0
#net_change = []
change = []

# CSV Files to load
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # reader = csv.reader(csvfile)
    next(csvreader, None)
    
    # Initialize previous value for change calculation
    prev_value = None

    # Add values to lists
    for row in csvreader:
        month = row[0]
        months.append(month)
        value = int(row[1])
        profit_losses.append(value)

        # Calculate monthly change if not the first row
        if prev_value is not None:
            change.append(value - prev_value)
        prev_value = value


# More Variables to track
total_months = len(months)
net_total = sum(profit_losses)
average_change = sum(change) / len(change) if change else 0
greatest_increase = max(change) if change else 0
greatest_decrease = min(change) if change else 0

# months for greatest increase and decrease
if change:
    greatest_increase_month = months[change.index(greatest_increase) + 1]
    greatest_decrease_month = months[change.index(greatest_decrease) + 1]


# Print out results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Create a text file with the results
# output_file financial_analysis.txt'
output_file = os.path.join('Analysis', 'financial_analysis.txt')
os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure directory exists

with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("--------------------\n")
    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total: ${net_total}\n")
    datafile.write(f"Average Change: ${average_change:.2f}\n")
    datafile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    datafile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
