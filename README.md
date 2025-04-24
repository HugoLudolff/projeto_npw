
Um projeto simples de monitoramento de rede com Python. O script verifica se os dispositivos estão online ou offline usando ping, grava um log com data/hora e envia um alerta por e-mail se algum estiver offline.

FUNCIONALIDADES:
  Verifica conectividade de dispositivos usando ping
  Envia alerta por e-mail quando um dispositivo está OFFLINE
  Gera log com data e hora
  Compatível com Windows, Linux e macOS

REQUISITOS:
  Python 3
  Conta de e-mail (com SMTP habilitado)
  Acesso à internet

INSTALAÇÃO:
  Clone o repositório: git clone https://github.com/seu-usuario/netping-watcher.git
  cd netping-watcher
  (Opcional) Crie um ambiente virtual: python -m venv venv 
  source venv/bin/activate (no Windows: venv\Scripts\activate)

  Instale as dependências: pip install -r requirements.txt
  Se usar variáveis de ambiente, instale também: pip install python-dotenv

COMO USAR:
  No arquivo devices.txt, adicione os IPs ou domínios, um por linha
  Configure seu e-mail no arquivo mensagem.py ou .env.
  Execute o script: python ping_monitor.py

  Resultados serão exibidos no terminal e salvos em log.txt.

EXEMPLO DE ALERTA:
  Assunto: Alerta de Dispositivo Offline
  Mensagem: O dispositivo 192.168.0.10 está offline

ESTRUTURA DO PROJETO:
  ping_monitor.py → Script principal
  mensagem.py → Função para envio de e-mail
  devices.txt → Lista de dispositivos
  log.txt → Log dos status
  README.md → Instruções

SEGURANÇA:
  Evite deixar a senha no código. Use variáveis de ambiente ou um arquivo .env.

Este projeto é open-source. Fique à vontade para usar e adaptar.
