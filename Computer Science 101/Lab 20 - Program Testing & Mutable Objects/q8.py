def update_inventory(inventory, items):
    for i in sorted(items): inventory[i] = 1 + (inventory[i] if i in inventory.keys() else 0)
    
inventory = {}
items = ["Snickers", "Mars", "Snickers", "Bounty", "M&M's Peanuts"]
update_inventory(inventory, items)
update_inventory(inventory, items)
for key in sorted(inventory.keys()):
    print(f"{key}: {inventory[key]} unit(s)")