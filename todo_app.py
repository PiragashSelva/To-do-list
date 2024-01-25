import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("To-Do List")

        # List to store tasks
        self.tasks = []

        # Entry for task input
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Task list
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for mark as complete and delete
        complete_button = tk.Button(
            root, text="Mark as Complete", command=self.mark_as_complete
        )
        complete_button.grid(row=2, column=0, padx=5, pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=2, column=1, padx=5, pady=5)

        # Populate task list
        self.update_task_list()

    def add_task(self):
        # Function to add a new task
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_as_complete(self):
        # Function to mark a task as complete
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] = f"[Completed] {self.tasks[task_index]}"
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def delete_task(self):
        # Function to delete a task
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task.")

    def update_task_list(self):
        # Function to update the task list in the GUI
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()