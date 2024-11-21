from fastapi import FastAPI
from router import router as router_pages

app = FastAPI()
app.include_router(router_pages)