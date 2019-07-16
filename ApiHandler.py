import requests


class ApiHandler:
    def __init__(self, city):
        self.city = city
        self.url1 = "http://api.openweathermap.org/data/2.5/weather?q="
        self.url2 = "&appid=d55e4671a5b45e80f03b70a550d7bcde"
        self.url = self.url1 + self.city + self.url2


    def request(self):
        self.json_data = requests.get(self.url).json()
        #print(self.json_data)
        self.temp = self.json_data['main']['temp']
        self.tempMin = self.json_data['main']['temp_min']
        self.tempMax = self.json_data['main']['temp_max']
        self.weatherDescription = self.json_data['weather'][0]['description']




