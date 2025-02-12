import pandas as pd

# Read the CSV file
df = pd.read_csv('dates.csv')

# Convert the "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the minimum and maximum dates
min_date = df['Date'].min()
max_date = df['Date'].max()

# Print the results
print(f"Date range: {min_date.date()} to {max_date.date()}")
