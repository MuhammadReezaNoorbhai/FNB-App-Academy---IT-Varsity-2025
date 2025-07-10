foods = []
prices = []
total = 0 

while True:
    food = input("Enter a food to buy or press X to exit: ")
    if food.lower() == 'x':
        break
    else:
        price = float(input(f"Please enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("----YOUR CART----")

for food in foods:
    print(food)
for price in prices:
    total = total + price
    
print(f"Your total is: R{total}")