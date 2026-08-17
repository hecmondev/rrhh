from fastapi import FastAPI
from settings import Settings

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/settings')
def read_settings():
    settings = Settings()
    return settings
