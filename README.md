# banza-spotify-endpoint


Endpoint to get a json response with all albums from a band search, based on Spotify API.


## Deployed at https://banza-spotify-endpoint.herokuapp.com/

To search for a band album list just go to https://banza-spotify-endpoint.herokuapp.com/api/v1/albums?q=band-name

Example : https://banza-spotify-endpoint.herokuapp.com/api/v1/albums?q=Soda%20Stereo

## Local deployment instructions

#### 1) Clone this repository

https://github.com/manu189/banza-spotify-endpoint.git


#### 2) Install requirements

In the cloned directory run: pip install -r requirements.txt

#### 3) Run app

run: uvicorn main:app

#### Optional

Create a Python enviroment

