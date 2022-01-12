## libraries
import requests
import colorama
from colorama import Fore, Back, Style
import pyfiglet                                                                                                                                                
                                                                                                    

print(
    '''
 ____        
(҂`_´)
<,︻╦╤─ ҉ - -
_/﹋\_
   '''
)


pii = pyfiglet.figlet_format("IP Information")
print(pii)


ip = input(f"{Fore.CYAN} - Enter Target IP : ")

res = requests.get("https://ipinfo.io/")
data = res.json()
print(data)
print(Style.RESET_ALL)
