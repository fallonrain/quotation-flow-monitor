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

## 📌 Status disponíveis para cotações

Atualmente, o sistema aceita apenas os seguintes status padronizados:

- `WAITING_SUPPLIER` — Cotação aberta aguardando retorno do fornecedor
- `APPROVED` — Cotação aprovada
- `REJECTED` — Cotação rejeitada

Esses valores são validados pela API e qualquer status fora desse padrão será rejeitado.

---

## 📤 Exemplo de requisição

### Criar uma cotação

**Endpoint:**

POST /quotations


**Query Params:**


status=WAITING_SUPPLIER


**Exemplo de resposta:**
```json
{
  "message": "Quotation created"
}

📥 Exemplo de alerta
### Consultar alertas de SLA

**Endpoint:**


GET /alerts?sla_hours=24


**Exemplo de resposta:**
```json
{
  "sla_hours": 24,
  "total_alerts": 1,
  "alerts": [
    {
      "id": 1,
      "status": "WAITING_SUPPLIER",
      "opened_at": "2025-01-18T10:00:00"
    }
  ]
}
---

## 🏗️ Arquitetura

O projeto segue separação de responsabilidades:

```text
app/
├── main.py        # API e rotas
├── services.py    # Regras de negócio
├── database.py    # Conexão com banco
├── models.py      # Modelos de domínio
└── templates/     # Dashboard HTML


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
