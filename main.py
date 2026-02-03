from calculator.add import add
from calculator.sub import sub
from calculator.mul import mul
from calculator.div import div


def main():
    print("Basic Calculator")
    print("Choose operation: add | sub | mul | div")

    operation = input("Enter operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "add":
        result = add(a, b)
    elif operation == "sub":
        result = sub(a, b)
    elif operation == "mul":
        result = mul(a, b)
    elif operation == "div":
        result = div(a, b)
    else:
        print("Invalid operation")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()
