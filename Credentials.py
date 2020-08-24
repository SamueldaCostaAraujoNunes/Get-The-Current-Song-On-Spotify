import os
try:
    from myCredentials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
except ImportError("Declare seu CLIENT_ID e o CLEINT_SECRET abaixo!"):
    SPOTIPY_CLIENT_ID = ''
    SPOTIPY_CLIENT_SECRET = ''

class SetCreditentials:

    def __init__(self):
        self.CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
        self.REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
        os.environ['SPOTIPY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
        os.environ['SPOTIPY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
        os.environ['SPOTIPY_REDIRECT_URI'] = "http://localhost:8888"