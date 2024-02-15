import random
num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print()
x = int(input("Number:"))
if (x) == (num): print('correct')
   
    
else:
    if x < num: 
        print("try again: the number is greater")
    if x > num:
        print("try again: the number is less")
   

