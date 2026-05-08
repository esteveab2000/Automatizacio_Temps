import requests
import json
import os
from datetime import datetime

#BARCELUNIA
LAT = 41.3888
LON = 2.159

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    f"&hourly=temperature_2m"
    f"&forecast_days=1"
)

response = requests.get(url)
data = response.json()

temperatures = data["hourly"]["temperature_2m"]

temp_max = max(temperatures)
temp_min = min(temperatures)
temp_avg = round(sum(temperatures) / len(temperatures), 2)

resultat = {
    "data": datetime.now().strftime("%Y-%m-%d"),
    "temperatura_maxima": temp_max,
    "temperatura_minima": temp_min,
    "temperatura_mitjana": temp_avg
}

os.makedirs("dades", exist_ok=True)

nom_fitxer = f"dades/temp_{datetime.now().strftime('%Y%m%d')}.json"

with open(nom_fitxer, "w", encoding="utf-8") as f:
    json.dump(resultat, f, indent=4, ensure_ascii=False)

print(f"Fitxer creat: {nom_fitxer}")
