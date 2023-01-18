import csv

# Initialize variables to store the results
months = 0
net_profit = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Open the CSV file
with open('budget_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    # Loop through the rows in the CSV
    for row in reader:
        # Increment the number of months
        months += 1
        
        # Add to the net profit
        net_profit += int(row["Profit/Losses"])
        
        # Calculate the change in profit from the previous row
        if months > 1:
            profit_change = int(row["Profit/Losses"]) - int(prev_profit)
            profit_changes.append(profit_change)
            
            # Check if this is the greatest increase or decrease
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = row["Date"]
                greatest_increase[1] = profit_change
            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row["Date"]
                greatest_decrease[1] = profit_change
        
        # Store the current row's profit for the next iteration
        prev_profit = int(row["Profit/Losses"])

# Calculate the average change in profit
avg_change = sum(profit_changes) / len(profit_changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
