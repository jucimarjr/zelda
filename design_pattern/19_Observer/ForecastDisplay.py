import Observer, DisplayElement

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._current_pressure = 29.92
        self._last_pressure = 0.0
        self._weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temp, humidity, pressure):
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: "),
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather")
