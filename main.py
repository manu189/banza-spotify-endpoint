# from pickle import TRUE
from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
import uvicorn
import requests
# import json
import base64
from secretscode import *
from spotifyrequest import SpotifyRequest
app = FastAPI()


client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

token_url = 'https://accounts.spotify.com/api/token'
method = 'POST'

token_date = {
    'grant_type': 'client_credentials'
}

token_headers = {
    'Authorization': f'Basic {client_creds_b64.decode()}'
}

req = requests.post(token_url, data=token_date, headers=token_headers)
token_response_data = req.json()

access_token = token_response_data['access_token']
expires_in = token_response_data['expires_in']
token_type = token_response_data['token_type']

spotify = SpotifyRequest(access_token)

@app.get("/")
async def root():
    html_content = """
    <html>
        <head>
            <title>Get Albums</title>
        </head>
        <body>
            <h1>Hello, go to /api/v1/albums?q="band-name" to get band albums</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/api/v1/albums")
def read_band(q: str = None):

    # return JSONResponse(content=jsonable_encoder(spotify.get_reduce_albums(spotify.get_albums(spotify.get_band_id(q)))))
    return spotify.get_reduce_albums(spotify.get_albums(spotify.get_band_id(q)))

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)