import os

warning_file = "warning.txt"

def limit(filename=warning_file, default_limit=500.0):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                content = file.read().strip()
                if content != "": 
                    return float(content)
        except (ValueError, FileNotFoundError):
            pass

    save_limit(default_limit, filename)
    return float(default_limit)

def save_limit(new_limit, filename=warning_file):
    with open(filename, "w") as file:
        file.write(str(new_limit))

expense = "spending.txt"

def spending(filename=expense):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                spending = file.read().strip()
                if spending != "":
                    return float(spending)
        except (ValueError, FileNotFoundError):
            pass
    return 0.0

def save_spending(new_spending, filename=expense):
    with open(filename, "w") as file:
        file.write(str(new_spending))

def reset_spending(filename="spending.txt"):
    with open(filename, "w") as file:
        file.write("0.0")
    

def warning(current_expense, limit):
    return current_expense > limit


