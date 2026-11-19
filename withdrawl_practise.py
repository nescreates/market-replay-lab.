balance = int(input())
withdrawal = int(input())
fee = int(input())

total_cost =  withdrawal + fee

if  balance <0  or fee <0 or withdrawal <=0 :
    remaining_balance = balance
    print("INVALID")
     
else :
   if balance  >= total_cost :
    remaining_balance = balance - total_cost
    print("approved")
   else:
    remaining_balance = balance
    print("insuffecient")
print(remaining_balance)





