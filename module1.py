import requests
import json
from datetime import datetime, timedelta
import statistics


api_key = "05acc5119f8ef9b2b1c90d3b4e1580cd" 
#FETCHING THE WEATHER FROM THE API
def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

      #MAKE THE API REQUEST USING REQUEST LIBRARY
    request = requests.get(url)

    if request.status_code == 200:
        data = request.json()
        return data
    else:
        print(f"Failed to fetch data!")
        return None
    
   

def current_weather(data):
    print("Current data")
    print(".................................")
    print(json.dumps(data['list'][0]['main'], indent = 2))

def historical_data(data):
    print("Historical data")
    print("............................")
    for entry in data['list']:
        timestamp = datetime.utcfromtimestamp(entry['dt'])
        temperature = entry['main']['temp']
        print(f"{timestamp}: {temperature} degree celsius")
  


def math_operations(historical_data):
    temperatures =[entry['main']['temp']for entry in historical_data['list']]
    average = sum(temperatures) / len(temperatures)
    median = statistics.median(temperatures)
    mode = statistics.mode(temperatures)

    print("MATH OPERATIONS")
    print("..........................")
    print(f"Average temperature: {average} degree C")
    print(f"Median: {median} degree C")
    print(f"Mode: {mode} degree C")

    return { 'Average': average,
        'Median ': median,
        'Mode ': mode,
        }


#SAVE TO FILE
def save_file(Math_results, filename = "Analysis.txt"):
    with open(filename, 'w') as file:
        file.write("Weather Mathematical operations")
        for key, value in Math_results.items():
            file.write(f"{key}: {value} degrees celsus")


def main():
          
    city = input("Enter the name of the city: ")

    if isinstance(city, str) and city.strip():
        print("VALID!")

    else:
        print("INVALID")

#FETCH WEATHER DATA
    weather_data = weather(city)
    if weather_data:
        current_weather(weather_data)
        historical_data(weather_data)


#DISPLAY AND ANALYSE HISTORICAL DATA
    historical_data = weather_data

    Math_results = math_operations(historical_data)

#SAVE TO FILE
    save_file(Math_results)
    print("results saved!")



if __name__ == "__main__":
    main()
       
