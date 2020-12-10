import requests
import os
from datetime import datetime

my_api = os.environ["API_KEY"]
my_id = os.environ["APP_ID"]
my_user = os.environ["MY_USER"]
my_pass = os.environ["MY_PASS"]



MY_GENDER = "male"
MY_AGE = 31
MY_HEIGHT = 198
MY_WEIGHT = 102

exercise_query = input("What exercise did you do today?")

headers = {
    "x-app-id": my_id,
    "x-app-key": my_api
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": exercise_query,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}


exercise_info = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = exercise_info.json()

sheety_endpoint = "https://api.sheety.co/992494e7999047088aa9bc2e49e2bf25/myWorkouts100DaysofCode/workouts"
sheety_headers = (my_user, my_pass)
date = datetime.now()

for exercise in range(len(result["exercises"])):
    sheety_params = {
        "workout": {
            "date": f"{date.strftime('%d')}/{date.strftime('%m')}/{date.strftime('%Y')}",
            "time": date.strftime("%X"),
            "exercise": result["exercises"][exercise]["name"].title(),
            "duration": result["exercises"][exercise]["duration_min"],
            "calories": result["exercises"][exercise]["nf_calories"]
        }
    }
    requests.post(url=sheety_endpoint, json=sheety_params, auth=sheety_headers)

