import operator

#function for get time now
def get_time():
    import datetime
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return time_now

#function for add data in log
def log_write(expression, answer, get_time):
    try:
        with open("log.txt", "a") as log:
            if answer is None:
                log.write(f"{get_time}   /   Question: {expression}. Answer: Error in calculation (division by zero or too large)." "\n")
            else:
                log.write(f"{get_time}   /   Question: {expression}. Answer: {answer}." "\n")
    except FileNotFoundError:
        print("File has been not found")

#expression parse func
def parse_expression(expression_string):

    valid_operators = ["*", "/", "%", "+", "-"]

    #delete of " "
    expression_string = expression_string.replace(" ", "")

    numbers = []
    operators = []
    current_number = ""
    operator = None

    #variables to parse expression
    current_index = 0
    expression_length = len(expression_string)

    if expression_string[-1] in valid_operators:
        return None

    #main func's loop
    while current_index < expression_length:
        current_char = expression_string[current_index]

        #dot as float interpretation
        if current_char.isdigit() or current_char in ".":
            current_number += current_char

        #interpretation of operators
        elif current_char in valid_operators:
            if current_char in "*/%+":
                numbers.append(current_number)
                current_number = ""

            #interpritation of minus
            if current_char == "-":
                if current_index > 0 and expression_string[current_index - 1] in valid_operators:
                    if expression_string[current_index + 1].isdigit():
                        current_number += current_char
                    else:
                        return None
                elif current_index > 0 and expression_string[current_index - 1].isdigit():
                    numbers.append(current_number)
                    current_number = ""
                    operator = "-"

            #correct "*" and "**" interpretation
            elif current_char == "*":
                if current_index == 0:
                    return None
                if current_index > 0 and expression_string[current_index + 1] in "*":
                    if expression_string[current_index +2] in valid_operators:
                        return None
                    elif len(numbers) > 0:
                        operator = "**"
                        current_index += 1
                    else:
                        return None
                else:
                    operator = "*"


            #else operators
            elif current_char in "+/%":
                if current_index == 0:
                    return None
                elif expression_string[current_index + 1] in valid_operators:
                    #user cant enter more as 1 operator
                    return None
                else:
                    operator = current_char

        #check for digit or operator
        else:
            return None

        if operator is not None:
            operators.append(operator)
            operator = None

        if current_number.count(".") > 1:
            return None

        current_index += 1

    numbers.append(current_number)

    #final check
    if len(numbers) < 2 or len(operators) < 1:
        return None

    if len(numbers) != len(operators) + 1:
        print("Too much operators. Try again.")
        return None

    return numbers, operators

#calculation func
def calculation(valid_operators, numbers, operators):

    operators = operators
    numbers = numbers

    #lopp for calculation with prority
    while operators:
        for current_operator in valid_operators.keys():
            if current_operator in operators:
                index = operators.index(current_operator)

                num1 = float(numbers[index])
                num2 = float(numbers[index + 1])

                #calculator
                try:
                    result = valid_operators[current_operator](num1, num2)
                except ZeroDivisionError:
                    return None
                except OverflowError:
                    return None

                #print(result) #-- if you will check the calculation process
                numbers[index] = result
                del numbers[index + 1]
                del operators[index]

                break

    return numbers[0]

valid_operators = {
    "**": operator.pow,
    "%": operator.mod,
    "*": operator.mul,
    "/": operator.truediv,
    "-": operator.sub,
    "+": operator.add,
}

while True:
    expression = str(input("Enter your expression - "))

    #get parced expression
    parse_result = parse_expression(expression)

    #check for results validity
    if parse_result is not None:
        numbers, operators = parse_result
    else:
        print("Invalid input. Try again.")
        continue

    #print(parse_result) #-- if you will check the result of parse

    #calculation
    answer = calculation(valid_operators, numbers, operators)

    #answers print
    if answer is not None:
        print(f"Answer: {answer}\n")
    else:
        print(f"Error in calculation (division by zero or too large). Try again.\n")

    # answer logging
    log_write(expression, answer, get_time())