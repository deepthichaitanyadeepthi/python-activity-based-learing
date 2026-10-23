# E-Commerce Order Processing

stock = 100
price = 50
revenue = 0

n = int(input("Enter number of orders: "))

for i in range(n):
    qty = int(input("Enter quantity: "))

    if qty <= 0:
        print("Invalid quantity")

    elif qty > stock:
        print("Insufficient stock")

    else:
        amount = qty * price

        if amount >= 500:
            discount = amount * 0.10
        else:
            discount = 0

        bill = amount - discount
        print("Final Bill:", bill)

        dispatch = input("Dispatch order? (yes/no): ")

        if dispatch == "yes":
            stock = stock - qty
            revenue = revenue + bill
            print("Order dispatched")

            ret = input("Return items? (yes/no): ")

            if ret == "yes":
                r = int(input("Enter return quantity: "))

                if 0 < r <= qty:
                    stock = stock + r
                    refund = (bill / qty) * r
                    revenue = revenue - refund
                    print("Refund:", refund)
                else:
                    print("Invalid return quantity")

        else:
            print("Order cancelled")

print("\n--- Final Summary ---")
print("Total Revenue:", revenue)
print("Remaining Stock:", stock)