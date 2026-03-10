import requests

def get_temperature(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data['hourly_units']['temperature_2m']

# call it in the same cell to test
print(get_temperature(48.35, 2.35))
import matplotlib as plt

import pandas as pd
s=pd.Series([10,30,20,45,84,551,71,22,55,44,45])
s.name="scores"
print(scores)
s.std()
s.describe()

import sqlite3 
conn=sqlite3.connect("dvdrental.db")
df=pd.read_sql("SELECT*FROM dvdrental",conn)