from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionTellJoke(Action):
    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        jokes = [
            "Почему React-разработчик не мог заснуть? Потому что он думал о пропсах и state!",
            "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!"
        ]
        dispatcher.utter_message(text=f"🎭 {random.choice(jokes)}")
        return []