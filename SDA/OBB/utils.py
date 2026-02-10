# Instead of wrapping code into a try-catch statement we're building a error-handler function.

def safe_calculator(func):
    def wrapper_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred during calculation, {e}")
            return None
    return wrapper_function
