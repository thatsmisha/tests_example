import requests

# -------------------- bot ------------------------


def send_telegram(text):
    token = "5156727216:AAFZ12cHkXOF4uinyc5amQ0-BhM8a1OItLc"
    url = "https://api.telegram.org/bot"
    channel_id = "@tests_example"
    url += token
    method = url + "/sendMessage"

    try:  # because Telegram can be unavailable
        r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
        })
    except:
        pass