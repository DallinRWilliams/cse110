"""
File: shopping_cart.py
Author: Dallin Williams

Purpose: Use lists and loops to store items with assigned integers and display the list of items and the sum of their integers.
"""

item_list = []
price_list = []
item = None

print()
print("Welcome to the Shopping Cart Program!\n")

print("""
Please Select One of the Following:\n
1. Add Item
2. View cart
3. Remove item
4. Compute total
5. Quit\n
""")

selection = int(input("Please Enter an Action: "))

for i in range(len(item_list)):
    print(f"{i+1}: {item_list[i]}")