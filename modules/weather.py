"""
Api response Example
{
	"coord":{
		"lon":78.17,
		"lat":29.97
	},
	"weather":[{
		"id":801,
		"main":"Clouds",
		"description":"few clouds",
		"icon":"02n"}],
	"base":"stations",
	"main":{
		"temp":290.732,
		"pressure":973.6,
		"humidity":83,
		"temp_min":290.732,
		"temp_max":290.732,
		"sea_level":1021.89,
		"grnd_level":973.6},
	"wind":{
		"speed":1.21,
		"deg":26.0014},
	"clouds":{
		"all":20},
	"dt":1522784086,
	"sys":{
		"message":0.0066,
		"country":"IN",
		"sunrise":1522715629,
		"sunset":1522760848},
	"id":1270351,
	"name":"Haridwar",
	"cod":200}




"""

import pytemperature
from urllib.request import urlopen
import json


class Weather():
    
    intentList=['WEATHER','TEMPERATURE','HUMIDITY']
            
    
    def getIntentsFromCommand(self, command):
        matchedIntents=[]
        for word in command.split():
            if word in self.intentList:
                matchedIntents.append(word)
        return matchedIntents
    
    def intentController(self,fullCommand):
        responseToController=''
        matchedIntents=self.getIntentsFromCommand(fullCommand)
        if matchedIntents is not None:
            self.fetchWeatherDetails()
            if 'TEMPERATURE' in matchedIntents:
                responseToController+=self.intentTemperature()
            if 'HUMIDITY' in matchedIntents:
                responseToController+=' '+self.intentHumidity()
            
        return responseToController                
    
    
    def fetchWeatherDetails(self):
        cityName = 'Pune'
        key = 'd22e1d48159252b0e6d7fc45b592def6'   # api key
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&APPID=' + key
        response = urlopen(url).read().decode('utf-8')
        obj = json.loads(response)
        self._cityCoordinates = obj['coord']
        self._weather=obj['weather']
        self._mainFeatures=obj['main']
        self._wind=obj['wind']
        self._sunDetails=obj['sys']
        
    def intentTemperature(self):
        return 'Today\'s temperature is '+str(pytemperature.k2c(self._mainFeatures['temp']))+' degrees celsius.'
    
    def intentHumidity(self):
        return 'Today\'s humidity is '+str(self._mainFeatures['humidity'])+' percentage.'
        
        
"""
Test by uncommenting
"""
if __name__=="__main__":
    weather=Weather()
    print(weather.intentController('WHAT IS HUMIDITY and TEMPERATURE'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        