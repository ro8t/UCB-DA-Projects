# Dependencies
import os
import csv
import pandas as pd

# Retrieving the file
file = os.path.join('budget_data.csv')

# Opening the file
with open(file, newline='') as data:
    budget = csv.reader(data, delimiter=',')
    budget_header = next(budget)
    print(f"The Headers are: {budget_header}")

    # Stores the data into a df via pandas
    budget_data = pd.DataFrame([row for row in budget])

# Sets the column names to their original names
budget_data = budget_data.rename(columns={0: str(budget_header[0]),
                                          1: str(budget_header[1])})

print('```')
print('Financial Analysis Descriptive Statistics')
print('-----------------------------------------')

# 1. The total months in the data set

total_months = len(budget_data['Date'])
question_one = f"There are {total_months} months in the data set."
print(question_one)

# 2. The net total amount of "Profit/Losses" over the entire period

    # Grab the data into seperate variable
pl = list(budget_data['Profit/Losses'].values)
    # Converts profit/loss column into integers
pl = [int(num) for index, num in enumerate(pl)]

    # Sums up the profit/loss column
total_pl = 0
for n in pl:
    total_pl += n

question_two = f"The net total amount of Profit/Losses over the entire period is: ${float(total_pl)}."
print(question_two)


# 3. The average of the changes in "Profit/Losses" over the entire period

pl_difference = []
for index, number in enumerate(pl[0:len(pl) - 1]):
    pl_difference.append(pl[index + 1] - pl[index])

    # Calculating mean change in P/L
mean_diff = round(sum(pl_difference) / len(pl_difference), 2)

question_three = f"The average of the changes in Profit/Losses over the entire period is : ${mean_diff}."
print(question_three)

# 4. The greatest increase in profits (date and amount) over the entire period

greatest_pi = max(pl_difference)

largest_date = budget_data.iloc[pl_difference.index(greatest_pi), 0]

question_four = f"Greatest increase in profits happened in {largest_date} with the amount of (${greatest_pi})."
print(question_four)

# 5. The greatest decrease in losses (date and amount) over the entire period

worst_pi = min(pl_difference)

worst_date = budget_data.iloc[pl_difference.index(worst_pi), 0]

question_five = f"Greatest decrease in profits happened in {worst_date} with the amount of (${worst_pi})."

print(question_five)
print('```')

with open("PyBank Results.txt", "w") as pybank:

    pybank.write('```\n')
    pybank.write('Financial Analysis Descriptive Statistics\n')
    pybank.write('-----------------------------------------\n')
    pybank.write(question_one + '\n')
    pybank.write(question_two + '\n')
    pybank.write(question_three + '\n')
    pybank.write(question_four + '\n')
    pybank.write(question_five + '\n')
    pybank.write('-----------------------------------------\n')
    pybank.write('```')

    pybank.close()

