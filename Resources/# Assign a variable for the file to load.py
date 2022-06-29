# Assign a variable for the file to load and the path.
file_to_load = 'Desktop/Modules/Election_Analysis/Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load,'r')
# Open the election results and read the file
with open(file_to_load) as election_data:

  



   import csv
     
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Desktop/Modules/Election_Analysis/Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)