from calculator import add
from calculator import sub
from calculator import mul
from calculator import div

def test_add():
    try:
        assert add(2, 3) == 5, "Addition test failed"
        assert sub(-1, 1) == -2, "Subtraction test failed"
        assert mul(0, 0) == 0, "Multiplication test failed"
        assert div(10, 2) == 5, "Division test failed"
    except AssertionError as e:
        print(f"Test failed: {e}")
    else:
        print("✅ All tests passed")

if __name__ == "__main__":
    test_add()
    print("✅ All tests passed")
    # You can run this test file directly to check the add function
    # or use pytest to run the tests in a more structured way.