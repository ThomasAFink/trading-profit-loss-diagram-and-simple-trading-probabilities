import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('../report.csv')

# Extract the Profit/Loss data
profits = df['Profit/Loss']


# Calculate the number of profitable and loss-making trades
num_profitable = len(profits[profits > 0])
num_loss = len(profits[profits <= 0])

# Calculate the probabilities of profit and loss
prob_profit = num_profitable / len(profits) * 100
prob_loss = num_loss / len(profits) * 100

print("Prob of profit: ", prob_profit, "Prob of loss: ", prob_loss)



# Calculate the overall net profit
net_profit_loss = profits.sum()

print("Net of profit/loss: ",net_profit_loss)




# Calculate mean and standard deviation
mean_profit = profits.mean()
std_deviation = profits.std()


# Categorize trades based on size
categories = ['Small Loss', 'Medium Loss', 'Large Loss', 'Small Profit', 'Medium Profit', 'Large Profit']

# Calculate probabilities for each category
small_loss_prob = len(profits[(profits <= 0) & (profits > mean_profit - std_deviation)]) / len(profits) * 100
medium_loss_prob = len(profits[(profits <= mean_profit - std_deviation) & (profits > mean_profit - 2*std_deviation)]) / len(profits) * 100
large_loss_prob = len(profits[profits <= mean_profit - 2*std_deviation]) / len(profits) * 100

small_profit_prob = len(profits[(profits > 0) & (profits < mean_profit + std_deviation)]) / len(profits) * 100
medium_profit_prob = len(profits[(profits >= mean_profit + std_deviation) & (profits < mean_profit + 2*std_deviation)]) / len(profits) * 100
large_profit_prob = len(profits[profits >= mean_profit + 2*std_deviation]) / len(profits) * 100

category_probs = [small_loss_prob, medium_loss_prob, large_loss_prob, small_profit_prob, medium_profit_prob, large_profit_prob]

# Plotting the categorized trade sizes
plt.figure(figsize=(14, 8))
bars = plt.bar(categories, category_probs, color=['#FF9999', '#FF6666', '#FF3333', '#99FF99', '#66FF66', '#33FF33'], alpha=0.7)

# Adding annotations to bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}%',
             ha='center', va='bottom', color='black', weight='bold', fontsize=10)

plt.title('Probability of Trade Profit/Loss Sizes')
plt.ylabel('Probability (%)')
plt.ylim(0, max(category_probs) + 10)  # Add some padding to the y-axis limit for better visualization
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()
plt.show()


