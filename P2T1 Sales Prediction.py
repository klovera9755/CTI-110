#CTI-110
#P2T1-Sales Prediction
#Adam Klover
#06/17/18

# Get the projected total sales.
total_sales = float(input('Enter the projected total sales: '))

# Calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

# Display the profit.
print('The profit is $' , format(profit, ',.2f'))
