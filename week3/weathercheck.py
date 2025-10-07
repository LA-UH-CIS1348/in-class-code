"""
write a program that gets the current temperature from open-meteo (for houston) in celcius
and converts it into fahrenheit  and prints it
"""
import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=29.7602&longitude=-95.3633&current_weather=true", timeout=2)
data = response.json()
c = data["current_weather"]["temperature"]
# c = (f-32)*5/9
# 9*c = (f-32)*5
# 9*c/5 = f-32
# 9*c/5+32=f
#f = 32+c*9/5
f = 32+c*9/5
print(f)