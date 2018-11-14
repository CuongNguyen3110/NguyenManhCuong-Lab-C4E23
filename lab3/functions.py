a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
op = input("Nhap phep toan: ")

while op != "+" and op != "-" and op != "*" and op != "/":
    op = input("Nhap phep toan: ")
    if op == "+":
        print(a + b)
    if op == "-":
        print(a - b)
    if op == "*":
        print(a * b)
    if op == "/":
        print(a / b)