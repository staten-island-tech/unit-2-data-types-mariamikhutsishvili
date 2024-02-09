x = int(input("Number:"))
y = int(input("Second Number:"))

def greatest_common_factor(x,y): 
    if y == 0: 
        return x
    else:
        return greatest_common_factor(y, x % y)
print("gcf is:", greatest_common_factor(x,y))
