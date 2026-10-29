# Module 10 Lab: Inventory List manager

# Reflection 1: What is the most surprising thing about how lists work in Python compared to what you expected coming in?

# I am suprised with the flexibility of lists in Python. I expected them to be more rigid and less dynamic, but they can easily be modified and sorted in different ways.

# Reflection 2: Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.

# In my business stastics class, we had to manually insert data from 70 homes into excel and then calculate the average price of homes in a neighborhood. If I had used a Python list, I could have easily stored the prices and calculated the average with just a few lines of code, saving a lot of time.

print("--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #first
print(inventory[1]) #last
middle = len(inventory) // 2
print(inventory[middle]) #middle

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) #first three
print(inventory[-2:]) #last two
print(inventory[::2]) #every other item

print("--- Exercise 4: Modifying the List ---")
inventory.append("envelope")

print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2))  # Apply a 10% discount

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")