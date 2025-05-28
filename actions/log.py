from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime


class ActionLogConversation(Action):
    def name(self) -> Text:
        return "action_log"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        user_input = tracker.latest_message.get("text")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("chat_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{timestamp} - User: {user_input}\n")

        return []