from Subject import *
from CurrentConditionsDisplay import *
from WeatherData import *
from ForecastDisplay import *
from Observer import *
from StatisticsDisplay import *

if __name__ == '__main__':
    # WeatherStation code
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.setMeasurements(80, 65, 30.4)
    weather_data.setMeasurements(82, 70, 29.2)
    weather_data.setMeasurements(78, 90, 29.2)