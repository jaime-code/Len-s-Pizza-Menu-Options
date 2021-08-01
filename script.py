# Len's Pizza Slices

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

# how many $2 pizza
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

# how many pizza toppings
num_pizzas = len(toppings)
#print(num_pizzas)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# two-dimensional list that shows one pizza toppings and an associated price
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#print(pizza_and_prices)

# sorting pizza prices by ascending order
pizza_and_prices.sort()
#print(pizza_and_prices)

# set index 0 to the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

# set index -1 as the most expensive pizza 
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

# someone has purchased the last anchovies pizza, will need to remove it from the option, and will need to replace it with peppers a new item
pizza_and_prices.pop(-1)
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Someone request the 3 cheapest pizzas
three_cheapest = pizza_and_prices[0:3]
print("These are our 3 cheapest pizza's " + str(three_cheapest))