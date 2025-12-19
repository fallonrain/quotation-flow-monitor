# 📊 Quotation Flow Monitor

Projeto backend desenvolvido em **Python + FastAPI** com foco em monitoramento de fluxo de cotações, inspirado em cenários reais de **RFQ / Procurement**, como os enfrentados em plataformas B2B.

O objetivo é identificar cotações paradas aguardando ação do fornecedor e gerar alertas baseados em SLA.

---

## 🎯 Motivação

Em fluxos de compras B2B, cotações podem ficar abertas por longos períodos sem retorno do fornecedor, impactando:

- tempo de negociação
- eficiência do processo
- tomada de decisão

Este projeto simula esse cenário e oferece visibilidade sobre o estado das cotações.

---

## 🧠 Funcionalidades

- Criação de cotações
- Listagem e filtro por status
- Persistência de dados com SQLite
- Monitoramento de SLA (cotações paradas)
- Endpoint de alertas
- Dashboard simples para visualização

---

## 🧱 Arquitetura

O projeto segue separação de responsabilidades:

app/
├── main.py # API e rotas
├── services.py # Regras de negócio
├── database.py # Conexão com banco
├── models.py # Modelos de domínio
└── templates/ # Dashboard HTML

yaml
Copy code

Essa organização facilita manutenção, testes e evolução futura.

---

## ⚙️ Tecnologias utilizadas

- Python 3.12
- FastAPI
- SQLite
- Jinja2
- Uvicorn

---

## 🚀 Como executar localmente

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
Acesse:

API Docs: http://127.0.0.1:8000/docs

Dashboard: http://127.0.0.1:8000/

📈 Próximos passos (ideias)
Integração com webhook (Slack / Discord)

Autenticação

Métricas de SLA por status

Exportação de dados

👩‍💻 Autor
Projeto desenvolvido por Thiago Fernandes
Voltado a estudos de backend, arquitetura e produtos B2B.