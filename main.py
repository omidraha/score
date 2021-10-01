from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
# noinspection PyPackageRequirements
from starlette.exceptions import HTTPException as StarletteHTTPException

import apps.score.view
from utility.exception import ServiceException

description = """
## Description
Github Score Application to rank repositories. 🚀
## Available APIs
The following is an list of available APIs. 
"""

tags_metadata = [
    apps.score.view.TAG_SCORE
]

app = FastAPI(
    title="Github Score App",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
)


# Define ServiceException as global exception handler
@app.exception_handler(ServiceException)
async def service_exception_handler(request: Request, exc: ServiceException):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"message": exc.message, },
    )


# Customize default HTTPException
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, },
    )


app.include_router(apps.score.view.router)
