import os

from utils.disconnector import disconnect as _disconnect


get = os.environ.get


ON_HEROKU = get('ON_HEROKU', False)


# === Load environment variables ==============================================


def load_env(name=""):
    if not ON_HEROKU:
        from dotenv import load_dotenv

        basedir = os.path.abspath(os.path.dirname(__file__))

        dotenv_path = os.path.join(basedir, name + '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path, encoding='utf-8', interpolate=True)


load_env()  # is optional


# === Environment variables ===================================================


TOKEN: str = get('TOKEN')


# === Other configurations ====================================================


from telethon.sync import TelegramClient


# Set bot configurations: session name, api_id and api_hash.
session_name = 'calculator-bot'
api_id = eval(get('API_ID'))
api_hash = get('API_HASH')

# Prevent the situation when another client was already connected.
# **Caution**: Doing this action will end the previous client session.
_disconnect(api_id, api_hash)

bot = TelegramClient(
    session_name, api_id, api_hash
).start(bot_token=TOKEN)

# Now it is connected, get some data.
bot_data = bot.get_me()
BOT_ID: int = bot_data.id
BOT_USERNAME: str = bot_data.username
