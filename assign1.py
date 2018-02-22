import requests

zipcode = raw_input("Enter zipcode: ")
wreck = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+ zipcode +',ph&appid=bde1f034d73c7075313509c3b3549cde')
obj = wreck.json()

temper = float(obj['main'] ['temp'])
celcius = temper - 273.15

name =  obj['name']


print "\n\nLocation: " + name
print "\nCurrent temperature: " + str(celcius) + "degree Celcius"

press = float(obj['main'] ['pressure'])
print "\nPressure: " + str(press)

humid = float(obj['main'] ['humidity'])
print "\nHumidity: " + str(humid)

