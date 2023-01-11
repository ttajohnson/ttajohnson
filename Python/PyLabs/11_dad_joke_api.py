# LAB 11: DAD JOKE API
# Use the Dad Joke API to get a dad joke and display it to the user.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# >>>
import requests

response = requests.get(
    "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
)
response_data = response.json()

print(response_data["joke"])
