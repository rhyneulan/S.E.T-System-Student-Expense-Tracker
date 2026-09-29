# S.E.T SYSTEM — Student Expense Tracker System

A simple command-line based **Student Expense Tracker System (SETSY)** developed using Python.

The system is designed to help students manage their available balance, record expenses, categorize spending, monitor their total expenses, and receive warnings when their spending exceeds a configured limit.

All data is stored locally using text files, so the system does not require an external database.

---

## 📌 Overview

The **S.E.T SYSTEM (Student Expense Tracker System)** provides a simple terminal-based solution where users can:

* Check their remaining balance
* Add money to their balance
* Record expenses
* Categorize expenses
* View transaction logs
* Set a spending limit
* Receive a warning when the spending limit is exceeded
* Clear transaction logs
* Reset current spending

The application runs directly in the terminal/command prompt and uses local `.txt` files for data storage.

---

## ✨ Features

### 💰 Balance Management

Users can check their current remaining balance and add additional money whenever needed.

The balance is stored locally in `money.txt`.

If no valid balance exists when the program starts, the system initializes the balance to `0.0`.

### 💸 Expense Tracking

Users can enter a new expense amount.

Before an expense is deducted, the system checks whether the expense is greater than the current balance.

If the expense exceeds the available balance, the system displays an insufficient-balance warning.

Otherwise, the expense is deducted from the balance and added to the current spending total.

### 📂 Expense Categories

Every recorded expense can be assigned to a category.

Available categories:

1. Foods
2. Bills
3. Transportation
4. Entertainment
5. Health
6. Supplies
7. Shopping

### 📋 Transaction Logs

The system records transactions in `logs.txt`.

Transactions include a timestamp and information about whether money was added or an expense was recorded.

### ⚠️ Spending Limit

Users can configure a spending limit.

The default spending limit is:

```text
P500.00
```

When current spending exceeds the configured limit, the program displays a warning.

### 🧹 Clear Logs

Users can clear all recorded transaction logs from the menu.

The system asks for confirmation before clearing the logs.

### 🔄 Reset Spending

Users can reset their current spending amount.

When reset, the spending value becomes:

```text
0.0
```

### 🎨 Terminal Formatting

The project uses the **Rich** Python package to display formatted terminal output.

---

# 🖥️ System Requirements

Before running the project, make sure you have:

* **Python 3**
* **pip**
* **Git** — only required if cloning the repository
* **Windows Command Prompt or PowerShell**
* **Rich** Python package

The project uses Python standard-library modules such as `os`, `datetime`, and `ast`. These are included with Python and do not need to be installed separately.

The only external Python package required is:

```text
rich
```

---

# 📦 Project Structure

```text
S.E.T-System-Student-Expense-Tracker/
│
├── main.py
├── balance.py
├── category.py
├── cleaner.py
├── expense.py
├── logs.py
├── warning.py
├── system_concept.drawio
│
├── money.txt
├── spending.txt
├── warning.txt
└── logs.txt
```

### File Description

| File                    | Description                                   |
| ----------------------- | --------------------------------------------- |
| `main.py`               | Main entry point and menu system              |
| `balance.py`            | Handles balance storage and retrieval         |
| `category.py`           | Handles expense categories                    |
| `cleaner.py`            | Clears the terminal screen                    |
| `expense.py`            | Contains the expense tracker introduction     |
| `logs.py`               | Handles transaction logs                      |
| `warning.py`            | Handles spending limits and spending tracking |
| `system_concept.drawio` | System concept/design diagram                 |
| `money.txt`             | Stores the current balance                    |
| `spending.txt`          | Stores the current spending                   |
| `warning.txt`           | Stores the spending limit                     |
| `logs.txt`              | Stores transaction history                    |

---

# 🚀 Installation

## 1. Clone the Repository

Open **Command Prompt** or **PowerShell**.

```bash
git clone https://github.com/rhyneulan/S.E.T-System-Student-Expense-Tracker.git
```

Enter the project directory:

```bash
cd S.E.T-System-Student-Expense-Tracker
```

> If you downloaded the project as a ZIP file, you can skip the `git clone` command and open the project folder directly.

---

## 2. Create a Virtual Environment

```bash
python -m venv setsy
```

---

## 3. Activate the Virtual Environment

For Windows:

```bash
setsy\Scripts\activate
```

