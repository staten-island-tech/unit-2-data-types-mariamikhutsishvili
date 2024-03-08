accounts = [["1", "2", "3"], ["4", "5", "6", "7"], ["8", "9"]]
y = [[int(i) for i in x] for x in accounts]

print (x[0]) 
def getMax():
    x = sum([0])
    b = sum(y[1])
    a = sum(y[2])
    if x > b and a: 
        print(x)
    if b > x and a: 
        print(b)
    if a > b and x: 
        print(a)
