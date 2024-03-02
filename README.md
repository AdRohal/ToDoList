# To-Do List Manager

A simple console-based to-do list manager with SQLite integration. Keep track of your tasks, mark them as completed, and clear completed tasks.

## Features

- **Add Task:** Add new tasks to your to-do list.
- **View Tasks:** Display all tasks in your to-do list.
- **Mark Task as Completed:** Mark a task as completed.
- **Clear Completed Tasks:** Remove completed tasks from the list.
- **SQLite Integration:** Persist your tasks in an SQLite database.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AdRohal/ToDoList.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd ToDoList
    ```

3. **Run the to-do list manager:**
    ```bash
    python main.py
    ```

## Usage

1. Choose options by entering the corresponding numbers.
2. Follow the prompts to manage your to-do list.

## Database Schema

The SQLite database contains a single table named `tasks` with the following columns:

- `id`: Unique identifier for each task.
- `task`: The text of the task.
- `completed`: Integer (0 or 1) indicating task completion status.

## Examples

```bash
Welcome to the To-Do List Manager! 📝

1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Clear Completed Tasks
5. Quit

Enter your choice (1-5): 1
Enter the task: Complete README for the project

Task "Complete README for the project" added successfully!

...

