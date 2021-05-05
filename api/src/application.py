from fastapi import FastAPI
from src.transaction import transaction
from src.routes.oauth2 import oauth

app = FastAPI()
app.mount('/oauth', oauth)

@app.on_event('startup')
async def startup():
    transaction.start()


@app.get('/')
async def index():
    return {'message': 'Hello World', 'status': 'success'}
