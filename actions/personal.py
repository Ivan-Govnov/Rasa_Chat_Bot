from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import logging
import spacy

nlp = spacy.load("ru_core_news_lg")
logger = logging.getLogger(__name__)


class ActionStoreName(Action):
    def name(self) -> Text:
        return "action_store_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> list:
        message = tracker.latest_message.get("text")
        doc = nlp(message)
        persons = [ent.text for ent in doc.ents if ent.label_ == "PER"]
        if persons:
            name = persons[0]
            dispatcher.utter_message(text=f"👋 Приветствую, {name}!")
            return [SlotSet("user_name", name)]
        return []