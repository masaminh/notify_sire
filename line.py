"""LINEへのアクセス関数群."""
import requests


def notify(token: str, message: str) -> None:
    """LINE Notifyでメッセージを送る."""
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + token}
    requests.post('https://notify-api.line.me/api/notify',
                  data=payload, headers=headers)
