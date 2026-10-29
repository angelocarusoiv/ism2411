# Self - Assesment Questions - Angelo Caruso

#1: The first bug I spotted was the second part because it obvious was missing a comma in the loop statement. I found it on my own.

#2: apply_discount(price, tier) is a fuction that includes 2 arguments and returns a price based on the tier.

#3 I used Google Gemini 3.6 flash to help me find the bugs in the broken_sales.py file. AI helped build my understanding but it also shortcuted it.

# Exercise 1

# Define calculate tax funtion

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# Write it out manually first, then refactor into a function

discounted = apply_discount(price, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    final = final_price(price, tier, 0.07)
    print(f"Order: ${price:.2f}, Tier: {tier}, Final Price: ${final:.2f}")

# Exercise 5

# # broken_sales.py - trace and diagnose before fixing anything.
# sales = [120, 80, 250, 175, 90]

# total = 0
# for sale in sales:
#     total += sale
# print(f"Total: ${total}")

# # before: prints a single sale
# # how to fix: add "+" to the print statement to concatenate the sale value

# count = 0
# for sale in sales:
#     count += 1
# print(f"Count: {count}")

# # before: mising the comma in the loop statement
# # how to fix: simply add a comma after the "for sale in sales" statement to separate the loop variable from the print statement

# i = 0
# while i < len(sales):
#     print(sales[i])
#     i += 1

# before: IndexError: list index out of range
# how to fix: change the while loop condition to "i < len(sales)" to

# Exercise 6

x = 100 #apple

def double_it():
    x = 999 # another apple
    return x * 2

print(x)
print(double_it())
print(x)