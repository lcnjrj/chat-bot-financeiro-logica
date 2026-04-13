# 💰 Assistente Financeiro IA para Autónomos

Este é um app digital leve e inteligente, projetado para rodar localmente no **Lubuntu**. O assistente utiliza IA Generativa (Google Gemini) para ajudar freelancers e trabalhadores autónomos a gerir rendas variáveis, priorizar gastos e manter uma reserva de segurança financeira.

## 🚀 Funcionalidades

- **Gestão de Renda Variável:** Registo de múltiplas entradas e saídas com cálculo de saldo em tempo real.
- **Análise Inteligente de Prioridades:** Classificação automática de gastos entre *Essencial* (segurança) e *Supérfluo* (estratégia de corte).
- **Gatilho de Zona de Reserva (22%):** Quando o saldo atinge 22% da receita total, a IA muda automaticamente para o **Modo Consultoria Proativa**, adotando um tom mais rigoroso e focado em sobrevivência financeira.
- **Chat Interativo:** Interface de chat contextualizada que conhece os teus números e sugere poupanças personalizadas.
- **Dicas de Poupança:** Área dedicada a estratégias para quem não possui rendimento fixo.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web:** Flask (Leve e rápido)
- **IA:** Google Gemini API (Modelo 1.5-Flash - Gratuito)
- **Banco de Dados:** SQLite (Embutido, sem necessidade de servidor externo)
- **Frontend:** HTML5, CSS (Tailwind CSS via CDN) e JavaScript (Fetch API)

## 📋 Pré-requisitos

Antes de começar, certifica-te de que tens o Python instalado no teu Lubuntu:

```bash
sudo apt update
sudo apt install python3 python3-pip
