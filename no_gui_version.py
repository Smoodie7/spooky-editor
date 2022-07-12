#  BY SMOODIE
from tkinter import *
from tkinter import filedialog
from pathlib import Path
import time

#  All important variables here to simplify reading my code
directory = None
path = None
save = None
room = None


def main():
    print('------------------------------\n'
          '| SPOOKY EDITOR / BY SMOODIE |\n'
          '------------------------------\n')
    print("\n[#] Select your game directory (run the gui version for a tutorial ) :")
    tk = Tk()
    time.sleep(1)
    tk.geometry("0x0")
    tk.wm_attributes('-toolwindow', 'True')
    global directory
    directory = filedialog.askdirectory(title="Select the game directory...")
    path = Path(f"{directory}/save_data_main.ini")

    if path.is_file():  # If save file exist
        with open(path, 'r') as save:
            lines = save.readlines()
        print("\n[*] Your currently at the", lines[5])
        print("[!] Please choose a number superior than 0 and inferior than 1000!")
        room = input("[#] Change the room value : ")
    #   if room < '0' or room > '1000':
    #        print("[!] ERROR: You can't go to a negative or superior than 1000 room!")
    #        input("[*] Press Enter to continue...")
    #        exit()
    #   else:        (i need to convert str into int but idk how so nvm)
        lines[5] = "room=" + str(room) + "\n"
        with open(path, 'w+') as save:
            save.writelines(lines)
        print("[*] Value changed with success.")
        if lines[8] == 'weapon=0':
            choice = input("Do you want to get the axe (weapon) ? [Y/N]")
            if choice in ['y', 'Y']:
                lines[5] = "weapon=1\n"
                with open(path, 'w+') as save:
                    save.writelines(lines)

    elif directory is None or directory == '':  # If the user didn't choose a file
        print("\n[!] ERROR: Please select a repertory.")
    else:  # Error save file doesnt exist
        print("\n[!] ERROR: Save file doesn't exist! Try to create a new Game.")
    input("[*] Press Enter to continue...")
    exit()


if __name__ == '__main__':
    main()
