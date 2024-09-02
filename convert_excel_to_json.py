import pandas as pd

# Load Excel file
df = pd.read_excel('student _reports.xlsx')

# Convert to JSON
data_json = df.to_json(orient='records')

# Save JSON to file
with open('student_reports.json', 'w') as f:
    f.write(data_json)
