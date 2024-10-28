
first_number = int(input("Please include the first number you want to operate with: "))
second_number = int(input("Please include the second number you want to operate with: "))
def addition(a, b):
    output = a + b
    return output
add = addition(a = first_number, b = second_number)
def multiplication(a, b):
    output = a * b
    return output
multiply = multiplication(a = first_number, b = second_number)
operations = input("Do you want to multiply or add? Type 'add' or 'multiply': ")
continue_operating = True
while continue_operating:
    if operations == 'multiply'.lower():
        ask_for_continue = input("Do you want to continue operating? ")
        if ask_for_continue == "yes":
            contnue = float(input("Add your number: "))
            multiply *= contnue
            print(multiply)
        else:
            print(multiply)
            continue_operating = False
            exit()
    elif operations == "add":
        ask_for_continue = input("Do you want to continue operating? ")
        if ask_for_continue == "yes".lower():
            contnue = input("Add or multiply? ")
            if contnue == "multiply":
                user_ask = float(input("Multiply a number: "))
                add *= user_ask
                print(add)
            elif contnue == "add":
                user_ask = float(input("Add a number: "))
                add += user_ask
                print(add)
        elif ask_for_continue == "No".lower():
            ask_for_continue = False
            exit()
    else:
            print("Invalid Entry")
            exit()
