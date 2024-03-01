y = (input("last name:")).upper()
x = y[0]
def first_initial(x):
    if x in ["A", "B", "C", "D", "E", "F", "G"]:
     print('101')
    elif x in ["H", "I", "J", "K", "L", "M", "N", "O", "P"]:
      print('102')
    else:
     print('103')

first_initial(x)