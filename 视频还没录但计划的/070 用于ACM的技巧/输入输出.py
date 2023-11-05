def resolve_template(template: str):
    lines = template.strip().split("\n")
    result = []

    for line in lines:
        line_input = input().split()
        for idx, seg in enumerate(line.split()):
            if seg == "g":
                matrix_lines = int(line_input[0])
                matrix = [list(map(int, input().split())) for _ in range(matrix_lines)]
                result.append(matrix)
            elif seg == "n":
                number = int(line_input[idx])
                result.append(number)
            elif seg == "a":
                array = list(map(int, line_input))
                result.append(array)

    return result


r = resolve_template(
    """

""".strip()
)


template = """
g
n n
a
"""

standard_input = """
3
1 2 3
4 5 6
7 8 9
114 514
1 3 5 7 9
""".strip()
grid, n1, n2, arr = resolve_template(template)
