from fastapi import APIRouter, HTTPException, status

from apps.score.serializer import ScoreResponse, ScoreRequest, ScoreExceptionResponse
from settings import GITHUB_ACCESS_TOKEN
from utility.exception import AppException
from utility.github_api import GitHubAPI

router = APIRouter()

TAG_SCORE = {
    "name": "score",
    "description": "The main API to score",
}


@router.post("/score/",
             # Hint the API docs by providing following info
             tags=["score"],
             response_model=ScoreResponse,
             responses={
                 status.HTTP_200_OK: {"model": ScoreResponse},
                 status.HTTP_404_NOT_FOUND: {"model": ScoreExceptionResponse},
                 status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ScoreExceptionResponse}})
async def score(data: ScoreRequest):
    """
    *Example:*

        curl -X 'POST' 'http://127.0.0.1:8000/score/' \
             -H 'accept: application/json' \
             -H 'Content-Type: application/json' \
             -d '{"repo":"python/cpython"}'
    """
    # @note: This may be raise ServiceException that handled globally
    g = GitHubAPI(token=GITHUB_ACCESS_TOKEN)
    try:
        repo = g.get_repo(data.repo)
    except AppException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.message)
    else:
        return ScoreResponse(repo=repo.full_name,
                             score=repo.score)
