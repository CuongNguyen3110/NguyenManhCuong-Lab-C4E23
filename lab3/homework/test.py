while True:

    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    x = int(input("Nhap x: "))

    if b < a <= b + x:
        print("True")
    else:
        print("False")