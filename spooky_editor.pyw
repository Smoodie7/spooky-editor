# BY SMOODIE
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path

tk = Tk()
tk.geometry("720x520")
tk.title('Spooky Editor | by Smoodie')
ico = PhotoImage(file='icon.png')
tk.iconphoto(False, ico)

directory = None


def main():
    print('Closed')  # When the Window is closed


def file_path():  # Function for the 'select repertory' button
    directory1 = filedialog.askdirectory(title="Select the game directory...")
    global directory
    directory = directory1
    del directory1
    return directory


label = Label(tk, text="Select your game directory")
label.pack(pady=30)
label.config(font=("Helvetica", 23))

btn = Button(tk, text="Click here to select one...", command=file_path, width=40)  # Select repertory button
btn.pack(pady=20)

label = Label(tk, text="--How to look for the game repertory ?--")  # The 'tutorial'
label.pack(padx=30, pady=10)
label.config(font=("Arial", 13))
label = Label(tk, text="(if you have a non steam version you should already know)\n"
                       "1.Open steam and select Spooky Jump scare Mansion (steam version)\n"
                       "2.Click the setting button at the left of the screen\n"
                       "3.Select 'Properties' then 'Local Files'\n"
                       "4.Then click 'Browse...' and copy the game repertory\n")
label.pack(pady=0)
label.config(font=("Arial", 8))

label = Label(tk, text="by Smoodie")
label.pack(pady=30, padx=50)
label.config(font=("Arial", 8))

if directory is not None:  # If 'directory' isn't null
    path = Path(f"{directory}/save_data_main.ini")

    if path.is_file():  # If save file exist
        tk.destroy()
        del tk
        tk1 = Tk()
        tk1.geometry("720x520")
        label = Label(tk1, text="Spooky Editor")
        label.pack(pady=30)
        label.config(font=("Helvetica", 23))

    else:  # Error the file doesn't exist
        messagebox.showerror("Error!", "Save file doesn't exist!\nTry to create a new Game.")
        print('Error01')
        del directory
        del path


mainloop()  # The loop for the window


if __name__ == '__main__':
    main()
