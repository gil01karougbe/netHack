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
                 \n\t2  - Scan
                 \n\t3  - SessionRST
                 \n\t4  - SYNflooding
                 \n\t5  - HTTPflooding
                 \n\t6  - Smurf
                 \n\t7  - TCPhijacking
                 \n\t8  - Macflooding
                 \n\t9  - PingOfDeath
                 \n\t10 - ICMPflood
                 \n\t11 - MACspoofing
                 \n\n --> Attack  """

, help="""Provide your attacks number : \t\n
                 1  - ARPpoisonning\n
                 2  - Scan\n
                 3  - SessionRST\n
                 4  - SYNflooding\n
                 5  - HTTPflooding\n
                 6  - Smurf\n
                 7  - TCPhijacking\n
                 8  - MACflooding\n
                 9  - PingOfDeath\n
                 10 - ICMPflood\n
                 11 - MACspoofing
          """)
# main function
def main(id):
    print('')
    time.sleep(0.4)

    if id == '1':
        ARPpoisonning()

    elif id == '2':
        Scan()

    elif id == '3':
        SessionRST()

    elif id == '4':
        SYNflood()

    elif id == '5':
        HTTPflood()

    elif id == '6':
        Smurf()

    elif id == '5':
        SessionRST()

    elif id == '6':
        Scan()

    elif id == '7':
        TCPhijacking()

    elif id == '8' :
        MACflood()

    elif id == '9':
        PingOfDeath()

    elif id == '10':
        ICMPflood()

    elif id == '11':
        MACspoofing()
    else:
        print('\nPlease enter a Correct number attack, Show help for more details (--help)')



