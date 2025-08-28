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

# Step 2: Explore the Dataset
# Identify columns related to medical codexes (e.g., ICD, DRG, HCPCS)
codex_keywords = ['ICD', 'DRG', 'HCPCS', 'CODE', 'DIAG', 'PROC']
codex_columns = [col for col in data.columns if any(kw in col.upper() for kw in codex_keywords)]

print("\nIdentified codex-related columns:")
for col in codex_columns:
    print(f"- {col}")

# Step 3: Analyze codex columns
if len(codex_columns) < 8:
    print(f"\nWarning: Only {len(codex_columns)} codex-related columns found. Try adjusting codex_keywords or check your dataset.")
else:
    print(f"\n{len(codex_columns)} codex-related columns identified.")

codex_summary = {}
for col in codex_columns:
    print(f"\nAnalyzing column: {col}")
    null_count = data[col].isnull().sum()
    print(f"Missing/null values: {null_count}")
    # Fill missing values with placeholder for analysis
    data[col] = data[col].fillna('UNKNOWN')
    value_counts = data[col].value_counts()
    print(f"Top 5 most common codes in {col}:")
    print(value_counts.head())
    codex_summary[col] = value_counts

