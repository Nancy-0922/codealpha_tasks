import pandas as pd

# Load the CSV file
csv_file = "google_play_10_app_reviews.csv"

# Read the CSV into a DataFrame
df = pd.read_csv(csv_file)

# Save as Excel file
excel_file = "google_play_10_app_reviews.xlsx"
df.to_excel(excel_file, index=False)

print(f"✅ CSV file '{csv_file}' converted to Excel and saved as '{excel_file}'")
