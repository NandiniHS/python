import requests

city = input("Enter the city name : ")
key = '5ca5d7031bbd1c1ce965c17eb32f06a2'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()
    print('Weather is ',data['weather'][0]['description'])