from colorama import init,  Fore, Back, Style
init()

print(f"{Fore.RED}Way to go team")
print(f"{Back.GREEN}All the way to state{Style.RESET_ALL}")
print('back to normal now')

import os
from termcolor import colored, cprint

if os.name == 'nt':
    os.system('color')

text = colored("Hello, world!", "red", attrs=["reverse", "blink"])

print(text)
cprint("Hello, World", "green", "on_blue")


