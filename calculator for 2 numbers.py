num1 = int(input("Enter a number one: ")) #ask user for the first number

question = True #variable to control the loop process

valid_operators = ["+", "-", "*", "/", "**", "//"]

while question == True:
    operator = input(f"Enter operator of {valid_operators}: ") #user need to enter operator

    if operator in valid_operators:
        num2 = int(input("Enter a number two - ")) #ask user for the second number

        if operator == "+":
            print(f"Answer: {num1 + num2}")
        elif operator == "-":
            print(f"Answer: {num1 - num2}")
        elif operator == "*":
            print(f"Answer: {num1 * num2}")
        elif operator == "/":
            print(f"Answer: {num1 / num2}")
        elif operator == "**":
            print(f"Answer: {num1 ** num2}")
        elif operator == "//":
            print(f"Answer: {num1 // num2}")
        #calculation
        break
    else:
        print("It isn´t a valid operator") #informing user about invalid operator

    if input("Do you want continue your tries? Enter Yes or No - ") not in ["Yes", "yes", "y", "Y"]:
        question = False
    #asking user for continue