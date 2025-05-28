from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re

class ActionCalculate(Action):
    def name(self) -> Text:
        return "action_calculate"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        text = tracker.latest_message.get("text")
        match = re.search(r"(\d+)\s*([-+*/])\s*(\d+)", text)
        if match:
            num1, op, num2 = match.groups()
            operations = {'+': float(num1) + float(num2), '-': float(num1) - float(num2),
                          '*': float(num1) * float(num2), '/': float(num1) / float(num2) if num2 != '0' else "ошибка"}
            result = operations.get(op, "ошибка")
            dispatcher.utter_message(text=f"🔢 {num1} {op} {num2} = {result}")
        return []