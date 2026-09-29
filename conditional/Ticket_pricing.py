age=int(input("Enter your age:"))
day= (input("Enter the day"+" "))

price=12 if age>=18 else 8


# For Discount on Wednesday
if day=="Wednesday":
    price=price-2

print("Your ticket price is : $",price)