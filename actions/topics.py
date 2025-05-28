from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import spacy

nlp = spacy.load("ru_core_news_lg")

class ActionDetectTopics(Action):
    def name(self) -> Text:
        return "action_detect_topics"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        text = tracker.latest_message.get("text")
        doc = nlp(text)

        topics_config = {
            'игры': ['игра', 'гейм', 'steam', 'игровой'],
            'музыка': ['музыка', 'песн', 'альбом', 'концерт'],
            'математика': ['математ', 'алгебр', 'геометр', 'уравнен']
        }

        detected = []
        for token in doc:
            lemma = token.lemma_.lower()
            for topic, keywords in topics_config.items():
                if any(kw in lemma for kw in keywords):
                    detected.append(topic)

        if detected:
            unique_topics = list(set(detected))
            dispatcher.utter_message(text=f"🎮 Темы: {', '.join(unique_topics)}")
            return [SlotSet("current_topic", unique_topics[0])]
        return []