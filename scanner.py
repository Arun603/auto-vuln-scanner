import nmap
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def scan_target(target):
    nm = nmap.PortScanner()
    print(Fore.CYAN + f"[*] Scanning {target}...")
    nm.scan(hosts=target, arguments="-T4 -F")

    for host in nm.all_hosts():
        print(Fore.GREEN + f"\nHost: {host} ({nm[host].hostname()})")
        print(Fore.YELLOW + f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(Fore.MAGENTA + f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in sorted(ports):
                print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")