price = - 35
quantity = 4
fee = 3
cash = 200


if price > 0 and quantity > 0 and fee >= 0 :
    

       total_value = price * quantity
       total_cost = total_value + fee

       if cash >= total_cost  :
           remaining_cash = cash - total_cost

           print("Purchase Affordable") 

  

       else :
            remaining_cash = cash 
 
            print("Insufficient cash") 
else :
     remaining_cash = cash 
     print("invalid purchase inputs")
 
print(remaining_cash)




 