grocery_list = []

def add_item(item):
    grocery_list.append(item)

def delete_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print("Item", item, "removed.")
    else:
        print("Item", item, "not found.")

while True:
    action = input(" Type 'a' to add, 'd' to delete, or 'q' to quit: ")
    if action.lower() == 'a':
        item = input("Enter the name of the item to add: ")
        add_item(item)
    elif action.lower() == 'd':
        item = input("Enter the name of the item to delete: ")
        delete_item(item)
    elif action.lower() == 'q':
        break

print("Grocery list: ")
for item in grocery_list:
    print("-", item)