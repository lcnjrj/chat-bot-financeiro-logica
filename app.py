import os
import sqlite3
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configuração da API Gemini (Substitua pela sua chave)
genai.configure(api_key="SUA_CHAVE_API_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT CHECK(tipo IN ('receita', 'despesa')),
            valor REAL NOT NULL,
            categoria TEXT CHECK(categoria IN ('essencial', 'superfluo')),
            descricao TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def calcular_resumo():
    conn = get_db_connection()
    receita = conn.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='receita'").fetchone()[0] or 0
    despesa = conn.execute("SELECT SUM(valor) FROM transacoes WHERE tipo='despesa'").fetchone()[0] or 0
    conn.close()

    saldo = receita - despesa
    percentual_reserva = (saldo / receita * 100) if receita > 0 else 0
    return receita, despesa, saldo, percentual_reserva

@app.route('/')
def index():
    receita, despesa, saldo, percentual = calcular_resumo()
    return render_template('index.html', receita=receita, despesa=despesa, saldo=saldo, percentual=percentual)

@app.route('/add_transacao', methods=['POST'])
def add_transacao():
    dados = request.json
    conn = get_db_connection()
    conn.execute("INSERT INTO transacoes (tipo, valor, categoria, descricao) VALUES (?, ?, ?, ?)",
                 (dados['tipo'], dados['valor'], dados['categoria'], dados['descricao']))
    conn.commit()
    conn.close()
    return jsonify({"status": "sucesso"})

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('mensagem')
    receita, despesa, saldo, percentual = calcular_resumo()

    # Lógica de Tom de Voz (Gatilho 22%)
    tom = "amigável e focado em crescimento" if percentual > 22 else "PROATIVO E ANALÍTICO, pois o usuário está na Zona de Reserva Crítica"

    prompt_sistema = f"""
    Você é um assistente financeiro para autônomos.
    Contexto Atual: Receita R${receita}, Saldo R${saldo}, Reserva {percentual:.1f}%.
    Seu tom deve ser {tom}.
    Se o gasto for supérfluo e a reserva estiver baixa, sugira cortes.
    Sempre dê dicas curtas de como criar uma poupança para quem tem renda variável.
    """

    response = model.generate_content(prompt_sistema + "\nUsuário: " + user_msg)
    return jsonify({"resposta": response.text})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
