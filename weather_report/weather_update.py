from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import requests
from utils import city_details, weather_data

city_result = city_details("delhi", 28.7, 77.1)
weather_date = weather_data(7, 0)


def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={city_result[1]}"
        f"&longitude={city_result[2]}"
        "&daily=temperature_2m_max,temperature_2m_min"
        f"&start_date={weather_date[0]}"
        f"&end_date={weather_date[1]}"
        "&timezone=Asia%2FKolkata"
    )

    # MAKING REQUEST FROM API
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    max_temp = data["daily"]["temperature_2m_max"]
    min_temp = data["daily"]["temperature_2m_min"]

    dates = data["daily"]["time"]
    city_name = city_result[0]

    return city_name, dates, max_temp, min_temp


dataset = get_weather()


# CONVERTING DATA TO DATAFRAME USING PANDA

df = pd.DataFrame(
    {
        "city": dataset[0],
        "Date": dataset[1],
        "max_temp": dataset[2],
        "min_temp": dataset[3],
    }
)

print(df)


# PLOTTING DATA INTO A GRAPH

df.plot(x="Date", y=["max_temp", "min_temp"], kind="line", marker="o")

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature")
plt.xticks(rotation=45)
plt.tight_layout()


filename = f"temperature_graph_{datetime.now().astimezone():%Y%m%d_%H%M%S}.png"
# filename = f"temperature_graph_{datetime.now():%Y%m%d_%H%M%S}.png"  # will save graph according to dates
plt.savefig(filename)
plt.show()
