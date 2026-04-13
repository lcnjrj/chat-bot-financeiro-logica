# 1. Preparação do Sistema
Abra o terminal (Ctrl+Alt+T) e garanta que o Python e o gerenciador de pacotes estão atualizados.

Bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git -y
2. Isolamento do Projeto (Ambiente Virtual)
No Linux, é uma boa prática não instalar bibliotecas diretamente no sistema para evitar conflitos.

Bash
# Crie a pasta do projeto
mkdir ~/financeiro_ia && cd ~/financeiro_ia

# Crie o ambiente virtual (venv)
python3 -m venv venv

# Ative o ambiente
source venv/bin/activate
Note que, após ativar, o nome (venv) aparecerá no início da linha do terminal.

3. Instalação das Dependências
Com o ambiente ativado, instale apenas o necessário para a aplicação rodar:

Bash
pip install flask google-generativeai
4. Estrutura de Pastas "Express"
Crie rapidamente a estrutura que desenhamos nos passos anteriores:

Bash
mkdir static templates
touch app.py static/style.css templates/index.html
5. Configuração da API Key (Segurança)
Em vez de colar a chave direto no código (o que é perigoso se você subir para o GitHub), no Lubuntu você pode exportar como variável de ambiente no seu .bashrc ou apenas no terminal atual:

Bash
export GEMINI_API_KEY="sua_chave_aqui"
(No seu app.py, você usaria os.getenv('GEMINI_API_KEY') para ler este valor).

6. Execução e Teste
Para rodar o servidor Flask localmente:

Bash
python3 app.py
O terminal mostrará algo como * Running on http://127.0.0.1:5000.
Basta abrir o navegador (Firefox ou Falkon, que costumam vir no Lubuntu) e acessar esse endereço.

