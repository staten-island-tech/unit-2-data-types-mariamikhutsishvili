import random
num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
z = ('Incorrect')
incorrectanswers = []

while z == ('Incorrect'):
    x = int(input("Number:"))
    if (x) == (num): 
        print('correct')
        z = ('Correct')
    
    else:
        incorrectanswers.append(x)
        if x < num: 
            print("try again: the number is greater")
        if x > num:
            print("try again: the number is less")
    
        print(incorrectanswers)
