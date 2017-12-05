import Observer, ForecastDisplay

class CurrentConditionsDisplay(Observer, ForecastDisplay):
    def __init__(self, weather_data):
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + str(self._temperature) +
              "F degrees and " + str(self._humidity) + " % humidity");
