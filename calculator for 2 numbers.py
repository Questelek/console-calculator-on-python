#function for get time now
def get_time():
    import datetime
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return time_now

#function for add data in log
def log_write(num1, operator, num2, answer, get_time):
    try:
        with open("log.txt", "a") as log:
            if answer is None:
                log.write(f"{get_time}   /   Question: {num1} {operator} {num2}. Answer: You cannot divide by zero." "\n")
            else:
                log.write(f"{get_time}   /   Question: {num1} {operator} {num2}. Answer: {answer}." "\n")
    except FileNotFoundError:
        print("File has been not found")

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
try:
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1 / num2
    elif operator == "**":
        answer = num1 ** num2
    elif operator == "//":
        answer = num1 // num2
except ZeroDivisionError:
    answer = None

#print of answer
if answer is None:
    print("You cannot divide by zero")
else:
    print(f"Answer: {answer}")

#answer logging
log_write(num1, operator, num2, answer, get_time())