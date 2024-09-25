from typing import Optional
from pydantic import BaseModel


class LogRequest(BaseModel):
    message: str
    level: int
    namespace: str
    thread_model: str = "SINGLE"  
    write_mode: str = "SYNC" 
    timestamp_format: Optional[str] = None