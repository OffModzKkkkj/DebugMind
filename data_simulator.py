
import pandas as pd
import random

def simulate_error_data(num_samples=1000):
    error_templates = [
        ("TypeError: unsupported operand type(s) for +: ", "You are trying to add two variables of incompatible types, like a string and a number. Make sure both sides of the '+' operator are of the same type, or convert one to match the other."),
        ("NameError: name ", " is not defined", "You are using a variable or function name that has not been declared or imported. Check for typos or ensure it's defined before use."),
        ("IndexError: list index out of range", "You are trying to access an element in a list (or array) using an index that is outside the valid range (e.g., trying to get the 10th element from a list with only 5 elements). Check your loop conditions or list length."),
        ("ValueError: invalid literal for int() with base 10: ", "You are trying to convert a string that does not represent a valid integer into an integer. Ensure the string contains only digits."),
        ("FileNotFoundError: [Errno 2] No such file or directory: ", "The program cannot find the file you specified. Check the file path and name, and ensure the file exists in the expected location."),
        ("SyntaxError: invalid syntax", "There's a grammatical mistake in your code that the Python interpreter cannot understand. Look for missing colons, parentheses, or incorrect keywords."),
        ("KeyError: ", "You are trying to access a key in a dictionary that does not exist. Check if the key is present in the dictionary before trying to retrieve its value."),
        ("AttributeError: ", " object has no attribute ", "You are trying to access an attribute or method on an object that does not possess it. This often happens when you misspell an attribute name or call a method on the wrong type of object."),
        ("ZeroDivisionError: division by zero", "You are attempting to divide a number by zero, which is mathematically undefined. Ensure your divisor is never zero before performing division."),
        ("ImportError: cannot import name ", " from ", "You are trying to import a specific name (function, class, variable) from a module, but that name does not exist in the module. Check the spelling or if the name is actually exported by the module.")
    ]

    languages = ["Python", "JavaScript", "Java", "C++"]
    
    data = []
    for i in range(num_samples):
        error_template, explanation_template = random.choice(error_templates)
        lang = random.choice(languages)

        # Generate a specific error message based on template
        if "TypeError" in error_template:
            error_message = f"{error_template}" + random.choice(["'str' and 'int'", "'list' and 'tuple'"])
        elif "NameError" in error_template:
            error_message = f"{error_template}" + random.choice(["'my_variable'", "'calculate_sum'"]) + explanation_template
        elif "IndexError" in error_template:
            error_message = error_template
        elif "ValueError" in error_template:
            error_message = f"{error_template}" + random.choice(["'abc'", "'2.5'"])
        elif "FileNotFoundError" in error_template:
            error_message = f"{error_template}" + random.choice(["'data.txt'", "'/app/config.json'"])
        elif "SyntaxError" in error_template:
            error_message = error_template
        elif "KeyError" in error_template:
            error_message = f"{error_template}" + random.choice(["'user_id'", "'item_name'"])
        elif "AttributeError" in error_template:
            error_message = f"{error_template}" + random.choice(["'str'", "'int'"]) + explanation_template + random.choice(["'append'", "'length'"])
        elif "ZeroDivisionError" in error_template:
            error_message = error_template
        elif "ImportError" in error_template:
            error_message = f"{error_template}" + random.choice(["'my_func'", "'MyClass'"]) + explanation_template + random.choice(["'my_module'", "'utils'"])
        else:
            error_message = error_template

        data.append({
            "language": lang,
            "error_message": error_message,
            "human_explanation": explanation_template # Simplified: direct mapping for now
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = simulate_error_data(num_samples=2000)
    df.to_csv("error_data.csv", index=False)
    print("Simulated error_data.csv created with 2000 samples.")
    print(df.head())
