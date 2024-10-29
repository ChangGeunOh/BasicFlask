from pydantic import BaseModel


from pydantic import BaseModel, Field
from typing import Optional

class MemberData(BaseModel):
    id: Optional[int] = Field(None, description="Unit member ID")
    userid: str = Field(..., max_length=16, description="User ID")
    userpw: Optional[str] = Field("", max_length=512, description="")
    name: str = Field(..., max_length=32, description="Member name")
    group0: Optional[str] = Field("", max_length=32, description="")
    group1: Optional[str] = Field("", max_length=32, description="")
    group2: Optional[str] = Field("", max_length=32, description="")
    group3: Optional[str] = Field("", max_length=32, description="")
    group4: Optional[str] = Field("", max_length=32, description="")
    group5: Optional[str] = Field("", max_length=32, description="")

    class Config:
        from_attributes = True  
        
        
        
class MemberTokenData(BaseModel):
    userid: str = Field(..., max_length=16, description="User ID")
    name: str = Field(..., max_length=32, description="Member name")
    group0: Optional[str] = Field("", max_length=32, description="")
    group1: Optional[str] = Field("", max_length=32, description="")
    group2: Optional[str] = Field("", max_length=32, description="")
    group3: Optional[str] = Field("", max_length=32, description="")
    group4: Optional[str] = Field("", max_length=32, description="")
    group5: Optional[str] = Field("", max_length=32, description="")
    
    class Config:
        from_attributes = True


