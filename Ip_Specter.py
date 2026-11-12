import requests
import folium
from rich.console import Console
from rich.table import Table

CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"

BANNER = f"""{CYAN}{BOLD}
 ████████╗██████╗     ███████╗██████╗ ███████╗██████╗████████╗██████╗ ███████╗
 ╚══██╔══╝██╔══██╗    ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝
    ██║   ██████╔╝    ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝█████╗  
    ██║   ██╔═══╝     ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══╝  
 ████████╗██║         ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║███████╗
 ╚═══════╝╚═╝         ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
{RESET}
{YELLOW}             [ IP-SPECTRE // Geolocation Intelligence ]{RESET}
{MAGENTA}                   [ Developed for OSINT & Security ]{RESET}
{GREEN}    [ Author: Dhwarkesh4545 | GitHub: https://github.com/Dhwarkesh4545/Ip-Specter ]{RESET}
------------------------------------------------------------------------------------------------------------
"""

print(BANNER)

API_KEY = "" 
console = Console()

def get_ip_info(ip_address):
    if API_KEY:
        url = f"https://ipinfo.io/{ip_address}?token={API_KEY}"
    else:
        url = f"https://ipinfo.io/{ip_address}"
        
    response = requests.get(url)
    data = response.json()
    
    if "loc" in data:
        lat, lon = data["loc"].split(",")
        data["google_maps"] = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
        
    return data

if __name__ == "__main__":
    ip = input(f"{GREEN}{BOLD}[?] Enter Target IP Address: {RESET}").strip()
    
    with console.status("[bold cyan]Analyzing target...", spinner="dots"):
        data = get_ip_info(ip)

    table = Table(title=f"Target Intel: {ip}")
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for key, value in data.items():
        table.add_row(str(key), str(value))

    console.print(table)
