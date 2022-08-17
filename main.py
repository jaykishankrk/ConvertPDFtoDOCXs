def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


print("Welcome to world of Python, May I know your name?")
get_name = input("Enter Name : ")
math_ops = ["Add", "Sub", "Mul", "Div"]
quit_loop = False
print("Hello " + get_name + ", hope you are doing well, what would you like to do today, e.g. " + str(math_ops))

while True:
    get_operation = input("Enter your choice , " + str(math_ops) + " :")
    while not quit_loop:
        get_num1_str = input("Enter Number 1 : ")
        get_num2_str = input("Enter Number 2 : ")

        if (not get_num1_str.isnumeric() and not isfloat(get_num1_str)) or (
                not get_num2_str.isnumeric() and not isfloat(get_num2_str)):
            print(get_name + ", you did not enter a valid number for either the first or second number or both, "
                         "please re-enter a valid number..! ")
            continue

        get_num1 = float(get_num1_str)
        get_num2 = float(get_num2_str)

        if get_operation.upper() == "ADD":
            print(" Addition of two number " + str(get_num1) + " and " + str(get_num2) + " is : " + str(
                get_num1 + get_num2))
            quit_loop = True

        elif get_operation.upper() == "SUB":
            print(" Subtraction of Number " + str(get_num1) + " against Number " + str(get_num2) + " is : " + str(
                get_num1 - get_num2))
            quit_loop = True

        elif get_operation.upper() == "MUL":
            print(" Multiplication of two number " + str(get_num1) + " and " + str(get_num2) + " is : " + str(
                get_num1 * get_num2))
            quit_loop = True

        elif get_operation.upper() == "DIV":
            print(
                " Division of Number " + str(get_num1) + " against " + str(get_num2) + " is : " + str(get_num1 / get_num2))
            quit_loop = True

        else:
            print("Wrong selection, you need to select within these options...  " + str(math_ops) + " Try again !!")

    loop_cont = input("Do you want to continue using the Math calculator? Type Y/y for Yes and N/n for No :")

    if loop_cont.upper() == "Y":
        quit_loop = False
        continue
    else:
        break

print("Thanks for using python " + get_name + ", have a nice day")

