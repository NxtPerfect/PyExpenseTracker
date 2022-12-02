import tkinter
from tkinter import StringVar, Button, Frame, Label, Listbox, Scrollbar, Tk, Entry, END, BOTTOM, RIGHT, BOTH, LEFT, ANCHOR


EXPENSE_LIST = []


root = Tk()
root.title("PyExpenseTracker")
root.geometry("800x700+200+200")
root.resizable(False, False)


def add_expense():
    expense_description = expense_description_entry.get()
    expense_description_entry.delete(0, END)
    expense_cost = expense_cost_entry.get()
    expense_cost_entry.delete(0, END)

    EXPENSE_LIST.append(expense_description + " cost:" + expense_cost)
    listbox_expense.insert(END, expense_description + " cost:" + expense_cost)


def delete_expense():
    local_expense = str(listbox_expense.get(ANCHOR))
    if local_expense in EXPENSE_LIST:
        EXPENSE_LIST.remove(local_expense)
        listbox_expense.delete(ANCHOR)


def calculate_all_expenses():
    overall_cost = 0
    for expense in EXPENSE_LIST:
        cost_list = expense.split(" cost:", 1)
        try:
            overall_cost += float(cost_list[1])
        except ValueError:
            all_expenses_cost.config(
                text="Invalid calculation, cost can't be not a numbe")
            return
    all_expenses_cost.config(text=overall_cost)
    # Change label


if __name__ == "__main__":
    heading = Label(root, text="All Expenses",
                    font="ubuntu 20 bold", bg="#aa6f73")
    heading.place(x=140, y=20)

    # Main
    frame = Frame(root, width=400, height=100, bg="white")
    frame.place(x=0, y=100)

    expense = StringVar()
    expense_description_entry = Entry(frame, width=18, font="ubuntu 20", bd=0)
    expense_description_entry.place(x=10, y=7)
    expense_description_entry.focus()
    expense_cost_entry = Entry(frame, width=18, font="ubuntu 20", bd=0)
    expense_cost_entry.place(x=10, y=47)
    expense_cost_entry.focus()

    button = Button(frame, text="Add", font="ubuntu 20 bold",
                    width=4, bg="#aa6f73", fg="#fff", bd=0,
                    command=add_expense)
    button.place(x=305, y=25)

    # Expense List
    frame1 = Frame(root, bd=3, width=700, height=280, bg="#66545e")
    frame1.pack(pady=(230, 0))

    listbox_expense = Listbox(frame1, font=('ubuntu', 12),
                              width=40, height=12, bg="#66545e",
                              fg="white", cursor="hand2", selectbackground="#a39193")
    listbox_expense.pack(side=LEFT, fill=BOTH, padx=2)

    scrollbar = Scrollbar(frame1)
    scrollbar.pack(side=RIGHT, fill=BOTH)

    listbox_expense.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox_expense.yview)

    # open_task_file()

    all_expenses_cost_label = Label(root, text="All expenses summed up to",
                                    font="ubuntu 20 bold", bg="#aa6f73")
    all_expenses_cost_label.place(x=200, y=500)
    all_expenses_cost = Button(root, text="Click to get expenses cost",
                               font="ubuntu 20 bold", bg="#aa6f73",
                               command=calculate_all_expenses)
    all_expenses_cost.place(x=175, y=550)

    # Delete expense
    delete = Button(root, text="Delete",
                    font="ubuntu 20 bold", bg="#aa6f73",
                    command=delete_expense)
    delete.pack(side=BOTTOM, pady=13)

    root.mainloop()
