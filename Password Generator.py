# password_generator.py

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("300x200")

        self.length_label = tk.Label(self.window, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(self.window, width=20)
        self.length_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(self.window, text="Generated Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.window, width=20)
        self.password_entry.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showerror("Error", "Password length must be at least 8 characters")
                return
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError:
            messagebox.showerror("Error", "Invalid password length")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
