import requests


class SpotifyRequest:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://api.spotify.com/v1/'
        self.headers = {
            'Authorization': f'Bearer {access_token}'
        }

    def get_band_id(self, band_name):
        url = f'{self.base_url}search'
        params = {
            'q': band_name,
            'type': 'artist'
        }
        req = requests.get(url, headers=self.headers, params=params)
        data = req.json()
        return data['artists']['items'][0]['id']



    def get_albums(self, artist_id):
        url = f'{self.base_url}artists/{artist_id}/albums'
        params = {
            'market': 'AR',
            'album_type': 'album',
            # 'limit': 5
        }
        req = requests.get(url, headers=self.headers, params=params)
        data = req.json()
        return data['items']


    def get_reduce_albums(self,albums):
        return [{"name": albums[i]['name'], "released": albums[i]['release_date'], "tracks": albums[i]['total_tracks'], "cover": albums[i]['images'][0]} for i in range(len(albums))] 
