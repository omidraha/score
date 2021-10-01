# noinspection PyPackageRequirements
from pydantic import BaseModel


class ScoreRequest(BaseModel):
    """
    This class define Request data model for score API
    """
    repo: str


class ScoreResponse(BaseModel):
    """
    This class define Response data model for score API
    """
    repo: str
    score: int


class ScoreExceptionResponse(BaseModel):
    """
    This class define Response data model for score exception API
    """
    message: str
