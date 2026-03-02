# Practice List Operations

# Create an Empty List
my_shopping_list = []
print(my_shopping_list)

# Add Items using append()
my_shopping_list.append("Apples")
print(my_shopping_list)

my_shopping_list.append("Bread")
print(my_shopping_list)

my_shopping_list.append("Milk")
print(my_shopping_list)

# Insert Item using insert()
my_shopping_list.insert(1, "Eggs")
print(my_shopping_list)

# Access Elements (Indexing)
print("First item:", my_shopping_list[0])
print("Last item:", my_shopping_list[-1])
print("Item at index 2:", my_shopping_list[2])

# Extract Sub-lists (Slicing)
print("First two items:", my_shopping_list[:2])
print("Items from index 2:", my_shopping_list[2:])
print("Reversed list:", my_shopping_list[::-1])

# Remove Item by Value using remove()
my_shopping_list.remove("Bread")
print(my_shopping_list)

# Remove Item by Index using pop()
popped_item = my_shopping_list.pop(0)
print("Popped item:", popped_item)
print(my_shopping_list)

# Add More Items for Sorting
my_shopping_list.append("Bananas")
my_shopping_list.append("Cheese")
my_shopping_list.append("Avocado")
print(my_shopping_list)

# Sort the List
my_shopping_list.sort()
print(my_shopping_list)

# Get Length
print("List length:", len(my_shopping_list))