"""
write a program that prints 
a joke everytime you run it
"""
import requests #install requests library (pip install requests)

data = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "text/plain"})
print(data.text)
