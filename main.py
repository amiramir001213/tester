import os
import socket
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    ip = input(Fore.CYAN + "Enter IPv4 address: ")

    print(Fore.YELLOW + "\n--- Ping ---" + Style.RESET_ALL)
    os.system(f"ping -c 4 {ip}")

    print(Fore.YELLOW + "\n--- Traceroute ---" + Style.RESET_ALL)
    os.system(f"traceroute {ip}")

    print(Fore.YELLOW + "\n--- Checking port 53 ---" + Style.RESET_ALL)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((ip, 53))
        if result == 0:
            print(Fore.GREEN + "Port 53 is open.")
        else:
            print(Fore.RED + "Port 53 is closed.")
        sock.close()
    except Exception as e:
        print(Fore.RED + f"Error checking port: {e}")

if __name__ == "__main__":
    main()
