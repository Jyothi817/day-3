Marked_price=float(input("Enter the Marked price: "))
Discount_percent=float(input("Enter the discount percentage: "))
discount=(Discount_percent*Marked_price)/100
Final_price = Marked_price - discount
print("the final price is ", Final_price)