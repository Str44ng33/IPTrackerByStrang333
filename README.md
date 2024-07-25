# IP Tracker by Strang333

Este script em Python permite que você encontre a localização geográfica de qualquer endereço IP, exibindo a latitude, longitude e um link do Google Maps para visualização, bem básiquinho <3

## Requisitos

Para usar este script no seu sistema baseado em Arch Linux, certifique-se de ter os seguintes pacotes instalados:

*Baseado em Arch linux*

1. **Instale o pipx e requests**:
    ```bash
    sudo pacman -S python-pipx
    pipx install requests
    ```

2. **Configure um ambiente virtual**:
    ```bash
    pipx run python -m venv myenv
    source myenv/bin/activate.fish
    pip install requests
    ```
*Termux*

   ```bash
   pkg update
   pkg upgrade -y
   pkg install python -y
   pip install --upgrade pip
   pip install virtualenv
   python -m virtualenv myenv
   source myenv/bin/activate
   pip install requests
   ```
*Baseado em Ubuntu*

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip -y
pip install --user pipx
python3 -m pipx ensurepath
pipx install virtualenv
pipx run python -m venv myenv
source myenv/bin/activate
pip install requests
```

## Como Clonar e Rodar o Script

1. Clone o repositório:
    ```bash
    git clone https://github.com/Str44ng33/IPTrackerByStrang333
    ```

2. Navegue até o diretório do projeto (lembre de trocar o nome de usuário quando der o "cd":
    ```bash
    cd /home/(coloque seu nome de usuário)/IP-TRACKER-BY-STRANG333
    ```

3. Execute o script:
    ```bash
    python3 arquivo.py
    ```

Agora você está pronto para começar a rastrear IPs e ver suas localizações! Se tiver qualquer dúvida ou sugestão, fique à vontade para contribuir no repositório.

