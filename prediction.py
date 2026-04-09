import pandas as pd
import numpy as np
import joblib
import requests
import matplotlib.pyplot as plt

# STEP 1: Function to get weather

def get_weather():
    API_KEY = "6597b7604cc5796a38dabf5a26a22830"  

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat=18.52&lon=73.86&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return None

    data = response.json()

    rows = []

    for item in data['list'][:8]:
        rows.append({
            "timestamp": pd.to_datetime(item['dt'], unit='s'),
            "temperature": item['main']['temp'],
            "humidity": item['main']['humidity'],
            "cloud_cover": item['clouds']['all'],
            "wind_speed": item['wind']['speed'],
            "precipitation": item.get('rain', {}).get('3h', 0)
        })

    df = pd.DataFrame(rows)
    return df

# STEP 2: Load model

model = joblib.load("model.pkl")

# STEP 3: Get weather data

df = get_weather()

if df is None:
    exit()


# STEP 4: Feature engineering

df['hour'] = df['timestamp'].dt.hour
df['sin_hour'] = np.sin(2 * np.pi * df['hour'] / 24)
df['cos_hour'] = np.cos(2 * np.pi * df['hour'] / 24)
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5,6]).astype(int)


# STEP 5: Prepare input

X = df[['temperature','humidity','cloud_cover','wind_speed','precipitation','sin_hour','cos_hour','is_weekend']]


# STEP 6: Predict

preds = model.predict(X)
preds = np.clip(preds, 0, None)

df['predicted_solar'] = preds


# STEP 7: Output

print("\nFuture Solar Predictions:\n")
print(df[['timestamp','predicted_solar']])



# STEP 8: Graph

# Load historical data
history = pd.read_csv("solar_weather_dataset.csv")
history['timestamp'] = pd.to_datetime(history['timestamp'])

plt.figure(figsize=(10,5))

# Historical
plt.plot(history['timestamp'][-50:], history['solar_output'][-50:], label="Historical")

# Predicted
plt.plot(df['timestamp'], df['predicted_solar'], marker='o', label="Predicted")

plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Solar Output")
plt.title("Solar Prediction (Historical + Future)")
plt.legend()
plt.tight_layout()
plt.show()