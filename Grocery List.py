#Sets grocery_list variable as an empty list
grocery_list = []

#Add_item function that apppends the grocery_list with item as parameter
def add_item(item):
    grocery_list.append(item)

#Delete_item function that removes an item from the grocery_list or returns a message stating "Item not found."
def delete_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print("Item", item, "removed.")
    else:
        print("Item", item, "not found.")

#Introduces user input to select which option they would like to go with
while True:
    action = input(" Type 'a' to add, 'd' to delete, or 'q' to quit: ")
#Prompts user to enter the name of the item they would like to add and calls upon the add_item function to append the list
    if action.lower() == 'a':
        item = input("Enter the name of the item to add: ")
        add_item(item)
#Prompts user to enter the name of the item they would like to delete and calls upon the delete_item function to remove the specified item from the list
    elif action.lower() == 'd':
        item = input("Enter the name of the item to delete: ")
        delete_item(item)
#Breaks the while loop
    elif action.lower() == 'q':
        break

#Displays all the items remaining in the grocery list
print("Grocery list: ")
for item in grocery_list:
    print("-", item)
