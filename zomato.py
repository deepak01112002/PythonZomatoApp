# Initialize data structures
menu = []
orders = {}

# Function to add a new dish to the menu
def add_dish():
    dish_id = input("Enter dish ID: ")
    dish_name = input("Enter dish name: ")
    price = float(input("Enter price: "))
    stocks = int(input("Enter stocks: "))
    availability = input("Enter availability (yes/no): ")
    
    # Check if dish ID already exists
    for dish in menu:
        if dish['dish_id'] == dish_id:
            print("Dish ID already exists.")
            return
    
    # Add the new dish to the menu
    menu.append({
        'dish_id': dish_id,
        'dish_name': dish_name,
        'price': price,
        'stocks': stocks,
        'availability': availability
    })
    print("Dish added successfully.")

# Function to get all dishes
def get_all_dishes():
    print("Menu:")
    for dish in menu:
        print(f"ID: {dish['dish_id']}, Name: {dish['dish_name']}, Price: {dish['price']}, Stocks: {dish['stocks']}, Availability: {dish['availability']}")

# Function to remove a dish from the menu
def remove_dish():
    dish_id = input("Enter dish ID to remove: ")
    
    # Find the dish with the given ID and remove it
    for dish in menu:
        if dish['dish_id'] == dish_id:
            menu.remove(dish)
            print("Dish removed successfully.")
            return
    
    print("Dish not found.")

# Function to update dish availability
def update_availability():
    dish_id = input("Enter dish ID to update availability: ")
    availability = input("Enter new availability (yes/no): ")
    
    # Find the dish with the given ID and update its availability
    for dish in menu:
        if dish['dish_id'] == dish_id:
            dish['availability'] = availability
            print("Availability updated successfully.")
            return
    
    print("Dish not found.")

# Function to take a new order
def take_order():
    customer_name = input("Enter customer's name: ")
    dish_ids = input("Enter dish IDs (comma-separated): ").split(',')
    
    order_id = len(orders) + 1
    order_status = 'received'
    
    # Check if each dish is available
    for dish_id in dish_ids:
        dish_found = False
        for dish in menu:
            if dish['dish_id'] == dish_id:
                dish_found = True
                if dish['availability'] == 'no':
                    print(f"Dish {dish_id} is not available.")
                    return
                break
        if not dish_found:
            print(f"Dish {dish_id} does not exist.")
            return
    
    # Process the order
    orders[order_id] = {
        'customer_name': customer_name,
        'dish_ids': dish_ids,
        'status': order_status
    }
    print(f"Order placed successfully. Order ID: {order_id}")

# Function to update order status
def update_order_status():
    order_id = int(input("Enter order ID to update status: "))
    new_status = input("Enter new status: ")
    
    # Find the order with the given ID and update its status
    if order_id in orders:
        orders[order_id]['status'] = new_status
        print("Order status updated successfully.")
    else:
        print("Order not found.")

# Function to review all orders
def review_orders():
    print("Orders:")
    for order_id, order in orders.items():
        print(f"Order ID: {order_id}, Customer: {order['customer_name']}, Status: {order['status']}").pretty()
        print("Dish IDs: ", end="")
        for dish_id in order['dish_ids']:
            print(dish_id, end=" ")
        print()

# Function to exit the application
def exit_app():
    print("Exiting the application...")
    # Additional cleanup or closing of resources if needed
    exit()

# Main loop for user interface
while True:
    print("\n========== Food Inventory Application ==========")
    print("1. Add a new dish to the menu")
    print("2. Get all dishes")
    print("3. Remove a dish from the menu")
    print("4. Update dish availability")
    print("5. Take a new order")
    print("6. Update order status")
    print("7. Review all orders")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        add_dish()
    elif choice == '2':
        get_all_dishes()
    elif choice == '3':
        remove_dish()
    elif choice == '4':
        update_availability()
    elif choice == '5':
        take_order()
    elif choice == '6':
        update_order_status()
    elif choice == '7':
        review_orders()
    elif choice == '8':
        exit_app()
    else:
        print("Invalid choice. Please enter a valid option (1-8).")
