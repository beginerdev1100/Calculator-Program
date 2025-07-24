# A simple couculater script to calculate the sum of two numbers
def main():

    y = input("Whats your first number. ")
    a = input("Whats your operater +,-,*,/. ")
    x = input("Whats your second number. ")
    y = int(y)
    x = int(x)



    if a == "+":
        print(y + x)
    elif a == "-":
        print(y - x)
    elif a == "*":
        print(y * x)
    elif a == "/":
        if x == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{y} / {x} = {y / x}")
    else:
        print("Not a valid operater")

main()
