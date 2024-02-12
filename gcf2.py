def greatest_common_factor(x,y): 
    factors = []
    for i in range(1, x+1):
        if x%i == 0 and y%i == 0:
            factors.append(i)
    return factors 

x = int(input("Number:"))
y = int(input("Second Number:"))
print(greatest_common_factor[-1])

