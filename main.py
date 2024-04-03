import sqlite3

class ToDoList:
    def __init__(self):
        self.conn = sqlite3.connect('todo_database.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                completed INTEGER
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        self.cursor.execute('INSERT INTO tasks (task, completed) VALUES (?, 0)', (task,))
        self.conn.commit()
        print(f'Task "{task}" added successfully!')

    def view_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        tasks = self.cursor.fetchall()

        if not tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nTo-Do List:")
            for task in tasks:
                status = "✔" if task[2] else "❌"
                print(f"{task[0]}. [{status}] {task[1]}")

    def mark_completed(self, task_id):
        try:
            task_id = int(task_id)
            self.cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
            self.conn.commit()
            print(f'Task with ID {task_id} marked as completed!')
        except (ValueError, sqlite3.Error):
            print("Invalid task ID. Please enter a valid ID.")

    def clear_completed(self):
        self.cursor.execute('DELETE FROM tasks WHERE completed = 1')
        self.conn.commit()
        print("Completed tasks cleared successfully!")

    def __del__(self):
        self.conn.close()

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear Completed Tasks")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = input("Enter the task ID to mark as completed: ")
            todo_list.mark_completed(task_id)
        elif choice == '4':
            todo_list.clear_completed()
        elif choice == '5':
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()