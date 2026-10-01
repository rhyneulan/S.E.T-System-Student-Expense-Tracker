from rich import print
from cleaner import clear_console
from balance import get_initial_balance, save_value
from logs import logs_tracker, clear_logs
from warning import limit, save_limit, warning, spending, save_spending, reset_spending
from category import choose_category

logs = logs_tracker()
balance = get_initial_balance()
spending_limit = limit()
current_expense = spending()

while True:
    clear_console() # Clear the Terminal before running again
    print("=============================================================")
    print("  Welcome to S.E.T SYSTEM: Student Expense Tracker System")
    print("=============================================================")
    print(    f"[dim]Current Spending: P {current_expense:.2f} [/dim]")
    print("=============================================================")
    print(    f"[dim]Current Spending Limit: P{spending_limit:.2f}[/dim]")
    print("=============================================================")
    print()

    print("1. Check Remaining Balance")
    print("2. Enter new expenses")
    print("3. Add amount")
    print("4. View Recorded Logs")
    print("5. Edit Spending Limit")
    print("6. Clear Logs")
    print("7. Reset Spending")
    print("0. Exit Program")

    try:
        option = int(input("Enter Option: "))
    except ValueError:
        option = -1 

    if option == 1:
        print(f"\n--- Current Balance: P{balance:.2f}---")

    elif option == 2:
        try:
            expense = float(input("Enter Expense Amount: "))
            if expense > balance:
                print("\n[red bold]---[!] Warning: Insuficent Balance!---[/red bold]")
            else:
                category = choose_category()
                balance -= expense
                save_value(balance) 
                current_expense += expense
                save_spending(current_expense)
                
                logs(f"[red bold]Expense: -P {expense:.2f}[/red bold] | [cyan bold] {category}[/cyan bold]")
                print(f"\n[green bold]---Succesfully Deducted P{expense:.2f}.({category})---[/green bold]")

                if warning(current_expense, spending_limit):
                    print(f"\n[red bold]---[!] Warning: You have exceeded your spending limit of P{spending_limit:.2f}!---[/red bold]")
        except ValueError:
            print("\n[red bold]---[!] Invalid Input! Please Enter a Valid Number!---[/red bold]")

    elif option == 3:
        try:
            amount = float(input("Enter Amount to Add: "))
            balance += amount
            save_value(balance)
            logs(f"[green bold]Added: +P {amount:.2f}[/green bold]") 
            print(f"\n[green bold]---Successfully Added P{amount:.2f}.---[/green bold]")
        except ValueError:
            print("\n[red bold]---[!] Invalid Input! Please Enter a Valid Number!---[/red bold]")

    elif option == 4: 
        print("\n---Recorded Logs---")
        current_logs = logs()
        if not current_logs:
            print("No Recorded Transactions Yet.")
        else:
            for log in current_logs:
                print(log)
            print()
               
    elif option == 5:
        print(f"\nCurrent Spending Limit: P{spending_limit:.2f}")
        try:
            new_limit = float(input("Enter New Warning Limit (P): "))
            if new_limit <= 0:
                print("\n[red bold]--- Limit must be greater than 0! ---[/red bold]")
            else:
                spending_limit = new_limit
                save_limit(spending_limit)
                print(f"\n[green bold]--- Spending Limit Updated to P{spending_limit:.2f}! ---[/green bold]")
        except ValueError:
            print("\n[red bold]--- Invalid Limit Input! ---[/red bold]")

    elif option == 6:
        confirm = input("Are you sure you want to clear all logs? (y/n): ").strip().lower()
        if confirm == 'y':
            clear_logs()         
            logs = logs_tracker() 
            print("\n[green bold]--- All recorded logs have been successfully cleared! ---[/green bold]")
        else:
            print("\n--- Action Cancelled --- ")

    elif option == 7:
        reset = input("Do you want to reset your spending? (y/n): ").strip().lower()
        if reset == "y":
            reset_spending()
            current_expense = spending()
            print("\n[green bold]---All spending has been successfully cleared!---[/green bold]")
        else:
            print("\n--- Action Cancelled --- ")

    elif option == 0:
        print("Exiting SETSY. Goodbye!")
        break

    else:
        print("\n--- Invalid Option! Please Try Again ---")
    
    input("Press Enter to Return to Menu...") 