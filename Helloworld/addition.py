def add():
    print("""To leave ADDITION, enter "0" in both inputs
and choose 'y' to continue to operations menu 
or 'n' to close calculator
""")

    while 1:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num1 == 0 and num2 == 0:
            break
        summation = num1 + num2
        sum_ans = f"{num1} + {num2} = {summation.__round__(4)}"
        print('-----------------------')
        print('>>>>   ' + sum_ans)
        print('-----------------------')
