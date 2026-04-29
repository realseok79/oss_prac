def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)

def mul(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    print(num1 / num2)

fir_num, cal, sec_num = input("cal:   ").split()
a = int(fir_num)
b = int(sec_num)
if cal == "+":
    add(a, b)
elif cal == "-":
    sub(a, b)
elif cal == "*":
    mul(a, b)
else:
    if b == 0:
        print("Error: zero division")
    else:
        div(a, b)
