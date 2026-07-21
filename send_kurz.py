import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://api.frankfurter.app/latest?from=EUR&to=CZK"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    kurz = data["rates"]["CZK"]

    text = f"""💶 Aktuální kurz EUR

1 EUR = {kurz} CZK
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text
        }
    )
else:
    print("Nepodařilo se načíst kurz.")
