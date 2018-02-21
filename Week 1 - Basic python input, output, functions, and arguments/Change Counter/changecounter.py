q = input("How many quarters? ")
print("*"*int(q))
d = input("How many dimes? ")
print("*"*int(d))
n = input("How many nickels? ")
print("*"*int(n))
p = input("How many pennies? ")
print("*"*int(p))

def countChange():
    print(int(q)+int(d)+int(n)+int(p))

countChange()
