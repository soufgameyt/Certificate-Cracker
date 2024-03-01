import itertools
import string
import xml.etree.ElementTree as ET
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
from cryptography.x509.oid import ExtensionOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
import sys
import time
from colorama import *
from pystyle import *
import os 

# soufgame was here

intro = """
 ██████╗███████╗██████╗ ████████╗    ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗    ██████╗ ██╗   ██╗
██╔════╝██╔════╝██╔══██╗╚══██╔══╝   ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║     █████╗  ██████╔╝   ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝   ██████╔╝ ╚████╔╝  by soufgame
██║     ██╔══╝  ██╔══██╗   ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗   ██╔═══╝   ╚██╔╝  
╚██████╗███████╗██║  ██║   ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██╗██║        ██║   
 ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                                                                                                                     

                                               > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


def check_p12_password(p12_path, p12_password):
    try:
        with open(p12_path, 'rb') as file:
            p12_data = file.read()

        load_key_and_certificates(p12_data, p12_password.encode(), backend=default_backend())
        return True
    except Exception:
        return False


def startCrack():
    MAX_LENGTH = 25

    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?"
    characters = string.ascii_letters + string.digits + special_characters


    p12_path = input("Enter the path of the certificate (P12) file: ")

    while not os.path.exists(p12_path):
         print("Invalid path. Please enter a valid path.")
         p12_path = input("Enter the path of the certificate (P12) file: ")


    for length in range(1, MAX_LENGTH + 1):
        for combination in itertools.product(characters, repeat=length):
            print(''.join(combination))
            p12_password = ''.join(combination)
            if check_p12_password(p12_path, p12_password):
                print("Password is correct.")
                exit()
            else:
                print("Password is incorrect.")


while True:
    Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
    Write.Print("\n1. Crack P12 Password", Colors.red_to_yellow)
    Write.Print("\n2. Close", Colors.red_to_yellow)
    Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
    user_input = input()
    if user_input in ['1']:
        startCrack()
    elif user_input == "2":
        Write.Print("\nExiting the program...", Colors.red_to_yellow)
        break
    else:
        Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)
