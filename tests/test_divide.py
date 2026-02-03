from divide import divide

def test_divide():
    # Normal cases
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5

    # Edge cases
    assert divide(0, 5) == 0
    assert divide(5, 0) == "Error: Cannot divide by zero"

    print("All tests passed!")

# Run the test
test_divide()
