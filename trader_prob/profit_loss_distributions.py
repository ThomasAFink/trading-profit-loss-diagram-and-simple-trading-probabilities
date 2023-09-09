from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm


# Set the style for the visualization
sns.set_style("whitegrid")

# Create a figure and axis
plt.figure(figsize=(12, 7))

df = pd.read_csv('../report.csv')

# Plot the distribution of Profit/Loss values
sns.histplot(df['Profit/Loss'], kde=True, color='skyblue', bins=50)

# Plot vertical lines for mean and standard deviations
mean = df['Profit/Loss'].mean()
std = df['Profit/Loss'].std()

plt.axvline(mean, color='red', linestyle='-', linewidth=1.5)
plt.axvline(mean + std, color='green', linestyle='--', linewidth=1)
plt.axvline(mean - std, color='green', linestyle='--', linewidth=1)
plt.axvline(mean + 2*std, color='yellow', linestyle='-.', linewidth=0.75)
plt.axvline(mean - 2*std, color='yellow', linestyle='-.', linewidth=0.75)

# Provide annotations
plt.text(mean, 5, 'Mean', rotation=0, color='red', fontweight='bold')
plt.text(mean + std, 5, '+1 STD', rotation=0, color='green', fontweight='bold')
plt.text(mean - std, 5, '-1 STD', rotation=0, color='green', fontweight='bold')
plt.text(mean + 2*std, 5, '+2 STD', rotation=0, color='yellow', fontweight='bold')
plt.text(mean - 2*std, 5, '-2 STD', rotation=0, color='yellow', fontweight='bold')

# Title and labels
plt.title('Normal Distribution of Trades Profit/Loss')
plt.xlabel('Profit/Loss ($)')
plt.ylabel('Frequency')

plt.show()



# Calculate probabilities
total_trades = df.shape[0]
profitable_trades = df[df['Profit/Loss'] > 0].shape[0]
loss_trades = df[df['Profit/Loss'] < 0].shape[0]
probability_profit = profitable_trades / total_trades
probability_loss = loss_trades / total_trades

# Calculate the average profit for profitable trades and average loss for loss trades
average_profit = df[df['Profit/Loss'] > 0]['Profit/Loss'].mean()
average_loss = df[df['Profit/Loss'] < 0]['Profit/Loss'].mean()

# Set the style for the visualization
sns.set_style("whitegrid")

# Parameters for the normal distribution
mean = df['Profit/Loss'].mean()
std = df['Profit/Loss'].std()

# Plotting the distribution of trades
plt.figure(figsize=(12, 7))
sns.histplot(df['Profit/Loss'], bins=30, kde=False, color='skyblue', label='Trade Distribution')
plt.title('Distribution of Trades with Normal Curve')
plt.xlabel('Profit/Loss ($)')
plt.ylabel('Number of Trades')

# Overlay the normal distribution
x = np.linspace(mean - 4*std, mean + 4*std, 1000)
plt.plot(x, norm.pdf(x, mean, std)*total_trades*(max(df['Profit/Loss']) - min(df['Profit/Loss']))/30, color='red', label='Normal Distribution')
plt.legend()
plt.show()






