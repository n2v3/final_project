import os
import requests
from dotenv import load_dotenv

load_dotenv()


def telegram_set_webhook():
    token = os.environ.get("TELEGRAM_API_TOKEN")
    url = "https://3f39-91-214-85-107.ngrok-free.app/telegram/"

    resp = requests.post(
        f"https://api.telegram.org/bot{token}/setWebhook", json={"url": url}
    )

    print(resp.json())


if __name__ == "__main__":
    telegram_set_webhook()
