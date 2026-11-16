price = 25
quantity = 6
fee=3
cash =153

total_value = price* quantity 
total_cost = total_value + fee 



if cash >= total_cost: 
    remaining_cash = cash - total_cost 
    print("purchase affordable")
else : 
    remaining_cash = cash
    print("insufficient funds")

print(remaining_cash) 




