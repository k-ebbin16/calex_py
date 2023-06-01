def mul():
    print("""To leave MULTIPLICATION, enter "0" in both inputs
and choose 'y' to continue to operations menu 
or 'n' to close calculator
""")

    while 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 == 0 and num2 == 0:
            break

        prod = num1 * num2
        prod_ans = f"{num1} × {num2} = {prod.__round__(4)}"
        print('''--------------------------------------------------------''')
        print('>>>>   ' + prod_ans)
        print('''--------------------------------------------------------''')
