"""
Author: Devin Ledesma
Date: 06/23/2025
File Name: ledesma_lemonadeStand.py
Description: The file calculates the cost of making lemonade and the profit from selling it.
"""

# Function to calculate total cost
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost
    return total_cost

# Function to calculate profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    profit = selling_price - total_cost
    return profit

# Variables for testing the functions
lemons_cost = 3 # Cost of lemons
sugar_cost = .75 # Cost of sugar_cost
selling_price = 6.50 # Price for lemonade

# Print variables
print("Cost of lemons: " f"${lemons_cost}")
print("Cost of sugar: " f"${sugar_cost}")
print("Price per 20 oz cup of lemonade: " f"${selling_price}")

print("""""") # Line break

# Calculate total cost to make lemonade
total_cost = calculate_cost(lemons_cost, sugar_cost)
print("Total Cost: " + f"${total_cost}")

# Calculate Profit from selling lemonade
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)
print("Profit: " + f"${profit}")