#tip calculator

x = int(input("Subtotal"))
Service = input("How was the service")
if Service == ("bad"): 
    print(float(x))
elif Service == ("okay"):
    print(float(x*1.15))
elif Service == ("good"):
    print(float(x*1.2))
elif Service == ("great"):
    print(float(x*1.25))
