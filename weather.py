import requests as r
api_key='71434fd24fd953e1ce5dedc27c9fbb5f'
user_h=input("Enter the city name: ")


weather_data=r.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_h}&units=imperial&APPID={api_key}")

data=weather_data.json()
if data['cod']=="404":
    print("No city found")
else:
    weather=data['weather'][0]['main']
    temp=data['main']['temp']
    print(f'The weather in {user_h} is: {weather}')
    print(f"The temperature of {user_h} is {temp}")
