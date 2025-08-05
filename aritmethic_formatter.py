def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top = []
    bottom = []
    lines = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        top.append(operand1.rjust(width))
        bottom.append(operator + operand2.rjust(width - 1))
        lines.append('-' * width)

        if show_answers:
            result = str(eval(operand1 + operator + operand2))
            results.append(result.rjust(width))

    arranged = "    ".join(top) + "\n" + "    ".join(bottom) + "\n" + "    ".join(lines)
    if show_answers:
        arranged += "\n" + "    ".join(results)

    return arranged

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))
