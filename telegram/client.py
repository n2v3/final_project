import os
import requests


def send_message(text, chat_id=None):
    token = os.environ.get("TELEGRAM_API_TOKEN")
    default_chat_id = "427396286"

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    response = requests.post(
        url, json={"chat_id": chat_id or default_chat_id, "text": text}
    )

    print(response.status_code)
    print(response.json())
