"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

ZyLab - 7.25
"""

def exact_change(user_total):
    
    dollars = user_total // 100
    user_total %= 100
    

    quarters = user_total // 25
    user_total %= 25


    dimes = user_total // 10
    user_total %= 10
    

    nickels = user_total // 5
    user_total %= 5
    
    pennies = user_total
    
    return (dollars, quarters, dimes, nickels, pennies)
    
if __name__ == "__main__":

    coins = int(input())
    
    (dollars, quarters, dimes, nickels, pennies) = exact_change(coins)
       
    
    if coins <= 0:
        print("no change")
        
    else:
        
        if dollars > 1:
            print(dollars, "dollars")
            
        elif dollars == 1:
            print(dollars, "dollar")
            
        if quarters > 1:
            print(quarters, "quarters")
            
        elif quarters == 1:
            print(quarters, "quarter")
        
        if dimes > 1:
            print(dimes, "dimes")
            
        elif dimes == 1:
            print(dimes, "dime")
            
        if nickels > 1:
            print(nickels, "nickels")
            
        elif nickels == 1:
            print(nickels, "nickel")
            
        if pennies > 1:
            print(pennies, "pennies")
            
        elif pennies == 1:
            print(pennies, "penny")
            


