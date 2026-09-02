products={
    1:("Rice",50),
    2:("wheat",30),
    3:("sugar",40),
    4:("salt",20),
    5:("oil",100),
    6:("milk",60),
    7:("soap",30),
    8:("Biscuits",25),
    9:("chocolate",80),
    10:("tea",90)
}
print("==========BILLING SYSTEM==========")
print("1. Rice -50")
print("2. wheat -30")
print("3. sugar -40")
print("4. salt -20")
print("5. oil -100")
print("6. milk -60")
print("7. soap -30")
print("8. Biscuits -25")
print("9. chocolate -80")
print("10. tea -90")
cart=[]
while True:
    choice=int(input("Enter your choice: "))
    if choice ==0:
       print("Thank you for using Billing system!")
       break
    if choice not in products:
       print("Invalid choice. Please select a valid product number.")
       continue
    Quantity=int(input("Enter the Quantity"))
    name,price=products[choice]
    Total=price*Quantity
    cart.append((name,Quantity,price,Total))
    print(f"Added to cart: {name} - Quantity: {Quantity}, Price: {price}, Total: {Total}")

#add dicount 
subtotal=0
subtotal+=sum(item[3] for item in cart)

discount=subtotal*0.1
amount_after_discount=subtotal-discount
#GST
gst=amount_after_discount*0.05

#final amount
grand_total=amount_after_discount+gst

print("--------------------------------")
print(f"subtotal: {subtotal:.2f}")
print(f"discount: {discount:.2f}")
print(f"GST: {gst:.2f}")
print(f"grand total: {grand_total:.2f}")
print("================================")
print("Thank you!")
