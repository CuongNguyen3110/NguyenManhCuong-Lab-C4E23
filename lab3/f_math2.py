from random import randint, choice
from calc_func import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    error = choice([-2,-1,0,0,0,1,2])
    op_list = ["+", "-", "*", "/"]
    op = choice(op_list)
    r = eval(x, y, op) + error
    return x, y, op, r

a, b, op, r = generate_quiz()
print(a, op, b, "=", r) # string formatting

c = input("Nhap dap an (Y/N): ").upper()
while c != "Y" and c != "N":
    c = input("Nhap dap an (Y/N): ").upper()
if error == 0:
    if c == "Y":
        print("Yay")
    if c == "N":
        print("Wrong")
else:
    if c == "Y":
        print("Wrong")
    if c == "N":
        print("Yay")
