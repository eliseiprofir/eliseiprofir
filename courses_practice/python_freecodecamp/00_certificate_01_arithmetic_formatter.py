def valid_problems(problems: list[str]) -> str:
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        if "+" not in problem and "-" not in problem:
            return "Error: Operator must be '+' or '-'."
    for problem in problems:
        num1, operator, num2 = problem.split(" ")
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
    return "Problems are valid."


def arithmetic_arranger(problems: list[str], show_answers: bool = False) -> str:
    """
    Rules:
    1) Not more than 5 problems
    2) Only numbers allowed
    3) Only 4-digit numbers allowed
    """

    if valid_problems(problems) != "Problems are valid.":
        return valid_problems(problems)

    line1_num1: str = ""
    line2_num2: str = ""
    line3_dash: str = ""
    line4_res: str = ""

    for problem in problems:
        num1, operator, num2 = problem.split(" ")

        len_num1: int = len(num1)
        len_num2: int = len(num2)

        int_num1: int = int(num1)
        int_num2: int = int(num2)

        result: int = 0

        if operator == "+":
            result = int_num1 + int_num2
        if operator == "-":
            result = int_num1 - int_num2

        len_res: int = len(str(result))
        str_res: str = str(result)

        if len_num1 > len_num2:
            full_len: int = len_num1 + 2
            line1_num1 += '  ' + num1 + '    '
            num2_spaces: int = len_num1 - len_num2
            line2_num2 += operator + ' ' + num2_spaces * ' ' + num2 + '    '
            line3_dash += full_len * '-' + '    '
            line4_res += (full_len - len_res) * ' ' + str_res + '    '

        if len_num1 < len_num2 or len_num1 == len_num2:
            full_len: int = len_num2 + 2
            line1_num1 += (full_len - len_num1) * " " + num1 + '    '
            line2_num2 += operator + ' ' + num2 + '    '
            line3_dash += full_len * '-' + '    '
            line4_res += (full_len - len_res) * ' ' + str_res + '    '

    line1_num1: str = line1_num1.rstrip()
    line2_num2: str = line2_num2.rstrip()
    line3_dash: str = line3_dash.rstrip()
    line4_res: str = line4_res.rstrip()

    if show_answers:
        arranger: str = line1_num1 + '\n' + line2_num2 + '\n' + line3_dash + '\n' + line4_res + '\n'
    else:
        arranger: str = line1_num1 + '\n' + line2_num2 + '\n' + line3_dash + '\n'

    return arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
