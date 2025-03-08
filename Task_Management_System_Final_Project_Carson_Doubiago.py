import tkinter as tk
from tkinter import messagebox

# Task class
class Task:
    def __init__(self, title, description, deadline, category):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# User class
class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def assign_task(self, task):
        self.tasks.append(task)

# Task Manager class
class TaskManager:
    def __init__(self):
        self.users = {}
        self.tasks = []

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)

    def add_task(self, title, description, deadline, category, username):
        if username in self.users:
            task = Task(title, description, deadline, category)
            self.users[username].assign_task(task)
            self.tasks.append(task)
        else:
            messagebox.showerror("Error", "User not found!")

    def get_tasks(self, username):
        if username in self.users:
            return self.users[username].tasks
        return []

# GUI class
class TaskManagerGUI:
    def __init__(self, root):
        self.task_manager = TaskManager()
        self.root = root
        self.root.title("Task Management System")

        self.label_user = tk.Label(root, text="User:")
        self.label_user.grid(row=0, column=0)
        self.entry_user = tk.Entry(root)
        self.entry_user.grid(row=0, column=1)
        self.button_add_user = tk.Button(root, text="Add User", command=self.add_user)
        self.button_add_user.grid(row=0, column=2)

        self.label_title = tk.Label(root, text="Task Title:")
        self.label_title.grid(row=1, column=0)
        self.entry_title = tk.Entry(root)
        self.entry_title.grid(row=1, column=1)

        self.label_desc = tk.Label(root, text="Description:")
        self.label_desc.grid(row=2, column=0)
        self.entry_desc = tk.Entry(root)
        self.entry_desc.grid(row=2, column=1)

        self.label_deadline = tk.Label(root, text="Deadline:")
        self.label_deadline.grid(row=3, column=0)
        self.entry_deadline = tk.Entry(root)
        self.entry_deadline.grid(row=3, column=1)

        self.label_category = tk.Label(root, text="Category:")
        self.label_category.grid(row=4, column=0)
        self.entry_category = tk.Entry(root)
        self.entry_category.grid(row=4, column=1)

        self.label_assign = tk.Label(root, text="Assign to User:")
        self.label_assign.grid(row=5, column=0)
        self.entry_assign = tk.Entry(root)
        self.entry_assign.grid(row=5, column=1)

        self.button_add_task = tk.Button(root, text="Add Task", command=self.add_task)
        self.button_add_task.grid(row=6, column=1)

        self.button_view_tasks = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.button_view_tasks.grid(row=7, column=1)

    def add_user(self):
        username = self.entry_user.get()
        if username:
            self.task_manager.add_user(username)
            messagebox.showinfo("Success", f"User {username} added successfully!")

    def add_task(self):
        title = self.entry_title.get()
        desc = self.entry_desc.get()
        deadline = self.entry_deadline.get()
        category = self.entry_category.get()
        username = self.entry_assign.get()
        
        if title and desc and deadline and category and username:
            self.task_manager.add_task(title, desc, deadline, category, username)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def view_tasks(self):
        username = self.entry_assign.get()
        if username:
            tasks = self.task_manager.get_tasks(username)
            task_list = "\n".join([f"{task.title} - {task.category} ({'Completed' if task.completed else 'Pending'})" for task in tasks])
            messagebox.showinfo("Tasks", task_list if task_list else "No tasks found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()

# Documentation
"""
Proposal:
The Task Management System helps a non-profit organization manage tasks efficiently. Users can create tasks, assign them to volunteers, set deadlines, and track completion.

Class Diagram:
1. Task - Represents an individual task with title, description, deadline, category, and completion status.
2. User - Represents a user (volunteer) who can be assigned tasks.
3. TaskManager - Manages all users and tasks, ensuring smooth assignment and retrieval.

Report & Sample Output:
- Users can be added to the system.
- Tasks can be assigned to users.
- Tasks can be viewed per user.
- Message pop-ups confirm actions.

Example Output:
User John added successfully!
Task 'Clean Park' added successfully!
John's Tasks:
- Clean Park - Urgent (Pending)
"""
