from datetime import date, timedelta


def city_details(city_name: str, latitude, longitude):
    city = city_name
    lat = latitude
    lon = longitude

    return city, lat, lon


def weather_data(days_previous_to_today, days_ahead_of_today):
    start_date = date.today() - timedelta(days=days_previous_to_today)
    end_date = date.today() + timedelta(days=days_ahead_of_today)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    return start_date, end_date
