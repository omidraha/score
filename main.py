from fastapi import FastAPI

description = """
## Description
Github Score Application to rank repositories. 🚀
## Available APIs
The following is a list of available APIs. 
"""

tags_metadata = [
    {
        "name": "score",
        "description": "The main API to score",
    },
]

app = FastAPI(
    title="Github Score App",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)


@app.get("/score/", tags=["score"])
async def score():
    """
    *Example:*

        curl -X 'GET' 'http://127.0.0.1:8000/score/' -H 'accept: application/json'
    """
    # @todo: Implement real score API
    return {"score": 100}


