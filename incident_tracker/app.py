from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .models import Incidents
from .schemas import Incident, IncidentUpdate, IncidentResponse

app = FastAPI()


@app.get("/incident", response_model=list[IncidentResponse])
async def get_incident_by_status(status: str | None = None, db: Session = Depends(get_db)) -> list[Incident]:
    query = select(Incidents)
    if status:
        query = query.where(Incidents.status == status)
    result = db.execute(query)
    incidents = result.scalars().all()
    return incidents


@app.post("/incident")
async def create_incident(incident_data: Incident, db: Session = Depends(get_db)) -> None:
    db_incident = Incidents(description=incident_data.description, status=incident_data.status, source=incident_data.source, create_dt=datetime.now())
    db.add(db_incident)
    db.commit()


@app.put("/incident/{incident_id}")
async def update_incident(
    incident_id: int,
    update_data: IncidentUpdate,
    db: Session = Depends(get_db),
) -> None:
    incident = db.get(Incidents, incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    incident.status = update_data.status
    db.commit()
