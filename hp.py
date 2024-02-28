h = int(input("Number of hungerpoints"))
a = int(input("Number of Apples"))
s = int(input("number of seconds"))
h = min(h,a)
if (h) < 1 or (h)  > 100000:
    print("h error")
if (a) < 1 or (a)  > 100000:
    print("a error")
if (s) < 1 or (s)  > 100000:
    print("s error")
else:
    if (h-s) < 0:
        print(0)
    else: 
        print(h-s) 
