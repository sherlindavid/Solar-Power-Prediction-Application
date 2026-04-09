import pandas as pd
import numpy as np
from datetime import datetime, timedelta

rows = []
start = datetime(2024, 1, 1)

for i in range(24 * 10):
    ts = start + timedelta(hours=i)
    hour = ts.hour

    temperature = 20
    humidity = 60
    cloud_cover = 30
    wind_speed = 5
    precipitation = 0

    solar_output = max(0, (hour - 6) * 50 if 6 <= hour <= 18 else 0)

    rows.append([ts, temperature, humidity, cloud_cover, wind_speed, precipitation, solar_output])

df = pd.DataFrame(rows, columns=[ "timestamp", "temperature", "humidity", "cloud_cover", "wind_speed", "precipitation", "solar_output"])

df.to_csv("solar_weather_dataset.csv", index=False)

print("DONE")