import requests
from datetime import datetime
import os


GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")


APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")


# Sheety auth bearer token
AUTH = "Bearer " + os.environ.get("AUTH")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/dcd85ae2f35c4818920ee73e8d841707/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(url=exercise_endpoint,
                         json=user_params, headers=headers)
result = response.json()


today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")


sheety_header = {
    "Authorization": AUTH,
}




for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_header)



    print(sheet_response.text)