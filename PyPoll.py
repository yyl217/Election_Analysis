#1. Open the data file.
#2. Write down the names of all the candidates.
#3. Add a vote count for each candidate.
#4. Get the total votes for each candidate.
#5. Get the total votes cast for the election.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

#file_to_save = os.path.join("analysis", "election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Hello World")