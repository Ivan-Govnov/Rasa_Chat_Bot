from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from textblob import TextBlob
import spacy

nlp = spacy.load("ru_core_news_lg")


class ActionHandleComplexMessage(Action):
    def name(self) -> Text:
        return "action_handle_complex_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Использование сохраненного имени
        user_name = tracker.get_slot("user_name")
        if user_name:
            dispatcher.utter_message(text=f"👋 Приветствую, {user_name}!")

        # Улучшенный анализ настроения
        message = tracker.latest_message.get("text")
        doc = nlp(message)

        # Проверка ключевых слов
        mood_keywords = {
            'positive': ['рад', 'счастлив', 'весело', 'хорошо'],
            'negative': ['грустно', 'плохо', 'ужасно', 'печально']
        }

        detected_mood = None
        for token in doc:
            lemma = token.lemma_.lower()
            for mood, keywords in mood_keywords.items():
                if lemma in keywords:
                    detected_mood = mood
                    break

        # Отправка соответствующего ответа
        if detected_mood == 'positive':
            dispatcher.utter_message(text="😊 Рад, что вам весело!")
        elif detected_mood == 'negative':
            dispatcher.utter_message(text="😔 Мне жаль это слышать...")
        else:
            blob = TextBlob(message)
            polarity = blob.sentiment.polarity
            if polarity > 0.3:
                dispatcher.utter_message(text="😀 Похоже, у вас хорошее настроение!")
            elif polarity < -0.3:
                dispatcher.utter_message(text="😟 Очень жаль, что вам грустно")

        return []