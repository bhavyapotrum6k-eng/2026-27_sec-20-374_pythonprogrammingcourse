def shopping_cart(**products):
    total = 0
    for item, price in products.items():
        print(item, ":", price, "Rs")
        total += price
    print("Total Cost:", total, "Rs")

shopping_cart(apple=15, orange=12, mango=10)