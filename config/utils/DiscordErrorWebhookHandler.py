import json
import logging
from django.utils import timezone

import requests


class DiscordErrorWebhookHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        log_entry = self.format(record)
        extra_info = getattr(record, 'extra', {})
        request_path = extra_info.get('request_path', 'N/A')
        timestamp = timezone.now().isoformat()

        payload = {
            "embeds": [
                {
                    "title": "Alert",
                    "description": f"```{log_entry}```\n\nAdditional Info:\nPath: {request_path}\nTimestamp: {timestamp}",
                    "color": 16711680
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
        }
        requests.post(url=self.webhook_url, headers=headers, data=json.dumps(payload))
