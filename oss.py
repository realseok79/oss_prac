fir_num, cal, sec_num = input("cal:   ").split()
a = int(fir_num)
b = int(sec_num)
if cal == "+":
    print(a+b)
elif cal == "-":
    print(a - b)
elif cal == "*":
    print(a * b)
else:
    if b == 0:
        print("Error: zero division")
    else:
        print(a / b)
