from concurrent.futures import process
from pyfiglet import figlet_format as fig
from termcolor import colored
from colorama import init
from os import getcwd
from pymem import *

init()

print(colored(fig("jude's  injector"), "yellow") + "\n")
dll_path = input(colored("DLL Filename: ", "yellow"))

if dll_path.replace("/", "") == dll_path:
    dll_path = getcwd() + "\\" + dll_path

dll_path_bytes = bytes(dll_path, "UTF-8")

print(str(dll_path_bytes))

proc = Pymem("GTA5.exe")
process.inject_dll(proc.process_handle, dll_path_bytes)
