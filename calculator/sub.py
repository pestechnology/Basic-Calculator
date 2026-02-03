def subtract(*numbers):
    """
    Subtract multiple numbers:
    subtract(a, b, c) = a - b - c
    """
    if len(numbers) < 2:
        raise ValueError("Provide at least two numbers")

    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result
