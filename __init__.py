from pynicotine.pluginsystem import BasePlugin
import requests

class Plugin(BasePlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = {
            "webhook": ""
        }
        self.metasettings = {
            "webhook": {
                "description": "Discord webhook URL to send upload/download notifications to",
                "type": "string"
            }
        }

    def post_webhook(self, username, content):
        result = requests.post(self.settings["webhook"], { "content": content, "username": username })
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            self.log(f"Error sending webhook message: {err}")


    def upload_started_notification(self, user, virtual_path, real_path):
        self.post_webhook(user, f"Downloading ``{real_path}``")