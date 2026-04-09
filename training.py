import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("solar_weather_dataset.csv")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Features
df['hour'] = df['timestamp'].dt.hour
df['sin_hour'] = np.sin(2 * np.pi * df['hour'] / 24)
df['cos_hour'] = np.cos(2 * np.pi * df['hour'] / 24)

df['day_of_week'] = df['timestamp'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5,6]).astype(int)


X = df[['temperature','humidity','cloud_cover','wind_speed','precipitation','sin_hour','cos_hour','is_weekend']]
y = df['solar_output']

# Train/Test split 
split = int(len(df) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

# Save model
joblib.dump(model, "model.pkl")

print("MODEL TRAINED")