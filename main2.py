CONTRIBUTORS = [Sai Srikar Kolagani]  

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {CONTRIBUTORS}")
    print("Addition:", add(2, 2))  # Conflicts generator 2
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(2, 3))
    print("Division:", divide(6, 2))
