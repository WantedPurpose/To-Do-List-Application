import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Input", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("No Task Selected", "Please select a task.")

def clear_tasks():
    listbox.delete(0, tk.END)

def main():
    global entry, listbox

    root = tk.Tk()
    root.title("To-Do List")


    root.geometry("400x400")
    root.config(bg="#f9f9f9")


    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack(pady=10)
    entry.bind("<Return>", add_task)  # Bind the Enter key to the add_task function


    listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10, bd=0, selectbackground="#a6a6a6")
    listbox.pack(padx=10, pady=5)


    button_frame = tk.Frame(root, bg="#f9f9f9")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add Task", font=("Arial", 12), command=add_task, bg="#a6a6a6", fg="#ffffff", bd=0, padx=10)
    add_button.grid(row=0, column=0, padx=5)

    delete_button = tk.Button(button_frame, text="Delete Task", font=("Arial", 12), command=delete_task, bg="#a6a6a6", fg="#ffffff", bd=0, padx=10)
    delete_button.grid(row=0, column=1, padx=5)

    clear_button = tk.Button(button_frame, text="Clear All", font=("Arial", 12), command=clear_tasks, bg="#a6a6a6", fg="#ffffff", bd=0, padx=10)
    clear_button.grid(row=0, column=2, padx=5)

    root.mainloop()

if __name__ == '__main__':
    main()
