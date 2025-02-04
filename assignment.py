def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    name = "Emmanuel"
    age = "25"
    return f"My name is {name} and I am {25} years old"
    pass

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

    pass

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    n = 10
    return loop_sum (1,2,3,4,5,6,7,8,9,10)
    pass

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    numbers= (2, 4, 6, 8)
    return (sum(numbers), max(numbers), min(numbers))
    pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    score = "numbers"
    students_dict = {"Anna": 85, "Andrew": 72,"Emmanuel": 90, "Eve": 86}
    return[name for name, scores in students_dict.items () if score > 80]
    pass

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    list1 (1,2,3,4,5,6)
    list2 (2,4,6,8,9)
    return 
    set (2,4,6)




    pass

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return{
        "addition": a + b,"substraction": a-b, "multiplication": a*b,
          "division": a / b if b !=0 else 
        "undefined" # Avoid division by zero
        "modulus": a % b if b !=0 else
        "undefined" # Avoid modulus by zero
        }
    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    x = True
    y = False
    logical_ops = "AND", x and y,"OR", x or y, "NOT x", not x,
    "NOT y", not y
    "XOR", x != y # True if x and y are different
    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    a=6
    b=3
    bitwise_ops = {
        "AND": a & b,
        "OR": a|b,
        "XOR": a^b,
        "NOT a": ~a,
        "NOT b": ~b,
        "Left Shift a by 1": a<<1,
        "Right Shift a by 1": a>>1,
        "Left Shift b by 1": b<<1,
        "Right Shift a by 1": b>>1
    }
    pass