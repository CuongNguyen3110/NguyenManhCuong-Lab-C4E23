import random

a = random.choice(range(10))
b = random.choice(range(10))
error = random.choice([-2,-1,0,0,0,1,2])
r = a + b + error
print(a, "+", b, "=", r) # string formatting

c = input("Nhap dap an (Y/N): ").upper()
while c != "Y" and c != "N":
    c = input("Nhap dap an (Y/N): ").upper()
if r == a + b:
    if c == "Y":
        print("Yay")
    elif c == "N":
        print("Wrong")
if r != a + b:
    if c == "Y":
        print("Wrong")
    elif c == "N":
        print("Yay")

    




