def greatest_common_factor(x,y): 
    gcf = []
    for i in range(1, x+1):
        if x%i == 0 and y%i == 0:
            gcf.append(i)
    return gcf [-1]

x = int(input("Number:"))
y = int(input("Second Number:"))
gcf = greatest_common_factor(x,y)
print("gcf is:", greatest_common_factor(x,y))

