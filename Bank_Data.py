import pandas as pd
import numpy as np
import os
import csv

rowcount = 0
total = 0
caverage = 0
greatinc = 0
greatd = 0
dateinc = str
dated = str


# actual path of file
#df = pd.read_csv(r'C:\Users\Owner\OneDrive\Documents\homework3\python-challenge2\PyPoll\Resources\election_data.csv')

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")
 

header = next(csv_reader)
  print(header)

    for row in csv_reader:
      print(row)
      rowcount = rowcount + 1 
      total = total + Profit/Losses
      
  with open('budget_out.csv') as csvfile:
   csvwriter = csv.writer(csvfile, delimeter = ',')

  print "Financial Analysis"
  print "-------------------"
  print " "
  print "Total Months = " rowcount
  print " "
  print "Total Profit/Loss: " total
  print " " 
  print "Average Change: " caverage
  print " "
  print "Greatest Increase In Profits: " greatinc
  print " "
  print "Greatest Decrease In Profits: " greatd
  
  
  
  
  
  
      
      
      
      







