
def exp():
    print("""To leave EXPONENT / INDICES, enter "0" in both inputs
and choose 'y' to continue to operations menu 
or 'n' to close calculator
""")

    while 1:
        num = float(input("Enter number: "))
        exp = float(input("Enter power / exponent: "))

        if num == 0 and exp == 0:
            break

        expo = num ** exp
        expo_ans = f"{num} ^ {exp} = {expo.__round__(4)}"
        print('''--------------------------------------------------------''')
        print('>>>>   ' + expo_ans)
        print('''--------------------------------------------------------''')

