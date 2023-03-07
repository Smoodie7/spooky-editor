from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from pathlib import Path


class SpookyEditor:
    def __init__(self, master):
        self.master = master
        self.master.geometry("720x520")
        self.master.title('Spooky Editor | by Smoodie')
        ico = PhotoImage(file='icon.png')
        self.master.iconphoto(False, ico)

        self.directory = None

        self.label = Label(self.master, text="Select your game directory")
        self.label.pack(pady=30)
        self.label.config(font=("Helvetica", 23))

        self.btn = Button(self.master, text="Click here to select one...", command=self.file_path, width=40)  # Select repertory button
        self.btn.pack(pady=20)

        self.label = Label(self.master, text="--How to look for the game repertory ?--")  # The 'tutorial'
        self.label.pack(padx=30, pady=10)
        self.label.config(font=("Arial", 13))
        self.label = Label(self.master, text="(if you have a non steam version you should already know)\n"
                           "1.Open steam and select Spooky Jump scare Mansion (steam version)\n"
                           "2.Click the setting button at the left of the screen\n"
                           "3.Select 'Properties' then 'Local Files'\n"
                           "4.Then click 'Browse...' and copy the game repertory\n")
        self.label.pack(pady=0)
        self.label.config(font=("Arial", 8))

        self.label = Label(self.master, text="by Smoodie")
        self.label.pack(pady=30, padx=50)
        self.label.config(font=("Arial", 8))

    def file_path(self):  # Function for the 'select repertory' button
        directory1 = filedialog.askdirectory(title="Select the game directory...")
        if directory1:
            self.directory = directory1
            self.verify_directory()

    def verify_directory(self):
        if not self.directory:
            messagebox.showerror("Error", "Please select a directory.")
            return

        # Open the save file
        path = Path(self.directory) / "save_data_main.ini"
        if not path.is_file():
            messagebox.showerror("Error", "Save file doesn't exist! Try to create a new Game.")
            return
        with open(path, 'r') as save_file:
            lines = save_file.readlines()

        # Changing room value
        room = simpledialog.askstring("Input", "Change the room value (0-999): ", parent=self.master)
        if not room.isdigit() or not 0 <= int(room) <= 999:
            messagebox.showerror("Error", "You can only enter an integer between 0 and 999.")
            return

        lines[5] = f"room={room}\n"
        with open(path, 'w') as save_file:
            save_file.writelines(lines)
        messagebox.showinfo("Success", "Value changed successfully.")

        # Change axe weapon
        if lines[8].strip() == 'weapon=0':
            choice = messagebox.askyesno("Input", "Do you want to get the axe (weapon)?")
            if choice:
                lines[8] = "weapon=1\n"
                with open(path, 'w') as save_file:
                    save_file.writelines(lines)
                messagebox.showinfo("Success", "Axe weapon obtained successfully.")


root = Tk()
app = SpookyEditor(root)
root.mainloop()
