import subprocess
import sys
import shutil
import requests

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import requests
except ImportError:
    install("requests")

def get_ip_location(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'error' in data:
        return None

    lat = data.get('latitude')
    lon = data.get('longitude')
    return lat, lon

def print_centered(text):
    terminal_width = shutil.get_terminal_size().columns
    for line in text.splitlines():
        print(line.center(terminal_width))

def print_ascii_art():
    art = """
 ██▓ ██▓███     ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███      ▄▄▄▄ ▓██   ██▓     ██████ ▄▄▄█████▓ ██▀███   ▄▄▄       ███▄    █   ▄████ ▓█████
▓██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒   ▓█████▄▒██  ██▒   ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀
▒██▒▓██░ ██▓▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒   ▒██▒ ▄██▒██ ██░   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███
░██░▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄     ▒██░█▀  ░ ▐██▓░     ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄
░██░▒██▒ ░  ░     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒   ░▓█  ▀█▓░ ██▒▓░   ▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░   ░▒▓███▀▒ ██▒▒▒    ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░
 ▒ ░░▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░   ▒░▒   ░▓██ ░▒░    ░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░
 ▒ ░░░            ░        ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░     ░    ░▒ ▒ ░░     ░  ░  ░    ░        ░░   ░   ░   ▒      ░   ░ ░ ░ ░   ░    ░
 ░                          ░           ░  ░░ ░      ░  ░      ░  ░   ░         ░     ░ ░              ░              ░           ░  ░         ░       ░    ░  ░
                                            ░                                        ░░ ░
"""
    print("\033[35m")
    print_centered(art)
    print("\033[0m")
    print_centered("\033[33m Oiii você está usando uma ferramenta criada pelo strange, obrigado! Meu GitHub: https://github.com/Str44ng33\033[0m")

def print_footer():
    footer = """
      _____           _____
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           Yd
8(              "              )8
I8                             8I
 Yb,                         ,dP
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        Y8a         a8P'
          88,     ,88'
            "8b   d8"
             "8b d8"
              888'
                "
    """
    print("\033[35m")
    print_centered(footer)
    print("\033[0m")

def main():
    print_ascii_art()
    ip = input("Digite o IP para consultar a localização: ")
    location = get_ip_location(ip)

    if location:
        lat, lon = location
        print(f"> Latitude: {lat}")
        print(f"> Longitude: {lon}")
        print(f"> Abaixo está o link do Google Maps:")
        print(f"https://www.google.com/maps/@{lat},{lon},15z")
    else:
        print("Não foi possível obter a localização para o IP fornecido.")

    print("\nObrigado por estar usando uma ferramenta do Strang333!")
    print_footer()

if __name__ == "__main__":
    main()
