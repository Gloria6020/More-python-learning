#list = used to store to store multiple items in asingle variable
food = ["pizza", "meat", "cheese"]
food[0]="sishi"

#print(food[0])` is printing the first item in the `food` list.
print(food[0])


# `food.append("ice_cream")` is adding the item "ice_cream" to the end of the `food` list.
food.append("ice_cream")
# `food.remove("meat")` is removing the item "meat" from the `food` list.
food.remove("meat")
#food.pop()` removes and returns the last item in the `food` list.
food.pop()
# `food.insert(0, "cake")` is inserting the item "cake" at the beginning of the `food` list, shifting
# all other items to the right.
food.insert(0, "cake")
# `food.sort()` is sorting the items in the `food` list in alphabetical order.
food.sort()
# `food.clear()` is removing all the items from the `food` list, making it an empty list.
food.clear()

for x in food:
    print(x)