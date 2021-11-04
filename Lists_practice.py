cities=["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities)
print(type(cities))
colors=["Orange", "Blue", "Yellow", "Pink", "Red", "Purple", "Brown", "Black", "White", "Green"]
print(colors)
print(cities[-3])
print(cities[2])
print(cities[0])


print(colors[-10])
print(colors[-1])
print(colors[4])


print(cities[0:4])
top_cities=cities[0:4]
print(top_cities)


cities[0]="San Francisco"
cities[2]="Brooklyn"
cities[-3]="Hollywood"
cities[5]="Tampa"
print(cities)
cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0,"Miami")
print(cities)


del cities[4]
cities.pop(-4)
cities.remove("Memphis")
print(cities)