import os
import aiohttp
from logging import getLogger
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from urllib.parse import quote
from src.transaction import transaction

oauth = FastAPI()
logger = getLogger(__name__)

@oauth.get('/login')
async def login():
    redirect_url = quote('{}/oauth/redirect'.format(os.environ['API_ENDPOINT_URL']))
    client_id = quote(os.environ['BOT_CLIENT_ID'])
    scope = quote(os.environ['OAUTH_SCOPES'])
    oauth_url = 'https://discord.com/api/oauth2/authorize?client_id={0}&redirect_uri={1}&response_type=code&scope={2}'.format(
        client_id, redirect_url, scope
    )
    return RedirectResponse(url=oauth_url, status_code=302)

@oauth.get('/redirect')
async def redirect(code: str, client: aiohttp.ClientSession = Depends(transaction)):
    body = {
        'client_id': os.environ['BOT_CLIENT_ID'],
        'client_secret': os.environ['BOT_CLIENT_SECRET'],
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': '{}/oauth/redirect'.format(os.environ['API_ENDPOINT_URL'])
    }
    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    resp = await client.post(
        '{}/oauth2/token'.format(os.environ['DISCORD_API_ENDPOINT']), data=body, headers=header
    )
    data = await resp.json()
    if resp.status == 200:
        return data
    else:
        logger.error(data)
        return {'message': 'Failed to authorize', 'status': resp.status}
