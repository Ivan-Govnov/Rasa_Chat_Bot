from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime

class ActionGetTime(Action):
    def name(self) -> Text:
        return "action_get_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        now = datetime.now()
        dispatcher.utter_message(text=f"🕒 {now.strftime('%H:%M')}, {now.strftime('%d.%m.%Y')}")
        return []