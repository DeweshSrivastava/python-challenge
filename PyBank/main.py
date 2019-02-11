import csv
import os 

#The path to the CSV file
budgetFilePath = "Resources/budget_data.csv"
# Read in the CSV file
with open(budgetFilePath, newline='') as csvfile:
   
   months =[]
   monthlyProfitsOrLosses = []
   csvreader = csv.reader(csvfile, delimiter=',')
   # Read the header row first 
   csv_header = next(csvreader)
   #Iterate through the file and save the values into a list for easier manipulation
   for row in csvreader:
      months.append(row[0])
      monthlyProfitsOrLosses.append(int(row[1]))
TotalProfitsOrLosses = 0
monthlyChange = list()
for i in range(len(monthlyProfitsOrLosses)):
   TotalProfitsOrLosses = TotalProfitsOrLosses + monthlyProfitsOrLosses[i]
   if i != 0: 
      monthlyChange.append( monthlyProfitsOrLosses[i] - monthlyProfitsOrLosses[i-1])

print(f"Total profits/losses is {TotalProfitsOrLosses}")
averageChange = sum(monthlyChange)/len(monthlyChange) 
print(f"Average change is {averageChange}")

maxIncreaseMonth = months[monthlyChange.index(max(monthlyChange))+1]
print(f"The greatest increase is {maxIncreaseMonth}  {max(monthlyChange)}")
maxDecreaseMonth = months[monthlyChange.index(min(monthlyChange))+1]
print(f"The greatest decrease is {maxDecreaseMonth}  {min(monthlyChange)}")
#Writing to the file
outputFile = open("PyBankOutput.txt", "w")
outputFile.write(f"Total profits/losses is {TotalProfitsOrLosses}\n")
outputFile.write(f"Average change is {averageChange}\n")
outputFile.write(f"The greatest increase is {maxIncreaseMonth}  {max(monthlyChange)}\n")
outputFile.write(f"The greatest decrease is {maxDecreaseMonth}  {min(monthlyChange)}\n")