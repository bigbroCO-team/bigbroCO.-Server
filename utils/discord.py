import json
import logging
import requests


class DiscordWebhookHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        print("start")
        log_entry = self.format(record)
        payload = {
            "embeds": [
                {
                    "title": "alert",
                    "description": log_entry,
                    "color": 16711680
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post(url=self.webhook_url, headers=headers, data=json.dumps(payload))

        print(r.status_code, r.text)
