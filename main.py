from Helloworld import addition, subtraction, multiplication, division, exponent, logarithm

# This imports all files that define functions of the operations.
# The "Helloworld" describes the folder in which the files are found.

print('WELCOME TO CALEX')

# The while loop allows the user to continue using the calculator even after using a first operation
while 1:
    print('''
    NOTE: ALL INPUTS MUST BE NUMBERS (i.e No letters)
    CHOOSE YOUR OPERATION: 
    1. ADDITION
    2. SUBTRACTION
    3. MULTIPLICATION
    4. DIVISION
    5. EXPONENT / INDICES
    6. LOGARITHM
    7. EXIT
    ''')
    # This allows the user to choose an operation
    choice = input(">>>> ")

    # The if-statement makes a condition that the user chooses an operation from 1 - 7
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        if choice == '1':  # if user chooses 1, the addition function runs
            # Calls the function add(), from the file "addition" to perform the additon operation
            addition.add()

        elif choice == '2':  # if user chooses 2, the subtraction function runs
            # Calls the function sub(), from the file "subtraction" to perform the subtraction operation
            subtraction.sub()

        elif choice == '3':  # if user chooses 3, the multiplication function runs
            # Calls the function mul(), from the file "multiplication" to perform the multiplication operation
            multiplication.mul()

        elif choice == '4':  # if user chooses 4, the division function runs
            # Calls the function add(), from the file "division" to perform the division operation
            division.div()

        elif choice == '5':  # if user chooses 5, the exponent function runs
            # Calls the function add(), from the file "exponent" to perform the exponent operation
            exponent.exp()
        elif choice == '6':  # if user chooses 6, the exponent function runs
            # Calls the function log(), from the file "logarithm" to perform the logarithm operation
            logarithm.log()

        elif choice == '7':  # if user chooses 7, the calculator is closed
            break
    else:  # if the user inputs anything other than 1 to 7, the terminal print a warning
        print('INVALID INPUT!')
    stop = input("Continue?(y/n): ")  # The user is then asked whether to continue or not
    if stop in ["y", 'Y']:  # if user returns "y", the code re-runs
        pass
    elif stop in ["n", 'N']:  # if user returns "n", the code is terminated
        break
