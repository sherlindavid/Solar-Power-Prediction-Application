#  Solar Power Prediction Project

##  Project Overview
This project predicts future solar power generation using weather data and machine learning.

It takes weather inputs like temperature, humidity, cloud cover, and time of day, and predicts how much solar energy will be generated in the next 24 hours.



##  Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)
- Matplotlib
- OpenWeatherMap API



##  Setup Instructions

### 1. Install dependencies
pip install -r requirements.txt

### 2. Create dataset
python create_data.py

### 3. Train model
python train.py

### 4. Set API Key
- Go to https://openweathermap.org
- Create a free account
- Generate API key
- Open `prediction.py`
- Replace:
API_KEY = "6597b7604cc5796a38dabf5a26a22830"

### 5. Run prediction
python prediction.py



##  Weather API Used

I used **OpenWeatherMap API (free version)** to get real-time weather forecast.

### How I got the API key:
1. Signed up on the OpenWeatherMap website  
2. Generated API key from dashboard  
3. Used forecast API to fetch next 24-hour weather data  



##  How the Project Works

1. Created a dataset with weather and solar values  
2. Trained a Random Forest model  
3. Fetched real-time weather data using API  
4. Applied feature engineering (time-based features)  
5. Predicted solar output  
6. Displayed results in table and graph  



##  Design Decisions & Assumptions

### Design Decisions:
- Used RandomForestRegressor for better prediction accuracy  
- Used time-based split (80% train, 20% test)  
- Used sin and cos transformation for hour (day-night pattern)  
- Used API for real-time prediction  

### Assumptions:
- Dataset is synthetic  
- Solar output is zero at night  
- Solar depends mainly on time of day  
- Location is fixed (Pune)  



##  Model Performance

(From training output)

- MAE: 0.0
- RMSE: 0.0 
- R² Score: 1.0  



##  Visualization

The project generates a graph showing:
- Historical solar data (past values)
- Predicted solar data (future values)



##  Sample Output 

| Timestamp | Predicted Solar |
|----------|----------------|
| 00:00 | 0 |
| 03:00 | 0 |
| 06:00 | Low |
| 09:00 | Medium |
| 12:00 | High |
| 15:00 | Peak |
| 18:00 | Decreasing |
| 21:00 | 0 |



##  Output Explanation

- Solar output is 0 at night  
- Increases in morning  
- Peaks in afternoon  
- Decreases in evening  



##  Project Structure

Solar Project/
│
├── create_data.py
├── train.py
├── prediction.py
├── solar_weather_dataset.csv
├── model.pkl
├── README.md
├── requirements.txt



##  Conclusion

This project demonstrates how machine learning and real-time weather data can be combined to predict solar power generation.



