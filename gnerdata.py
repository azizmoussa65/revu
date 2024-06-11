import pandas as pd
import numpy as np

# Generate date range
date_range = pd.date_range(start='1/1/2020', end='12/31/2020', freq='D')

# Generate random data
np.random.seed(42)  # For reproducibility
sales = np.random.randint(100, 500, size=len(date_range))
expenses = np.random.randint(50, 300, size=len(date_range))
profit = sales - expenses
regions = np.random.choice(['North', 'South', 'East', 'West'], size=len(date_range))

# Create DataFrame
data = {
    'Date': date_range,
    'Sales': sales,
    'Expenses': expenses,
    'Profit': profit,
    'Region': regions
}
df = pd.DataFrame(data)

# Display first few rows
print(df.head())

# Save to a CSV file
df.to_csv('sample_data.csv', index=False)

# Optional: Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], label='Sales')
plt.plot(df['Date'], df['Expenses'], label='Expenses')
plt.plot(df['Date'], df['Profit'], label='Profit')
plt.xlabel('Date')
plt.ylabel('Amount ($)')
plt.title('Company Sales, Expenses, and Profit over 2020')
plt.legend()
plt.show()
