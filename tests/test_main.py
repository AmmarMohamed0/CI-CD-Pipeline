from src.main import add, subtract

def test_add_functoin():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(5, 5) == 10
    
def test_subtract_functoin():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(10, 5) == 5
