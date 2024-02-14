def calculate_order_total(order, inventory):
    total_price = 0
    for i in order:
        item = i[0]
        count = i[1]
        price = inventory[item]
        total_price += price * count
    return total_price
    
inventory = {'Snickers Bar': 0.99, 'Mars Bar': 0.99, 'Crunchie Bar': 0.99, 'Pepsi 355ml Can': 1.15, 'Pepsi Max 355ml Can': 1.15, 'Coke 355ml Can': 1.2, 'Coke Zero 355ml Can': 1.2}
order = [("Snickers Bar", 3), ("Mars Bar", 2), ("Pepsi Max 355ml Can", 5)]
print(f"The order total is ${round(calculate_order_total(order, inventory), 2)}")