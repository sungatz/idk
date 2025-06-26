number = [ ]
numbers = [ ]

def opr(x):
    if x%2 == 0:
        number.append(x)
    else:
        numbers.append(x)
b = (input('').split(' '))

for i in range(1, len(b)+1):
    c = opr(i)
    
def sredn(s):
    if len(s) == 0:
        print(' ')
    else: 
        e = sum(s) / len(s)
        print(e)






sredn(number)

sredn(numbers)