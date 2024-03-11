accounts = [["1", "2", "3"], ["4", "5", "6", "7"], ["8", "9"]]

def max(accounts):
    int_accounts = [[int(i) for i in x] for x in accounts]
    largest = 0
    for money in int_accounts:  
        x = sum(money)
        if x > largest: 
            largest = x 
        print (largest)

def max(accounts):
    int_accounts = [[int(i) for i in x] for x in accounts]
    z = [sum(i) for i in int_accounts]
    return(max(z))