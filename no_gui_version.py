# BY SMOODIE
from tkinter import *
from tkinter import filedialog
from pathlib import Path

def main():
    # ASCII GUI
    print('------------------------------\n'
          '| SPOOKY EDITOR / BY SMOODIE |\n'
          '------------------------------\n')
    print("\n[#] Select your game directory (run the gui version for a tutorial ) :")

    # Ask for a directory
    directory = filedialog.askdirectory(title="Select the game directory...")

    # Verify if valid
    if not directory:
        print("\n[!] ERROR: Please select a directory.")
        return

    # Open the save file
    path = Path(directory) / "save_data_main.ini"
    if not path.is_file():
        print("\n[!] ERROR: Save file doesn't exist! Try to create a new Game.")
        return
    with open(path, 'r') as save_file:
        lines = save_file.readlines()

    # Changing room value
    room = input("\n[#] Change the room value (0-999): ")
    if not room.isdigit() or not 0 <= int(room) <= 999:
        print("[!] ERROR: You can only enter an integer between 0 and 999.")
        return

    lines[5] = f"room={room}\n"
    with open(path, 'w') as save_file:
        save_file.writelines(lines)
    print("[*] Value changed successfully.")

    # Change axe weapon
    if lines[8].strip() == 'weapon=0':
        choice = input("Do you want to get the axe (weapon) ? [Y/N]")
        if choice.lower() == 'y':
            lines[8] = "weapon=1\n"
            with open(path, 'w') as save_file:
                save_file.writelines(lines)

if __name__ == '__main__':
    main()
