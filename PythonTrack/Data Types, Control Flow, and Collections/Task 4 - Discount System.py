#Task 4 - Discount System
purchase_amount = eval(input("Enter purchase amount: "))

if purchase_amount >= 5000:
    discount_applicable = purchase_amount * 0.2
    print("Discount Applied: ",discount_applicable)
    final_amount = purchase_amount - discount_applicable
elif purchase_amount >= 3000:
    discount_applicable = purchase_amount * 0.1
    print("Discount Applied: ",discount_applicable)
    final_amount = purchase_amount - discount_applicable
else:
    final_amount = purchase_amount
    print("No discount applied")

print("Purchase Amount: ",final_amount)
