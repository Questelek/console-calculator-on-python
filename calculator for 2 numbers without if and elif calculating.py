import operator

#function for get time now
def get_time():
    import datetime
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return time_now

#function for add data in log
def log_write(num1, user_operator, num2, answer, get_time):
    try:
        with open("log.txt", "a") as log:
            if answer is None:
                log.write(f"{get_time}   /   Question: {num1} {user_operator} {num2}. Answer: You cannot divide by zero." "\n")
            else:
                log.write(f"{get_time}   /   Question: {num1} {user_operator} {num2}. Answer: {answer}." "\n")
    except FileNotFoundError:
        print("File has been not found")

#number asking function
def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number")

valid_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow,
    "%": operator.mod,
}

#function to get keys of valid operators
valid_operators_keys = []
for el in valid_operators.keys():
    valid_operators_keys.append(el)

num1 = get_number("Enter number one: ")

#user need to enter operator
user_operator = input(f"Enter operator of {valid_operators_keys}: ")
while user_operator not in valid_operators_keys:
    user_operator = input(f"Enter operator of {valid_operators_keys}: ")

num2 = get_number("Enter number two: ")

#calculation
try:
    answer = valid_operators[user_operator](num1, num2)
except ZeroDivisionError:
    answer = None

#print of answer
if answer is None:
    print("You cannot divide by zero")
else:
    print(f"Answer: {answer}")

#answer logging
log_write(num1, user_operator, num2, answer, get_time())