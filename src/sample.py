# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 1) == 1

def multiply(x, y):
  """Multiplies two numbers together."""
  return x * y

def divide(x, y):
  """Divides two numbers."""
  return x / y
