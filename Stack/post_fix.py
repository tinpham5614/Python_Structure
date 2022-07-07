
def postfix(exp: str) -> int:
    cool_stack = []

    for token in exp:
        if token in "*+-/":

            second = cool_stack.pop()
            first = cool_stack.pop()

            if token == "*":
                cool_stack.append(first * second)
            elif token == "+":
                cool_stack.append(first + second)
            elif token == "-":
                cool_stack.append(first - second)
            elif token == "/":
                cool_stack.append(first // second)

        elif token != " ":
            cool_stack.append(int(token))

    return cool_stack.pop() if len(cool_stack) != 0 else 0


if __name__ == "__main__":
    example = ""
    print(postfix(example))
