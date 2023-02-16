from fastapi import FastAPI

from metar_reader_python.endpoints.v1 import metar

APP_ENDPOINTS = [
    metar.endpoint
]

app = FastAPI(
    title="Metar Reader"
)

for endpoint in APP_ENDPOINTS:
    app.include_router(endpoint.router, prefix=endpoint.prefix)

