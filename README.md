# Task Management System

## Overview
The Task Management System is a Python-based application designed to help a non-profit organization manage tasks efficiently. It enables users to create tasks, assign them to volunteers, set deadlines, and track their completion.

## Features
- **User Management**: Add and manage users.
- **Task Management**: Create, assign, and categorize tasks.
- **Task Status Tracking**: Mark tasks as completed or pending.
- **Graphical User Interface (GUI)**: User-friendly interface built with Tkinter.

## Technologies Used
- Python
- Tkinter (for GUI)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/task-management-system.git
   ```
2. Navigate to the project directory:
   ```sh
   cd task-management-system
   ```
3. Run the Python script:
   ```sh
   python Task_Management_System.py
   ```

## Usage
1. Open the application.
2. Add users by entering a name and clicking "Add User".
3. Create tasks by filling in the title, description, deadline, category, and assigning them to users.
4. View tasks assigned to a user.

## Class Diagram
- **Task**: Represents an individual task with title, description, deadline, category, and completion status.
- **User**: Represents a volunteer or team member who can be assigned tasks.
- **TaskManager**: Manages users and tasks.

## Example Output
```
User John added successfully!
Task 'Clean Park' added successfully!
John's Tasks:
- Clean Park - Urgent (Pending)
```

## License
This project is open-source and available under the MIT License.

## Author
Carson Doubiago

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.
