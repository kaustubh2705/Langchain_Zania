from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    def __init__(self, token, channel):
        self.client = WebClient(token=token)
        self.channel = channel

    def post_results(self, answers):
        message = "Here are the answers to your questions:\n"
        for question, answer in answers.items():
            message += f"*{question}*\n{answer}\n\n"
        try:
            self.client.chat_postMessage(channel=self.channel, text=message)
        except SlackApiError as e:
            print(f"Error posting to Slack: {e.response['error']}")
