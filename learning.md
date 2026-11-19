**what does the programe do ?

programe can compare the cash avaible  with the total cost 
When affordable, subtract the total cost from the available cash: cash - total_cost
Otherwise, display insufficient cahs and keep the cash unchanged
when the cash equals the total cost the purchase is affordable and remaining cash becomes 0.


**Why the fee is included in the affordability check ?

fee is included because it is part of the total cost

**What happens when cash equals the total cost?

would print out the purvhase is affordable

**One mistake you fixed and what you learned:

I forgot to add the colon after the if statement so i added that 
I learnt the the order of the varables you are comparing does matter and can affect what the programe does 
Also both paths must give remaining_cash a value before it's printed .




why zero is allowed for the fee but rejected for the price?

0 is allowed for the fee because it specifcally add the equal operator to 0 in order for it to not be rejected
0 as the price is rejected beu=cuse it only state price being greater than 0 not equal to 0 .
a zero fee means no charge; our purchase model requires a positive price.

Why validation comes before affordability
We need to make sure the inputs being given make sense. For instance, if the price was negative, subtracting a negative total cost from our cash could increase our remaining cash incorrectly.

That’s why validation comes first. If the inputs pass validation, then we can ask: “Are we able to afford this purchase?”
How the inner and outer else differ
The outer else handles invalid inputs. It prints “Invalid purchase inputs” and leaves the cash unchanged.

The inner else handles valid inputs when the purchase isn’t affordable. It prints “Insufficient cash” and also leaves the cash unchanged.
Which parts needed hints
I struggled with indentation and remembering to give remaining_cash a value in every possible path.

When the purchase is affordable, I subtract the total cost from the cash. When it’s rejected, I keep the cash unchanged.

I also needed help remembering to print the remaining cash once at the end, outside the conditions.

I sometimes mix up greater-than (>) and less-than (<), but I’m getting better. The open side faces the larger value. 

Why does True mean rejection in this validation check?
The condition checks whether any purchase input is invalid:
- Price is zero or negative.
- Quantity is zero or negative.
- Fee is negative.
With or, at least one check must be True for the whole condition to be True.

True therefore means an invalid input was found, so the program prints “Invalid purchase inputs”.

If all three checks are False, the program follows else and prints “Valid purchase inputs”.

Validation happens before affordability. If any invalid-input condition is true, the withdrawal is rejected—even if there is enough money.