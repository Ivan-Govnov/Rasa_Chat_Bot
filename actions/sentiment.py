from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import spacy

nlp = spacy.load("ru_core_news_lg")

class ActionAnalyzeSentiment(Action):
    def name(self) -> Text:
        return "action_analyze_sentiment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        message = tracker.latest_message.get("text")
        doc = nlp(message)

        positive_words = {'хороший', 'радостный', 'веселый', 'отличный', 'прекрасный'}
        negative_words = {'плохой', 'грустный', 'ужасный', 'печальный', 'плохо'}

        sentiment = "neutral"
        for token in doc:
            lemma = token.lemma_.lower()
            if lemma in positive_words:
                sentiment = "positive"
                break
            elif lemma in negative_words:
                sentiment = "negative"
                break

        if sentiment == "positive":
            dispatcher.utter_message(text="😊 Отличное настроение!")
        elif sentiment == "negative":
            dispatcher.utter_message(text="😔 Мне жаль это слышать... Хотите анекдот или поддержку?")
            dispatcher.utter_message(text="Напишите 'анекдот' или 'поговорить'.")
        else:
            dispatcher.utter_message(text="🤔 Расскажите подробнее, что вас интересует?")

        return [SlotSet("mood", sentiment)]