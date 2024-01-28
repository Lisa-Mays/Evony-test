import os
import tkinter as tk
from tkinter import filedialog

class SetupWizard:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Setup Wizard")

        self.project_name = ""
        self.installation_path = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to the Project Setup Wizard").pack(pady=10)

        tk.Label(self.root, text="Project Name:").pack(pady=5)
        self.project_name_entry = tk.Entry(self.root)
        self.project_name_entry.pack(pady=5)

        tk.Button(self.root, text="Select Installation Folder", command=self.choose_installation_path).pack(pady=10)

        tk.Button(self.root, text="Start Setup", command=self.start_setup).pack(pady=10)

    def choose_installation_path(self):
        self.installation_path = filedialog.askdirectory()
        if self.installation_path:
            print(f"Installation Path: {self.installation_path}")

    def start_setup(self):
        self.project_name = self.project_name_entry.get()
        if not self.project_name:
            tk.messagebox.showerror("Error", "Please enter a project name.")
            return

        if not self.installation_path:
            tk.messagebox.showerror("Error", "Please select an installation folder.")
            return

        self.install_project()

    def install_project(self):
        # Perform installation tasks, e.g., create project directory, copy files, etc.
        print(f"Installing '{self.project_name}' to '{self.installation_path}'...")
        # Add your installation logic here.

        # Close the setup wizard when done.
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    setup_wizard = SetupWizard(root)
    root.mainloop()
