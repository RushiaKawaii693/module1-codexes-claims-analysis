# Medicare Inpatient Claims Data Analysis Report

## Steps Taken in Analysis
1. **Data Loading:** Imported the CMS Synthetic Medicare Inpatient Claims dataset using Pandas, ensuring the correct delimiter ('|') and verifying file existence.
2. **Dataset Exploration:** Inspected the dataset structure and identified columns related to medical codexes (ICD, DRG, HCPCS, etc.) using keyword-based search.
3. **Codex Column Analysis:** For each codex column, calculated the frequency of unique codes, checked for missing/null values, and filled them with a placeholder ('UNKNOWN').
4. **Summary of Most Common Codes:** Printed the top 5 most common codes for ICD, DRG, and HCPCS columns.
5. **Pattern Analysis:** Explored relationships between codex codes and region/demographic columns (e.g., state, age, gender) to identify any notable patterns or trends.

## Purpose of Each Part of the Code
- **Data Loading:** Ensures the dataset is accessible and correctly formatted for analysis.
- **Column Identification:** Finds all relevant codex columns for further analysis, regardless of naming variations.
- **Frequency Analysis:** Highlights the most common diagnoses and procedures, providing insight into prevalent health issues.
- **Missing Data Handling:** Prevents errors and bias by filling missing values, ensuring robust analysis.
- **Pattern Analysis:** Investigates relationships between codes and patient/region characteristics to uncover trends.

## Key Findings
- Multiple codex columns were identified, including primary and secondary diagnosis/procedure codes.
- The most common ICD, DRG, and HCPCS codes represent frequent diagnoses and procedures in the dataset.
- Some codes are highly prevalent in specific regions or among certain patient groups (e.g., age, gender), suggesting geographic or demographic trends.
- Missing data was present in several codex columns but was successfully handled by filling with a placeholder.

## Challenges Faced & Solutions
- **File Format Issues:** Ensured the correct delimiter was used and added file existence checks to avoid runtime errors.
- **Column Name Variability:** Used keyword-based searches to robustly identify codex columns, even with inconsistent naming.
- **Missing Data:** Addressed missing/null values by filling with a placeholder, allowing for complete frequency analysis.
- **Pattern Analysis:** Required flexible code to handle varying region/demographic columns across datasets.

## Implications for Healthcare Providers & Policy Makers
- Identifying common codes helps providers understand prevalent health issues and allocate resources effectively.
- Patterns by region or demographics can inform targeted interventions and policy decisions.
- Robust data analysis supports better decision-making and highlights areas for further investigation or improvement.

## Most Common Findings

Based on the analysis in `analysis.py`, the following codes were found to be the most common in the dataset:

- **ICD Codes:** The top 5 most frequent ICD codes represent the most common diagnoses among inpatient claims. These codes appeared significantly more often than others, indicating prevalent health conditions in the dataset.
- **DRG Codes:** The most common DRG codes correspond to the most frequently billed diagnosis-related groups, reflecting typical inpatient procedures or treatments.
- **HCPCS Codes:** The top HCPCS codes highlight the most common procedures and services provided to patients.Top 5 codes being 99221, G0444, 96156, 99408 and lastly 99495 with 99221 being the most appeared at 8298 entries. 

Additionally, the analysis revealed:
- Certain ICD and DRG codes are more prevalent in specific regions or among particular patient groups (such as age or gender), suggesting geographic or demographic trends in healthcare utilization.
- Missing values were present in several codex columns but were successfully handled by filling with a placeholder, ensuring complete analysis.

These findings provide insight into the most frequent diagnoses, procedures, and patterns in the synthetic Medicare inpatient claims data, which can help inform resource allocation and policy decisions.


