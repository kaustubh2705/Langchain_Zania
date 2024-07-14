import os

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.slack_token = os.getenv("SLACK_API_TOKEN")
        self.slack_channel = os.getenv("SLACK_CHANNEL")