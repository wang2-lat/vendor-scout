from pydantic import BaseModel, Field
from typing import List, Optional

class Review(BaseModel):
    rating: float = Field(ge=0, le=5)
    project_type: str
    comment: str

class Vendor(BaseModel):
    id: int
    name: str
    skills: List[str]
    rating: float = Field(ge=0, le=5)
    completed_projects: int
    price_range: str
    location: str
    description: str
    reviews: List[Review] = []

class SearchFilters(BaseModel):
    skill: Optional[str] = None
    min_rating: Optional[float] = None
    min_projects: Optional[int] = None
