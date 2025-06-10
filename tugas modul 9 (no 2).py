import os
from termcolor import cprint

os.system("cls")
print("LOGO ADIDAS")

logo_stripes_data = [
  "                           ",
    "                                ###",
    "                            ##########",
    "                         #################",
    "                            ################",
    "                       ###     ################ ",
    "                   ##########    ################",
    "                ################    ################",
    "                  ################    ################",
    "         ###        ################    ################",
    "      #########       ################    ################",
    "     #############      ################    ################",
    "        #############     ################     ################",
]

for baris in logo_stripes_data:
    for piksel in baris:
        if piksel == '#':
            cprint(' ', on_color='on_black', end='')
        else:
            cprint(' ', color='white', end='')
    print("\n")

cprint("                        █   ██        █","black")
cprint("           ████     █████         █████     ████   █████ ","black")
cprint("          █    █   █    █   ██   █     █   █    █  ██","black")
cprint("          █    █   █    █   ██   █     █   █    █    ███","black")
cprint("           █████    █████   ██    █████     █████  █████","black")
