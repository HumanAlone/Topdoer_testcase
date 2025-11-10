from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    NEW = "new"
    IN_PROGRESS = "in progress"
    CLOSED = "closed"


class SourceEnum(str, Enum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"


class Incident(BaseModel):
    description: str
    status: StatusEnum
    source: SourceEnum


class IncidentUpdate(BaseModel):
    status: StatusEnum
