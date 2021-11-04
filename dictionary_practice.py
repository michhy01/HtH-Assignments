food_prices={"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}
print(food_prices)
print(type(food_prices))
print()
people_age={"Luna": 20, "Kitty": 25, "Mauricio": 4, "Rowena": 16}
print(people_age)

print(food_prices["Chicken"])
print(food_prices["Beef"])
print(food_prices["Cheese"])
print(food_prices["Milk"])
print()
print(people_age["Luna"])
print(people_age["Kitty"])
print(people_age["Mauricio"])
print(people_age["Rowena"])
print()
shoes_instore={"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
print(shoes_instore)
print(shoes_instore["SB Dunk"] - 2)
print(shoes_instore["Yeezy"] + 1)
print(shoes_instore["Jordan 13"] + 7)
print(shoes_instore["Yeezy"] + 7)
print(shoes_instore["Foamposite"] + 7)
print(shoes_instore["Air Max"] + 7)
print(shoes_instore["SB Dunk"] + 7)
print(shoes_instore["Jordan 13"] -3)
print(shoes_instore["Yeezy"] - 3)
print(shoes_instore["Foamposite"] - 3)
print(shoes_instore["Air Max"] - 3)
print(shoes_instore["SB Dunk"] -3)
shoes_instore["Vans"]=13
shoes_instore["Converse"]=25
shoes_instore["Nike"]=5
print(shoes_instore)
del shoes_instore["Nike"]
del shoes_instore["Yeezy"]
print(shoes_instore)


#Python Operators, Iteration, and Functions
# Step II
def total_price(menu_item, menu_item2):
    return food_prices[menu_item] + food_prices[menu_item2]
print("The total price of beef and cheese is $ " + str(total_price("Beef", "Cheese")))

#Step III
def price_difference(menu_item, menu_item2):
    total_diff= food_prices[menu_item] - food_prices[menu_item2] 
    return abs(total_diff)
print ("The difference between beef and cheese is $ " + str(price_difference("Beef", "Cheese")))

#Step IV
def shoes_restock(shoe, num):
    shoes_instore[shoe] *= num
    return shoes_instore
print(shoes_restock("Air Max", 3))

#Step V
def clearance(shoe, num):
    shoes_instore[shoe] /= num
    return shoes_instore
print(clearance("SB Dunk", 2))

#Step VI
def shoe_demand(shoe, num):
    shoes_instore[shoe] **= num
    return shoes_instore
print(shoe_demand("Converse", 2))