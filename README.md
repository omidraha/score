Intro
=====

This is a GitHub Score Application to rank repositories based on forks and starts.

More info (Issues):

* https://github.com/omidraha/score/issues

Stack
=====

In this application we used:

* Python 3.9.7
* FastAPI 0.68.1
* Docker 20.10.8
* Docker-compose 1.29.2
* Docker-compose file version: 3.1
* Gunicorn 20.1.0
* uvicorn 0.15.0

Images
======

* tiangolo/uvicorn-gunicorn-fastapi:python3.9

More info:

* https://fastapi.tiangolo.com/deployment/docker/#official-docker-image-with-gunicorn-uvicorn

Backend topology
=================

```
gunicorn -> gunicorn worker -> uvicorn -> main.py
```

More info:

* https://www.uvicorn.org/deployment/#gunicorn
* https://www.uvicorn.org/#running-with-gunicorn


Environments
============

Before run the app or run their tests, copy `example.env` as new `.env` file: 

```
$ cp example.env .env
```

Set the value of `GITHUB_ACCESS_TOKEN` to your valid GITHUB access token.

Run application
===============

Set `Environments` as previous section and then run the application:

```
$ docker-compose -p score build
$ docker-compose -p score up
```

For run in daemon, use `-d` if it's required:

```
$ docker-compose -p score up -d
```


Run tests
=========

Set `Environments` as previous section and then:

```
$ docker-compose -p test run --rm web pytest
```


Health check
============

To see health check of service, use this command:

```
$ docker-compose -p score ps
```

Sample output:

```
score_web_1   /start.sh   Up (healthy)   0.0.0.0:80->80/tcp,:::80->80/tcp
```

To see logs of health check:

```
docker inspect --format='{{json .State.Health}}' score_web_1
```


Browse
======

    http://127.0.0.1/docs/

    http://127.0.0.1/score/


Curl
====

```
$ curl -X 'POST' 'http://127.0.0.1/score/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"repo":"python/cpython"}'
```

TODO
====

* Cache external `GitHub` service API response for some short period of the time for example for 1 hour in the Redis,
    And maybe provide a new cache option for example `Cache-Control: no-cache` header to the `score` API

* Use async library for communicate with `Github` service API 


Extra useful links
==================


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
* https://fastapi.tiangolo.com/deployment/docker/
* https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
