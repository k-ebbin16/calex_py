import math


def log():
    print("""To leave ADDITION, enter "0" in both inputs
and choose 'y' to continue to operations menu 
or 'n' to close calculator
""")

    while 1:

        num = float(input("Enter number: "))
        base = float(input("Enter log base: "))

        if num == 0 and base == 0:
            break
        log = math.log(num, base)
        log_ans = f"log({num}) base({base}) = {log.__round__(4)}"
        print('-----------------------')
        print('>>>>   ' + log_ans)
        print('-----------------------')
