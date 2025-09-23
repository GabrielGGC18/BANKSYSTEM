from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

# Simulated account data
accounts = {
    "546421": {'pin': '751312', 'balance': 2000.0},
    "120983": {'pin': '566312', 'balance': 50000.0},
    "052.731.071-99": {'pin': '999999', 'balance': 1000.0}  # Destination account
}

# Authentication
def authenticate():
    account_number = entry_account.get()
    pin = entry_pin.get()

    data = accounts.get(account_number)
    if data and data['pin'] == pin:
        messagebox.showinfo("Success", "Logged in successfully 😎")
        open_menu(account_number)
    else:
        messagebox.showerror("Error", "Incorrect account or PIN 😞")

# Main Menu
def open_menu(account):
    menu_window = Toplevel(root)
    menu_window.title("ATM Menu")
    menu_window.geometry("450x300")

    notebook = ttk.Notebook(menu_window)
    notebook.pack(expand=True, fill='both')

    # Balance Tab
    tab_balance = Frame(notebook)
    notebook.add(tab_balance, text="Balance")

    def view_balance():
        balance = accounts[account]['balance']
        messagebox.showinfo("Balance", f"Current balance: R${balance:.2f}")

    Button(tab_balance, text="View Balance", command=view_balance).pack(pady=20)

    # Deposit Tab
    tab_deposit = Frame(notebook)
    notebook.add(tab_deposit, text="Deposit")

    Label(tab_deposit, text="Deposit Amount:").pack()
    entry_deposit = Entry(tab_deposit)
    entry_deposit.pack()

    def deposit():
        amount = float(entry_deposit.get())
        accounts[account]['balance'] += amount
        messagebox.showinfo("Deposit", "Deposit successful!")

    Button(tab_deposit, text="Deposit", command=deposit).pack(pady=10)

    # Withdraw Tab
    tab_withdraw = Frame(notebook)
    notebook.add(tab_withdraw, text="Withdraw")

    Label(tab_withdraw, text="Withdraw Amount:").pack()
    entry_withdraw = Entry(tab_withdraw)
    entry_withdraw.pack()

    def withdraw():
        amount = float(entry_withdraw.get())
        accounts[account]['balance'] -= amount  # Allows negative balance
        messagebox.showinfo("Withdraw", "Withdrawal successful 😎")

    Button(tab_withdraw, text="Withdraw", command=withdraw).pack(pady=10)

    # Pix Tab
    tab_pix = Frame(notebook)
    notebook.add(tab_pix, text="Pix")

    Label(tab_pix, text="Destination Account:").pack()
    entry_dest = Entry(tab_pix)
    entry_dest.pack()
    entry_dest.insert(0, "052.731.071-99")

    Label(tab_pix, text="Pix Amount:").pack()
    entry_pix_amount = Entry(tab_pix)
    entry_pix_amount.pack()

    def send_pix():
        dest = entry_dest.get()
        amount = float(entry_pix_amount.get())
        if dest not in accounts:
            messagebox.showerror("Error", "Destination account not found 😞")
            return
        accounts[account]['balance'] -= amount  # Allows overdraft
        accounts[dest]['balance'] += amount
        messagebox.showinfo("Pix", f"Pix of R${amount:.2f} sent to {dest} 😎")

    Button(tab_pix, text="Send Pix", command=send_pix).pack(pady=10)

    # Credit Card Tab
    tab_credit = Frame(notebook)
    notebook.add(tab_credit, text="Credit Card")

    Label(tab_credit, text="Card Limit:").pack()
    entry_limit = Entry(tab_credit)
    entry_limit.pack()

    Label(tab_credit, text="Send Amount via Card:").pack()
    entry_card_send = Entry(tab_credit)
    entry_card_send.pack()

    def send_with_card():
        limit = float(entry_limit.get())
        amount = float(entry_card_send.get())
        if amount <= limit:
            messagebox.showinfo("Credit", f"R${amount:.2f} sent using credit card 😎")
        else:
            messagebox.showerror("Error", "Amount exceeds card limit 😞")

    Button(tab_credit, text="Send via Card", command=send_with_card).pack(pady=10)

# Loading Screen
def loading_screen():
    loading = Toplevel()
    loading.title("Loading...")
    loading.geometry("300x150")
    Label(loading, text="Starting system...", font=("Arial", 12)).pack(pady=10)
    progress = ttk.Progressbar(loading, orient=HORIZONTAL, length=250, mode='determinate')
    progress.pack(pady=10)

    def load():
        for i in range(101):
            progress['value'] = i
            loading.update_idletasks()
            loading.after(15)
        loading.destroy()

    Button(loading, text="Start", command=load).pack(pady=10)

# Main Window
root = Tk()
root.title("ATM System")
root.geometry("400x250")

Label(root, text="Account Number:").pack()
entry_account = Entry(root)
entry_account.pack()

Label(root, text="PIN:").pack()
entry_pin = Entry(root, show="*")
entry_pin.pack()

Button(root, text="Login", command=authenticate).pack(pady=10)
Button(root, text="Loading Screen", command=loading_screen).pack(pady=5)

root.mainloop()
