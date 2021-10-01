Intro
=====

This is a Github Score Application to rank repositories based on forks and starts.


Stack
=====

In this application we used:

* Python
* FastAPI



Install requirements
====================

```bash

$ pip install -r requirements.txt

```

Environments
============

```bash

$ export GITHUB_ACCESS_TOKEN="YOUR_GITHUB_ACCESS_TOKEN"

```

Run server
==========

```bash

$ uvicorn main:app

```

Run tests
=========

```bash

$ pytest

```

Browse
======

    http://127.0.0.1:8000/docs

    http://127.0.0.1:8000/score/


Curl
====

```bash

$ curl -X 'POST' 'http://127.0.0.1:8000/score/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"repo":"python/cpython"}

```

TODO
====

    Cache external service API response for some short period of time for example for 1 hour in the Redis,
    And maybe provide a new cache option for example `Cache-Control: no-cache` header to the `score` API


Useful links
============


* https://fastapi.tiangolo.com/tutorial/metadata/
* https://levelup.gitconnected.com/deploying-an-asynchronous-fastapi-on-nginx-unit-b038288bec5
* https://dev.to/shuv1824/deploy-fastapi-application-on-ubuntu-with-nginx-gunicorn-and-uvicorn-3mbl
* https://medium.com/analytics-vidhya/how-to-deploy-a-python-api-with-fastapi-with-nginx-and-docker-1328cbf41bc
* https://stackoverflow.com/questions/67435296/how-to-access-fastapi-swaggerui-docs-behind-an-nginx-proxy
* https://fastapi.tiangolo.com/advanced/behind-a-proxy/
* https://www.reddit.com/r/flask/comments/j2289k/anyone_using_fastapi_in_production/
* https://stackoverflow.com/questions/62976648/architecture-flask-vs-fastapi/62977786#62977786
* https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
* https://fastapi.tiangolo.com/deployment/manually/
* https://unit.nginx.orga
* https://www.uvicorn.org/#running-with-gunicorn
* https://github.com/encode/uvicorn
* https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-with-fastapi-docker-and-github-actions-13374cbd638a
* https://fastapi.tiangolo.com/tutorial/first-steps/
* https://unit.nginx.org/
* https://fastapi.tiangolo.com/advanced/behind-a-proxy/
* https://fastapi.tiangolo.com/deployment/manually/
* https://www.uvicorn.org/#running-with-gunicorn
* https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
* https://stackoverflow.com/a/63427961
* https://stackoverflow.com/a/66426744
* https://levelup.gitconnected.com/deploying-an-asynchronous-fastapi-on-nginx-unit-b038288bec5
* https://dev.to/shuv1824/deploy-fastapi-application-on-ubuntu-with-nginx-gunicorn-and-uvicorn-3mbl
* https://github.com/tiangolo/fastapi/issues/1034#issuecomment-591651300
* https://fastapi.tiangolo.com/tutorial/body/
* https://fastapi.tiangolo.com/tutorial/handling-errors/
* https://gist.github.com/omidraha/72817ed0c6173f6c47613e3eebf03ad7
