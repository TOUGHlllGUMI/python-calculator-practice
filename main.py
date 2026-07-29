from calculator import add, subtract, multiply, divide

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def main():
    print("Simple Calculator (type 'q' to quit)")
    print("Format: <number> <+|-|*|/> <number>  e.g. 3 + 4")

    while True:
        expression = input("\n> ").strip()
        if expression.lower() == "q":
            break

        parts = expression.split()
        if len(parts) != 3 or parts[1] not in OPERATIONS:
            print("Invalid input. Format: <number> <+|-|*|/> <number>")
            continue

        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
            result = OPERATIONS[op](a, b)
            print(f"= {result}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
