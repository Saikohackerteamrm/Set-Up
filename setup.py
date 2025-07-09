from os import system as ALLMasTerx1001
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred

bblack = "\033[1;30m"  # Black
M = "\033[1;31m"       # Red
H = "\033[1;32m"       # Green
Y = "\033[1;33m"       # Yellow
bblue = "\033[1;34m"   # Blue
P = "\033[1;35m"       # Purple
C = "\033[1;36m"       # Cyan
B = "\033[1;37m"       # White

my_color = [B, C, P, H]
warna = random.choice(my_color)

logo = ("""
\033[1;34m
      
 _______                     _________
(  ____ \       |\     /|    \__   __/
| (    \/       | )   ( |       ) (   
| (_____  _____ | (___) | _____ | |   
(_____  )(_____)|  ___  |(_____)| |   
      ) |       | (   ) |       | |   
/\____) |       | )   ( |       | |   
\_______)       |/     \|       )_(   
                                      
                      version : 0.2              
\033[1;33mo|--------------------------------------------------------------\033[1;33m|o
\033[1;33mo| \033[1;32mDeveloper     : \033[1;33mR.M RONY ALI      
\033[1;33mo| \033[1;32mTeam          : \033[1;33mS-H-T                       
\033[1;33mo| \033[1;32mTools Type    : \033[1;33mFree                       
\033[1;33mo| \033[1;32mVersion       : \033[1;33m0.2                                   
\033[1;33mo| \033[1;32mTools Status  : \033[1;33mTerminal Setup    
\033[1;33mo|--------------------------------------------------------------\033[1;33m|o
""")

def linex():
    print('\033[1;33mo|--------------------------------------------------------------\033[1;33m|o')

def clear():
    os.system('clear')
    print(logo)

def install_package(package):
    print(f"Installing: {package}")
    ALLMasTerx1001(package)

def RONY():
    clear()
    ALLMasTerx1001('xdg-open https://facebook.com/groups/694288526013401/')
    print(f'{B} [{warna}01{B}] Full Setup [ Unique:- 90 ] ')
    print(f'{B} [{warna}02{B}] Join Telegram Channel')
    print(f'{B} [{warna}00{B}] EXIT PROGRAM')
    linex()
    option = input(f' {B}[{warna}??{B}] CHOOSE OPTION>> ')
    
    if option in ['01', '1']:
        FULLSETUP()
    elif option in ['02', '2']:
        ALLMasTerx1001('xdg-open https://t.me/rm7669')
    else:
        exit('Thanks for using!')

def FULLSETUP():
    clear()
    packages = [
    
"pkg update -y",
"pkg upgrade -y",
"pkg install python -y",
"pkg install python2 -y",
"pkg install python3 -y",
"pkg install python-static -y",
"pkg install python2-static -y",
"pkg install python-tkinter -y",
"pkg install python-pip",
"pkg install vim-python -y",
"pkg install weechat-python-plugin -y",
"pkg install git -y",
"pkg install figlet -y",
"pkg install cmatrix -y",
"pkg install toilet -y",
"pkg install nano -y",
"pkg install php -y",
"pkg install fish -y",
"pkg install ruby -y",
"pkg install openssh -y",
"pkg install wget -y",
"pkg install curl -y",
"pkg install proot -y",
"pkg install help",
"pkg install dnsutils",
"pkg install perl",
"pkg install lua",
"pkg install parallel",
"pkg install nmap",
"pkg install bash",
"pkg install clang",
"pkg install w3m",
"pkg install hydra",
"pkg install cowsay",
"pkg install tar",
"pkg install zip",
"pkg install unzip",
"pkg install net-tools",
"pkg install tor -y",
"pkg install sudo -y",
"pkg install wireshark",
"pkg install wgetrc",
"pkg install wcalc",
"pkg install openssl",
"pkg install openssl-tool",
"pkg install bmon",
"pkg install vpn",
"pkg install unrar",
"pkg install goaccess",
"pkg install golang",
"pkg install tmux",
"pkg install mtools",
"pkg install screen",
"pkg install neofetch",
"pkg install mariadb",
"pkg install dropbear",
"pip install pip",
"pip install rich",
"pip install bs4",
"pip2 install bs4",
"pip install astroid",
"pip install autopep8",
"pip install certifi",
"pip install chardet",
"pip install colorama",
"pip install future",
"pip install idna",
"pip install isort",
"pip install lazy-object-proxy",
"pip install lolcat",
"pip install mccabe",
"pip install Pillow",
"pip install pilo",
"pip install pycodestyle",
"pip install pyfiglet",
"pip install pylint",
"pip install requests",
"pip2 install requests",
"pip install setuptools",
"pip install six",
"pip install termcolor",
"pip install toml",
"pip install urllib3",
"pip install wheel",
"pip install wrapt",
"pip install youtube-dl",
"pip install mechanize",
"pip2 install wget",
"pip2 install mechanize",
    ]
    
  
    with tred(max_workers=4) as executor:
        executor.map(install_package, packages)
RONY()