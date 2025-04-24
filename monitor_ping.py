import os
import platform
from datetime import datetime
from mensagem import alerta

# Detecta o comando certo para o sistema operacional #
system_os = platform.system().lower()
param = "-n" if system_os == "windows" else "-c"


# Lê a lista de dispositivos #
with open("devices.txt", "r") as file:
    devices = [line.strip() for line in file.readlines()]  

# Cria o arquivo de log #
with open("log.txt", "a") as log_file:
    for device in devices:
        response = os.system(f"ping {param} 1 {device} > nul" if system_os == "windows" else f"ping {param} 1 {device} > /dev/null")

        status = "ONLINE" if response == 0 else "OFFLINE"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{timestamp} - Dispositivo {device} está {status}\n"

        # Envia o alerta se o dispositivo estiver offline #
        if status == "OFFLINE":
            alerta(device)


        # Adiciona o log no arquivo #   
        print(log_line)
        log_file.write(log_line+"\n")