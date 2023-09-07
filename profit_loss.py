import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read in the CSV file as a pandas dataframe
df = pd.read_csv('report.csv')

# Convert Profit/Loss column to numeric data type (remove commas and euro symbols)
#df['Profit/Loss'] = pd.to_numeric(df['Profit/Loss'].str.replace(',', '').str.replace('€', ''))

# Create a new dataframe with just the Profit/Loss and CloseTime columns
profits = df[['Profit/Loss', 'CloseTime']]

# Convert the CloseTime column to datetime format and extract only the date
profits['CloseTime'] = pd.to_datetime(profits['CloseTime'], format='%d/%m/%Y').dt.date

# Set the CloseTime column as the index of the dataframe
profits.set_index('CloseTime', inplace=True)

# Create a new column to categorize profits as positive or negative
profits['Profit Category'] = profits['Profit/Loss'].apply(lambda x: 'Profit' if x > 0 else 'Loss')

# Create a dictionary to map the Profit Category to the color
colors = {'Profit': 'green', 'Loss': 'red'}

# Create a bar chart of the profits, with green bars for profits and red bars for losses
ax = profits['Profit/Loss'].plot(kind='bar', color=profits['Profit Category'].map(colors), figsize=(12, 6), width=0.8)

# Set the x-axis tick frequency
ax.xaxis.set_major_locator(mdates.DayLocator(interval=14))

# Reverse the order of the date axis
ax.set_xlim(ax.get_xlim()[::-1])

#Add extra spacing at end
bar_spacing = -1  # Assuming 1 unit of space between each bar
current_xlim = ax.get_xlim()
ax.set_xlim(current_xlim[0], current_xlim[1] + bar_spacing)


# Set the title and axis labels
ax.set_title('Individual Trades Profit/Loss')
ax.set_xlabel('Close Date')
ax.set_ylabel('Profit/Loss (in €)')

# Set the padding for the x-axis labels
plt.gcf().subplots_adjust(bottom=0.3)

# Save the chart as a JPEG image
plt.savefig('profit_loss_chart_old.jpg', dpi=300)

# Show the chart
plt.show()

