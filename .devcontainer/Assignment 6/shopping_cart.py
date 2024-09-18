cart = []

def add_item(cart, item):
    cart.append(item)
    print(f"{item} added to the cart. Current cart: {cart}")

def remove_item(cart, item):
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from the cart. Current cart: {cart}")
    else:
        print(f"{item} not found in the cart.")

def update_quantity(cart, index, new_item):
    if 0 <= index < len(cart):
        old_item = cart[index]
        cart[index] = new_item
        print(f"Replaced {old_item} with {new_item}. Current cart: {cart}")
    else:
        print(f"Invalid index. Cart remains unchanged: {cart}")

# Sample loop for user interaction
while True:
    print("\n1. Add item\n2. Remove item\n3. Update item\n4. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        item = input("Enter item to add: ")
        add_item(cart, item)
    elif choice == 2:
        item = input("Enter item to remove: ")
        remove_item(cart, item)
    elif choice == 3:
        index = int(input("Enter the index to update: "))
        new_item = input("Enter new item: ")
        update_quantity(cart, index, new_item)
    elif choice == 4:
        break
    else:
        print("Invalid option. Try again.")
