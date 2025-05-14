import calculator

def test_add():
    assert calculator.add(3, 2) == 5

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_multiply():
    assert calculator.multiply(2, 3) == 6

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    assert calculator.divide(5, 0) == "❌ Cannot divide by zero"

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("✅ All tests passed")
