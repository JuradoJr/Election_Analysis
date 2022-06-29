# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load,'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


file_to_save =os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
     txt_file.write("Arapahoe\nDenver\nJefferson")





# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:   
     file_reader = csv.reader(election_data)
     headers=next(file_reader)
     print(headers) 
 
 