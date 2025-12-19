from fastapi import FastAPI, Query
from app.services import init_db, add_quotation, get_quotations
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.services import get_stale_quotations
from app.models import QuotationStatus


app = FastAPI(title="Quotation Flow Monitor")
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def startup():
    init_db()

@app.post("/quotations")
def create_quotation(status: QuotationStatus):
    add_quotation(status)
    return {"message": "Quotation created"}

@app.get("/quotations")
def list_quotations(status: str | None = Query(default=None)):
    rows = get_quotations(status)

    return [
        {
            "id": row[0],
            "status": row[1],
            "opened_at": row[2]
        }
        for row in rows

        
    ]

from app.services import get_stale_quotations

@app.get("/alerts")
def quotation_alerts(sla_hours: int = 24):
    alerts = get_stale_quotations(sla_hours)

    return {
        "sla_hours": sla_hours,
        "total_alerts": len(alerts),
        "alerts": alerts
    }

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    rows = get_quotations()

    total = len(rows)
    waiting = len([r for r in rows if r[1] == "WAITING_SUPPLIER"])
    approved = len([r for r in rows if r[1] == "APPROVED"])

    alerts = get_stale_quotations()
    alerts_count = len(alerts)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "total": total,
            "waiting": waiting,
            "approved": approved,
            "alerts": alerts,
            "alerts_count": alerts_count
        }
    )


