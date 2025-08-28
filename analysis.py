
import pandas as pd
import os


# Step 1: Load the Data
# Use a delimiter argument if the data is separated by a character other than a comma (e.g., | or ;)
# For us we need to use | as the delimiter
file_name = 'inpatient.csv'
file_path = os.path.abspath(file_name)
if not os.path.exists(file_path):
	raise FileNotFoundError(f"CSV file not found at {file_path}. Please make sure 'inpatient.csv' is in the assignment folder.")
data = pd.read_csv(file_path, sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())