After activation, you should see:

```text
(setsy)
```

at the beginning of your command line.

---

## 4. Install the Required Package

```bash
pip install rich
```

---

# ▶️ Running the Program

Run:

```bash
python main.py
```

The program will display the S.E.T SYSTEM main menu.

```text
1. Check Remaining Balance
2. Enter new expenses
3. Add amount
4. View Recorded Logs
5. Edit Spending Limit
6. Clear Logs
7. Reset Spending
0. Exit Program
```

---

# 🧭 How to Use the System

### Option 1 — Check Remaining Balance

Select:

```text
1
```

Displays the current remaining balance.

### Option 2 — Enter New Expense

Select:

```text
2
```

Enter the expense amount and select a category.

If the expense is within the available balance:

* The balance is reduced.
* The expense is added to current spending.
* The transaction is saved.
* The selected category is recorded.
* The spending limit is checked.

If the expense is greater than the available balance, the transaction is not processed.

### Option 3 — Add Amount

Select:

```text
3
```

Enter the amount you want to add.

The amount is added to the current balance and recorded in the logs.

### Option 4 — View Recorded Logs

Select:

```text
4
```

Displays previously recorded transactions.

### Option 5 — Edit Spending Limit

Select:

```text
5
```

Enter a new spending limit.

The limit must be greater than `0`.

### Option 6 — Clear Logs

Select:

```text
6
```

Confirm with:

```text
y
```

to clear the transaction logs, or:

```text
n
```

to cancel.

### Option 7 — Reset Spending

Select:

```text
7
```

Confirm with `y` to reset the current spending to `0.0`.

### Option 0 — Exit

Select:

```text
0
```

to exit the program.

---

# 💾 Data Storage

SETSY uses **local text files** instead of a database.

| File           | Purpose                   |
| -------------- | ------------------------- |
| `money.txt`    | Current available balance |
| `spending.txt` | Current total spending    |
| `warning.txt`  | Spending warning limit    |
| `logs.txt`     | Transaction history       |

You do **not** need to create these files manually. The application manages them automatically.

---

# 📋 Quick Start

If Python and Git are already installed:

```bash
git clone https://github.com/rhyneulan/S.E.T-System-Student-Expense-Tracker.git
cd S.E.T-System-Student-Expense-Tracker
python -m venv setsy
setsy\Scripts\activate
pip install rich
python main.py
```

---

# ⚠️ Important Notes

* Run the program from the project directory containing `main.py`.
* Keep the virtual environment activated while using the system.
* The default spending limit is **₱500.00**.
* Your data is stored locally in the project folder.
* Do not delete the `.txt` files if you want to keep your saved data.
* The system does not require MySQL, SQLite, MongoDB, or another external database.

---

# 🛠️ Troubleshooting

### Python is not recognized

Try:

```bash
py --version
```

If `py` works, create the virtual environment with:

```bash
py -m venv setsy
```

Then activate it:

```bash
setsy\Scripts\activate
```

### Rich is not installed

Activate the environment:

```bash
setsy\Scripts\activate
```

Then install Rich:

```bash
pip install rich
```

Run the program:

```bash
python main.py
```

### Virtual Environment Is Not Activated

If you do not see:

```text
(setsy)
```

activate it again:

```bash
setsy\Scripts\activate
```

### PowerShell Activation Issue

If PowerShell prevents the activation script from running, open **Command Prompt (CMD)** and use:

```cmd
setsy\Scripts\activate
```

---

# 📜 Policy

By using this project, users agree to use the system responsibly and for its intended purpose of tracking personal or student expenses.

* Users are responsible for the accuracy of the information they enter.
* The system stores expense data locally on the user's computer.
* Users are responsible for protecting and backing up their saved data.
* The developers are not responsible for loss of data caused by deletion, modification, or damage to the local storage files.
* This project is provided for educational and personal use.

---

# 👥 Authors

* CATANDIJAN, MAE ANN O.
* DANGGOY, IAN DEXTER L.
* DEMETILA, JAMES C.
* GALO, RANIEL C.
* LADRA, RHYNE MARC B. (Developer)
* NALASA, CHEED RODJON B.


---

# 📄 License

This project is intended for **educational purposes**.

Unless otherwise stated by the authors, the project should not be redistributed, modified, or used for commercial purposes without permission from the authors.
