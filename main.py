symbol = "DEMO"
price = 80
fee = 4
cash = 250

quantity = 3
total_value = price * quantity 
total_cost = total_value + fee


if cash >= total_cost:
    remaining_cash = cash  - total_cost 
    print("Purchase affordable")
else :
    remaining_cash = cash
    print("Insufficient cash")
   


 
print(symbol)
print (price)

print(total_value)
print(total_cost)

print(remaining_cash)






