import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Employees.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove decimal places in the Age column
df['Age'] = df['Age'].astype(int)

# Convert USD salary to EGP
df['Salary(USD)'] = df['Salary(USD)'] * 31

# Print some stats
print('Average age:', df['Age'].mean())
print('Median salary:', df['Salary(USD)'].median())
print('Male/Female ratio:', df['Gender'].value_counts(normalize=True))

# Write the data to a new CSV file
df.to_csv('Employees Updated.csv', index=False)
