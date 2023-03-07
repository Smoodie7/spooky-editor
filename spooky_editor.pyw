from tkinter import *
from tkinter import filedialog, messagebox
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
            self.check_file_existence()

    def check_file_existence(self):
        if self.directory is not None:  # If 'directory' isn't null
            path = Path(f"{self.directory}/save_data_main.ini")

            if path.is_file():  # If save file exist
                self.master.destroy()
                self.show_editor_window()
            else:  # Error the file doesn't exist
                messagebox.showerror("Error!", "Save file doesn't exist!\nTry to create a new Game.")
                self.directory = None

    def show_editor_window(self):
        tk1 = Tk()
        tk1.geometry("720x520")
        label = Label(tk1, text="Spooky Editor")
        label.pack(pady=30)
        label.config(font=("Helvetica", 23))
        tk1.mainloop()

def main():
    root = Tk()
    SpookyEditor(root)
    root.mainloop()

if __name__ == '__main__':
    main()
