def div():
    print("""To leave DIVISION, enter "0" in both inputs
and choose 'y' to continue to operations menu 
or 'n' to close calculator""")

    while 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 == 0 and num2 == 0:
            break

        div = num1 / num2
        div_ans = f"{num1} / {num2} = {div.__round__(4)}"
        print('''--------------------------------------------------------''')
        print('>>>>   ' + div_ans)
        print('''--------------------------------------------------------''')
