# You must implement a decorator. @strict
# The decorator checks that the types of arguments passed to a function call match the argument types declared in the function prototype.
# (hint: argument type annotations can be obtained from the function object attribute func.__annotations__or using the module inspect)
# Throw an exception if the types do not match. TypeError. It is guaranteed that the parameters in the decorated functions will be of
# the following types: bool, int, float, str. It is guaranteed that the decorated functions will not have default parameter values


def strict(func):
    def wrapper(*args, **kwargs):
        # Get the expected argument types from the function annotations
        expected_types = func.__annotations__

        # Check positional arguments
        for arg, (param_name, expected_type) in zip(args, expected_types.items()):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Argument '{param_name}' must be of type {expected_type.__name__}, got {type(arg).__name__}")
        
        # Call the original function with the validated arguments
        return func(*args, **kwargs)
    
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError


# Program Output

"""
MacBook-Air:anish-tetrika-tasks anish$ python task1.py 
3
Traceback (most recent call last):
  File "/Users/anish/anish7605/github-projects/anish-tetrika-tasks/task1.py", line 29, in <module>
    print(sum_two(1, 2.4))  # >>> TypeError
  File "/Users/anish/anish7605/github-projects/anish-tetrika-tasks/task1.py", line 16, in wrapper
    raise TypeError(f"Argument '{param_name}' must be of type {expected_type.__name__}, got {type(arg).__name__}")
TypeError: Argument 'b' must be of type int, got float
"""
