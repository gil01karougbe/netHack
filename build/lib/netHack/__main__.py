#!/usr/bin/python3
import click
import datetime
import pyfiglet
from pyfiglet import Figlet
import time
import progressbar
from colorama import Fore, init
from pathlib import Path

from netHack.Attacks import ARPpoisonning
from netHack.Attacks import SYNflood
from netHack.Attacks import HTTPflood
from netHack.Attacks import smurf
from netHack.Attacks import SessionRST
from netHack.Attacks import TCPhijacking
from netHack.Attacks import Scan
from netHack.Attacks import Macspoofing
# Print name of Tools using pyfiglet
print(Fore.GREEN + '\n')
f = Figlet(font='standard')
init(autoreset=True)
print(f.renderText("   net - H 4  k  R  "))

print('    v1.0')
init(autoreset=True)
print(Fore.BLUE + '    https://github.com/ensao ')
print('   ', Fore.GREEN + str(datetime.datetime.now()))
print('\n')


# Print Progress Bar :
def animated_marker(x):
    widgets = [Fore.GREEN + 'Loading :  ', progressbar.AnimatedMarker()]
    init(autoreset=True)
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(x):
        time.sleep(0.1)
        bar.update(i)
    bar.finish()

# Driver's code
animated_marker(5)
print('\n')


# For Option : using click library
@click.command()
@click.option("--id", prompt=Fore.GREEN + """[+] Please enter attack number : 
                 \n\t1  - ARPpoisonning
                 \n\t2  - SYNflood
                 \n\t3  - HTTPflood
                 \n\t4  - SMURF
                 \n\t5  - SessionRST
                 \n\t6  - Scan
                 \n\t7  - TCPhijacking
                 \n\t8  - Macspoofing
                 \n\n --> Attack  """

, help="""Provide your attacks number : \t\n
                 1  - ARPpoisonning \n
                 2  - SYNflood \n
                 3  - HTTPflood \n
                 4  - SMURF \n
                 5  - SessionRST \n
                 6  - Scan \n
                 7  - TCPhijacking \n
                 8  - Macspoofing
          """)
# main function
def main(name):
    print('')
    time.sleep(0.4)

    if name == '1':
        ARPpoisonning()

    elif name == '2':
        SYNflood()

    elif name == '3':
        HTTPflood()

    elif name == '4':
        smurf()

    elif name == '5':
        SessionRST()

    elif name == '6':
        Scan()

    elif name == '7':
        TCPhijacking()

    elif name == '8' :
        Macspoofing()

    else:
        print('\nPlease enter a Correct number attack, Show help for more details (--help)')



