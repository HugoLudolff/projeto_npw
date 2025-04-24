# 🖥️ NetPing Watcher

Um projeto simples de monitoramento de rede com **Python**, que verifica se dispositivos estão online ou offline utilizando `ping`, gera um log com o status e envia um **alerta por e-mail** em caso de falha.

---

## 🚀 Funcionalidades

- ✅ Verificação automática de conectividade com dispositivos de rede.
- 📨 Envio de alerta por e-mail quando algum dispositivo está **OFFLINE**.
- 🗂️ Log dos eventos com data e hora.
- 💻 Compatível com Windows, Linux e macOS.

---

## 🛠️ Requisitos

- Python 3 instalado
- Conta de e-mail com acesso SMTP habilitado (ex: Gmail)
- Acesso à internet para envio de e-mails

---

## 🧪 Como usar
1. Edite o arquivo devices.txt com os IPs ou nomes dos dispositivos que deseja monitorar (um por linha):
2. Configure seu e-mail no arquivo mensagem.py ou via .env.
3. Execute o script: python ping_monitor.py

O resultado será exibido no terminal e também salvo em log.txt.

📧 Exemplo de alerta por e-mail
Assunto: Alerta de Dispositivo Offline
Corpo: O dispositivo 192.168.0.15 está offline


