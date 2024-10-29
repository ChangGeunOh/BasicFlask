from typing import Optional
from pydantic import BaseModel, Field


class TokenData(BaseModel):
    access_token: str = Field(..., description="JWT Access Token")
    refresh_token: Optional[str] = Field("", description="JWT Refresh Token")
    
    class Config:
        from_attributes = True
        
        