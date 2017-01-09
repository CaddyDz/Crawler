# Lists acts like arrays in Python but must be stored between brackets and separated by commas
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
# List's items can be accessed by index
print("First Item", grocery_list[0])  # Output First Item Juice
# Accessing indexes directly adds a space between the printed string and item automagically
# therefor, formatting the string should be explicitly defined
print("First Item{item}".format(item=grocery_list[0]))  # Output First ItemJuice
# List's items can be updated, deleted in place
grocery_list[0] = "Green Juice"

print("First Item", grocery_list[0])  # Output Green Juice

# List's items can be accessed by range using colon
# Note that the last index won't be included
print(grocery_list[1:3])  # Output ['Tomatoes', 'Potatoes']

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
# Lists can contain lists within and accessed simply as nested lists
to_do_list = [other_events, grocery_list]
print(to_do_list[0][0])  # Output Wash Car
# We can append items to lists
grocery_list.append("Onion")
print(to_do_list)
# Use insert instead of append to add an item on a specific index
grocery_list.insert(1, "sth")
print(to_do_list)
# Use the remove function to remove items from a list
grocery_list.remove("sth")
print(grocery_list)  # Outputs ['Green Juice', 'Tomatoes', 'Potatoes', 'Bananas', 'Onion']
grocery_list.sort()
print(grocery_list)  # Sort the list alphabetically
del grocery_list[0]
print(grocery_list)
to_do_list2 = other_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))