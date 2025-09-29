# Reverse Polish is a mathematical notation where operators follow their operands
import math


def evaluate_rpn(tokens: list[str]) -> int:
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        # isdigit returns False for negative integer strings
        # int function can very well handle negativity
        if token not in operators:
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            res = None

            match token:
                case "+":
                    res = num1 + num2
                case "-":
                    res = num1 - num2
                case "*":
                    res = num1 * num2
                case "/":
                    # Truncate toward zero
                    # When there is a negative operand, integer division moves away from zero
                    res = math.trunc(num1 / num2)

            stack.append(res)
    return stack.pop()


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evaluate_rpn(tokens))
