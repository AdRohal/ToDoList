import sqlite3
import tkinter as tk
from tkinter import messagebox

class UserDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('user_database.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                address TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')
        self.conn.commit()

    def get_user_input(self):
        self.input_window = tk.Toplevel()
        self.input_window.title("Add User")
        self.resize_window(self.input_window, 1.3)

        tk.Label(self.input_window, text="First Name:").grid(row=0, column=0)
        tk.Label(self.input_window, text="Last Name:").grid(row=1, column=0)
        tk.Label(self.input_window, text="Age:").grid(row=2, column=0)
        tk.Label(self.input_window, text="Address:").grid(row=3, column=0)
        tk.Label(self.input_window, text="Phone Number:").grid(row=4, column=0)
        tk.Label(self.input_window, text="Email:").grid(row=5, column=0)

        self.first_name_entry = tk.Entry(self.input_window)
        self.last_name_entry = tk.Entry(self.input_window)
        self.age_entry = tk.Entry(self.input_window)
        self.address_entry = tk.Entry(self.input_window)
        self.phone_number_entry = tk.Entry(self.input_window)
        self.email_entry = tk.Entry(self.input_window)

        self.first_name_entry.grid(row=0, column=1)
        self.last_name_entry.grid(row=1, column=1)
        self.age_entry.grid(row=2, column=1)
        self.address_entry.grid(row=3, column=1)
        self.phone_number_entry.grid(row=4, column=1)
        self.email_entry.grid(row=5, column=1)

        tk.Button(self.input_window, text="Add User", command=self.add_user).grid(row=6, column=0, columnspan=2)
        self.add_back_button(self.input_window)

        # Center the input window
        self.center_window(self.input_window)

    def add_back_button(self, window):
        tk.Button(window, text="Back", command=window.destroy).grid(row=7, column=0, columnspan=2)

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def resize_window(self, window, scale):
        window.update_idletasks()
        width = int(window.winfo_reqwidth() * scale)
        height = int(window.winfo_reqheight() * scale)
        window.geometry('{}x{}'.format(width, height))

    def add_user(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = int(self.age_entry.get())
        address = self.address_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        user_data = (first_name, last_name, age, address, phone_number, email)
        self.cursor.execute('''
            INSERT INTO users (first_name, last_name, age, address, phone_number, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', user_data)
        self.conn.commit()
        messagebox.showinfo("Success", "User information added successfully!")
        self.input_window.destroy()
        self.add_back_button(self.input_window)
    def show_users(self):
        self.show_window = tk.Toplevel()
        self.show_window.title("Show Users")
        self.resize_window(self.show_window, 2.9)

        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()

        if not users:
            messagebox.showinfo("No Users", "No users found in the database.")
            self.show_window.destroy()
        else:
            user_text = "ID\tName\tAge\tAddress\tPhone\tEmail\n"
            for user in users:
                user_text += f"{user[0]}\t{user[1]} {user[2]}\t{user[3]}\t{user[4]}\t{user[5]}\t{user[6]}\n"

            text_label = tk.Label(self.show_window, text=user_text, justify=tk.LEFT)
            text_label.pack()

        # Center the show window
        self.center_window(self.show_window)
        self.add_back_button(self.show_window)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack()

    def delete_user(self):
        user_id = int(input("Enter the ID of the user you want to delete: "))
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()
        print("🗑️ User deleted successfully!")
        # tk.Button(self.root, text="Back", command=self.root.quit).pack()

    def main(self):
        self.root = tk.Tk()
        self.root.title("User Database")
        self.resize_window(self.root, 1.3)

        tk.Button(self.root, text="Add User", command=self.get_user_input).pack()
        tk.Button(self.root, text="Show Users", command=self.show_users).pack()
        tk.Button(self.root, text="Delete User", command=self.delete_user).pack()
        tk.Button(self.root, text="Quit", command=self.root.quit).pack()

        # Center the main window
        self.center_window(self.root)

        self.root.mainloop()

if __name__ == "__main__":
    db = UserDatabase()
    db.main()
