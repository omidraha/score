FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9 as build

COPY . /app

RUN pip3 install -r requirements.txt

