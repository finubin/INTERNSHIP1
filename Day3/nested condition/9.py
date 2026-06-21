purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount>5000:
    discount = purchase_amount * 0.20
    print(f"Discount: {discount}")
elif purchase_amount>2000:
    discount = purchase_amount * 0.10
    print(f"Discount: {discount}")
else:
    print("No discount.")