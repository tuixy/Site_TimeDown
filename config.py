import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/uploads')
SECRET_KEY = 'your_secret_key'
SESSION_TYPE = 'filesystem'
