# Utilizamos colorama para colorear el texto
from colorama import init, Fore, Style

no_color = Style.RESET_ALL
ncs = Style.RESET_ALL + " "

init()

def main():
    print(Fore.RED + "ERROR" + ncs + "Texto después del error")

main()