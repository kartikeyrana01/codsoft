import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Enter password length:")
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def generate_password(self):
        password_length = int(self.length_entry.get())

        if password_length < 4:
            messagebox.showerror("Error", "Password length must be at least 4 characters")
            return

        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(password_length))
        self.result_label.config(text="Generated Password: " + password)


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
