from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionSearch(Action):
    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        query = tracker.latest_message.get("text").replace("найди", "").strip()
        if query:
            webbrowser.open(f"https://google.com/search?q={query}")
            dispatcher.utter_message(text=f"🌐 Ищу: '{query}'")
        else:
            dispatcher.utter_message(text="Укажите запрос, например: 'найди котиков'.")
        return []