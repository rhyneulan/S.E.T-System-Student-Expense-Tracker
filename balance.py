import ast

budget_storage = "money.txt"

def save_value(input_value, filename=budget_storage):
    with open(filename, "w") as file:
        file.write(str(input_value))

def load_value(filename=budget_storage):
    with open(filename, "r") as file:
        return file.read()

def get_initial_balance(filename=budget_storage):
    try:
        return float(ast.literal_eval(load_value(filename)))
    except:
        save_value(0.0, filename)
        return 0.0