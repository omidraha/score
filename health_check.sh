#!/usr/bin/env bash
curl  --fail -s -X 'POST' 'http://127.0.0.1/score/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"repo":"python/cpython"}' || exit 1
