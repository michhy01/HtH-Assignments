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

#step IX
def all_printed_cities(list):
    for el in list:
        print(el)
    return "All cities are printed"


#Step X

def reorganized_list(list):
    print(list)
    counter = 0 

    while counter < len(list):
        item1 = list[counter]
        item2 = list[counter - 1]

        if len(item1) >= len(item2):
            counter += 1
            continue
        elif counter + 1 == len(list) - 1:
            break
        else:
            list.remove(item1)
            list.append(item1)
            counter += 1

    return list

print(all_printed_cities(cities))
print(reorganized_list(cities))