# Code by AkinoAlice@TyrantRey

from pydantic import BaseModel
from datetime import datetime


class PatentInfo(BaseModel):
    ApplicationDate: int = 0
    PublicationDate: int = 0
    ApplicationNumber: str = ""
    PublicationNumber: str = ""
    Applicant: str = ""
    Inventor: str = ""
    Attorney: str = ""
    Priority: str = ""
    GazetteIPC: str = ""
    IPC: str = ""
    GazetteVolume: str = ""
    KindCodes: str = ""
