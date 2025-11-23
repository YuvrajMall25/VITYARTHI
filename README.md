deliveries, order_id = {}, 1

def place_order():
    global order_id
    name, item, address = input("
Customer Name: "), input("Item to Deliver: "), input("Delivery Address: ")
    deliveries[order_id] = {"name": name, "item": item, "address": address, "status": "Preparing for delivery"}
    print(f"
Order placed successfully! Your Order ID is: {order_id}
")
    order_id += 1

def update_status():
    oid = int(input("
Enter Order ID: "))
    if oid in deliveries:
        status_map = {"1": "Preparing for delivery", "2": "Out for delivery", "3": "Delivered"}
        choice = input("Choose status (1: Preparing, 2: Out, 3: Delivered): ")
        if choice in status_map:
            deliveries[oid]["status"] = status_map[choice]
            print("Status updated successfully!
")
        else:
            print("Invalid choice.
")
    else:
        print("Order ID not found.
")

def check_order():
    oid = int(input("
Enter Order ID: "))
    if oid in deliveries:
        o = deliveries[oid]
        print(f"
Order ID: {oid}
Customer: {o['name']}
Item: {o['item']}
Address: {o['address']}
Status: {o['status']}
")
    else:
        print("Order not found.
")

def show_all_orders():
    if deliveries:
        print("
--- All Delivery Orders ---")
        for oid, info in deliveries.items():
            print(f"Order {oid}: {info['item']} for {info['name']} - {info['status']}")
        print()
    else:
        print("No orders yet.
")

def main():
    actions = {"1": place_order, "2": update_status, "3": check_order, "4": show_all_orders}
    while True:
        print("
====== Delivery Service Menu ======")
        print("1. Place New Order
2. Update Delivery Status
3. Check Order Status
4. Show All Orders
5. Exit")
        choice = input("Choose an option: ")
        if choice == "5":
            print("Thank you for using the Delivery Service System!")
            break
        actions.get(choice, lambda: print("Invalid option. Try again.
"))()

main()
