import requests


class SpotifyRequest:
    def __init__(self, access_token):
        self._access_token = access_token
        self._base_url = 'https://api.spotify.com/v1/'
        self._headers = {
            'Authorization': f'Bearer {access_token}'
        }

    @property
    def access_token(self):
        return self._access_token

    @property
    def base_url(self):
        return self._base_url

    @property
    def headers(self):
        return self._headers

    def get_band_id(self, band_name):
        url = f'{self.base_url}search'
        params = {
            'q': band_name,
            'type': 'artist'
        }
        req = requests.get(url, headers=self.headers, params=params)
        data = req.json()
        try:
            return data['artists']['items'][0]['id']
        except IndexError:
            return None
        except KeyError:
            return None



    def get_albums(self, artist_id):
        url = f'{self.base_url}artists/{artist_id}/albums'
        params = {
            'market': 'AR',
            'album_type': 'album',
            # 'limit': 5
        }
        req = requests.get(url, headers=self.headers, params=params)
        data = req.json()
        try:
            return data['items']
        except IndexError:
            return None
        except KeyError:
            return None


    def get_reduce_albums(self,albums):
        if albums is None:
            return None
        return [{"name": albums[i]['name'], "released": albums[i]['release_date'], "tracks": albums[i]['total_tracks'], "cover": albums[i]['images'][0]} for i in range(len(albums))] 
