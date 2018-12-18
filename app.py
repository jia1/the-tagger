from flask import Flask
from telethon import TelegramClient, events, sync
import os

app = Flask(__name__)
api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']
group = os.environ['GROUP']

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/pingu')
def pingu():
    client = TelegramClient('session_name', api_id, api_hash).start()
    with client:
        usernames = client.get_participants(group)
        print(usernames)

