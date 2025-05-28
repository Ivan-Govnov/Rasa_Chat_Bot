from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city") or "Москва"  # По умолчанию Москва
        api_key = "7a4443cf1174bbbd8262b389c0e57fda"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

        try:
            response = requests.get(url).json()
            if response["cod"] == 200:
                temp = round(response["main"]["temp"])
                desc = response["weather"][0]["description"].capitalize()
                dispatcher.utter_message(text=f"🌤 В {city} сейчас {temp}°C, {desc}.")
            else:
                dispatcher.utter_message(text=f"⚠ Город '{city}' не найден.")
        except:
            dispatcher.utter_message(text="⚠ Не удалось получить погоду.")
        return []