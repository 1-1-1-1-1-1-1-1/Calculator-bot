# Simple tool to disconnect from Telegram manually


from typing import NoReturn

from telethon.sync import TelegramClient


default_session_name = 'null'


def disconnect(api_id, api_hash,
               session_name=default_session_name) -> NoReturn:
    try:
        TelegramClient(session_name, api_id, api_hash).log_out()
        print('Disconnected from Telegram')
    except ConnectionError:
        print('[Connection error raised: already disconnected from Telegram]')
