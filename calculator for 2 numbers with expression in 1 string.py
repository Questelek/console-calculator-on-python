import operator

#function for get time now
def get_time():
    import datetime
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return time_now

#function for data logging
def log_write(num1, user_operator, num2, answer, get_time):
    try:
        with open("log.txt", "a") as log:
            if answer is None:
                log.write(f"{get_time}   /   Question: {num1} {user_operator} {num2}. Answer: You cannot divide by zero." "\n")
            else:
                log.write(f"{get_time}   /   Question: {num1} {user_operator} {num2}. Answer: {answer}." "\n")
    except FileNotFoundError:
        print("File with log has been not found")

#func to parse user's expression
def parse_expression(expression_string):

    #delete of " "
    expression_string = expression_string.replace(" ", "")

    num1 = ""
    num2 = ""
    operator = None

    current_index = 0
    expression_length = len(expression_string)

    #main func's loop
    while current_index < expression_length:
        current_char = expression_string[current_index]

        #dot as float interpretation
        if current_char.isdigit() or current_char in ".":
            if operator is None:
                num1 += current_char
            else:
                num2 += current_char

        #interpritation of minus
        elif current_char == "-":
            if current_index == 0 or expression_string[current_index - 1] in "+-*/%":
                #minus as "number"
                if operator is None:
                    num1 += current_char
                else:
                    num2 += current_char
            else:
                #minus as operator
                operator = "-"

        #correct "*" and "**" interpretation
        elif current_char == "*":
            try:
                if current_index != 0 and expression_string[current_index + 1] in "*":
                    if operator is None:
                        operator = "**"
                        current_index += 1
                    else:
                        return None
                else:
                    operator = "*"
            except IndexError:
                return None

        #else operators
        elif current_char in "+/%":
            try:
                if operator is not None:
                    #user cant enter more as 1 operator
                    return None
                operator = current_char
            except ValueError:
                return None

        #check for digit
        else:
            return None

        current_index += 1

    #func for get count of dot
    def dot_count(number):
        dot_count = number.count(".")
        return dot_count

    #check for dots count. User cant input more as 1 dot per number
    if dot_count(num1) > 1 or dot_count(num2) > 1:
        return None

    #final check
    if not num1 or not num2 or operator is None:
        return None

    return float(num1), operator, float(num2)

valid_operators = {
    "**": operator.pow,
    "%": operator.mod,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

#main loop
while True:
    expression = input("Enter your question - ")

    try:
        result = parse_expression(expression)
    except ValueError:
        result = None

    #retry by invalid question
    if result is None:
        print("Invalid input! Make your question like '2+2'. Try again!.\n")
        continue

    num1, user_operator, num2 = result

    #calculation
    try:
        answer = valid_operators[user_operator](num1, num2)
    except ZeroDivisionError:
        answer = None
    except OverflowError:
        print("Answer is too large. Try again!.\n")
        continue

    #print of answer
    if answer is None:
        print("You cannot divide by zero")
    else:
        print(f"Answer: {answer}")

    #data logging
    log_write(num1, user_operator, num2, answer, get_time())