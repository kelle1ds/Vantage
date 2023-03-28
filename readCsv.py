import csv
import time
 
# opening the CSV file
with open('numbers.csv', mode ='r') as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)
        time.sleep(5)
        