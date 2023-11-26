import pandas as pd
import numpy as np
import os
import csv

votecount = 0
Charles = 0
Diana = 0
Raymon = 0
count = 0
winner = str

# actual path of file 
# df = pd.read_csv(r'C:\Users\Owner\OneDrive\MSU Bootcamp\homework\03_challenge\Starter_Code (2)\Starter_Code\python-challenge2\PyPoll\Resources\election_data.csv')

election_data_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_data_csv) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")

header = next(csv_reader)
print(header)
  
for row in csv_reader:
      print(row)
      votecount = votecount + 1 
      
      if (row, 3) == "Charles Casper Stockham":
          Charles = Charles + 1
      elif (row, 3)  == "Diana DeGette":
           Diana = Diana + 1
      else
            Raymon = Raymon + 1
next            
      
if Charles < Diana > Raymon:
    Diana = count
    winner = "Diana DeGette"
elif   Diana < Raymon > Charles:
      Raymon = count
      winner = "Raymon Anthony Doane"
else 
        Charles = count
        winner = "Charles Casper Stockham"  

with open('election_out.csv') as csvfile:
   csvwriter = csv.writer(csvfile, delimeter = ',')


print "Election Results"
print "-------------------"
print "Total Votes = " votecount
print "----------------------"
print "Charles Casper Stockholm: " Charles
print "Diana DeGette: " Diana
print "Raymon Anthony Doane: " Raymon
print "------------------------"
print "Winner: " winner  " with " count " votes"
print "------------------------"
