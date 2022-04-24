import tekore as tk

def authorize():
    CLIENT_ID = "d53bb49cc6c04be3bf5456cffb0443ea"
    CLIENT_SECRET = "529efb264fc54566893c3ee6675bbecc"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)