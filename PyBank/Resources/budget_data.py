import csv
import os

# Absolute path to the CSV file b/c it wouldnt work any other way LOL
file_path = r'C:\Users\User\OneDrive\Desktop\(Copy) bootcamp\Github challenges or Projects\Module 03 Challenge - Due 04-18-2024\PyBank\Resources\budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit_loss = None
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Count the total number of months
        total_months += 1
        
        # Calculate the net total profit/loss
        net_total += profit_loss
        
        # Calculate the change from the previous month
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            # Check for greatest increase in profits
            if change > greatest_increase['amount']:
                greatest_increase['date'] = date
                greatest_increase['amount'] = change
                
            # Check for greatest decrease in profits
            if change < greatest_decrease['amount']:
                greatest_decrease['date'] = date
                greatest_decrease['amount'] = change
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Prepare the analysis results
analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the analysis to the terminal
print(analysis)

# Export the results to a text file
output_file = r'C:\Users\User\OneDrive\Desktop\(Copy) bootcamp\Github challenges or Projects\Module 03 Challenge - Due 04-18-2024\PyBank\Resources\financial_analysis.txt'
with open(output_file, 'w') as txtfile:
    txtfile.write(analysis)

print(f"Analysis has been exported to {output_file}")