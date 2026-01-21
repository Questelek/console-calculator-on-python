log = open("log.txt", "a", encoding="utf-8")

#number asking function
def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number")

valid_operators = ["+", "-", "*", "/", "**", "//"]

#ask user for the first number
num1 = get_number("Enter number one: ")

#user need to enter operator
operator = input(f"Enter operator of {valid_operators}: ")
while operator not in valid_operators:
    operator = input(f"Enter operator of {valid_operators}: ")

# ask user for the second number
num2 = get_number("Enter number two: ")

# calculation
if operator == "+":
    answer = num1 + num2
    print(f"Answer: {answer}")
    log.write(f"Question: {num1, operator, num2} Answer: {answer}" "\n")

elif operator == "-":
    answer = num1 - num2
    print(f"Answer: {answer}")
    log.write(f"Question: {num1, operator, num2} Answer: {answer}" "\n")

elif operator == "*":
    answer = num1 * num2
    print(f"Answer: {answer}")
    log.write(f"Question: {num1, operator, num2} Answer: {answer}" "\n")

elif operator == "/":
    try:
        answer = num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"Answer: {answer}")
        log.write(f"Question: {num1, operator, num2} Answer: {answer}" "\n")

elif operator == "**":
    answer = num1 ** num2
    print(f"Answer: {answer}")
    log.write(f"Question: {num1, operator, num2} Answer: {answer}" "\n")

elif operator == "//":
    try:
        answer = num1 // num2
    except ZeroDivisionError:
        print("You cannot divide by zero")
    else:
        print(f"Answer: {answer}")
        log.write(f"Question: {num1, operator, num2} Answer: {answer}" "\n")

log.close()