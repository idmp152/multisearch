from pydantic import BaseModel


class QueryResponse(BaseModel):
    """Response dataclass for the /search method"""

    title: str
    description: str
    url: str
    engine: str
