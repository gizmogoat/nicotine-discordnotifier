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
        if not self.settings["webhook"]: return # Do not attempt to do anything if no hook had been set
        
        result = requests.post(self.settings["webhook"], { "content": content, "username": username })
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            self.log(f"Error sending webhook message: {err}")


    def upload_started_notification(self, user, virtual_path, real_path):
        self.post_webhook(f"{user} - Nicotine+", f"Uploading ``{real_path}`` to {user}")

    def download_started_notification(self, user, virtual_path, real_path):
        self.post_webhook(f"{user} - Nicotine+", f"Downloading ``{real_path}`` from {user}")

    def server_connect_notification(self):
        self.post_webhook(f"Nicotine+", "**Connection dropped from Soulseek server**")

    def server_connect_notification(self):
        self.post_webhook(f"Nicotine+", "**Connection established to Soulseek server**")