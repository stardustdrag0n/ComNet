import requests
from datetime import datetime

ip_address = input("Enter IP address: ")

response = requests.get(f"http://worldtimeapi.org/api/ip/{ip_address}")
data = response.json()

timezone = data['timezone']

datetime_obj = datetime.fromisoformat(data['datetime'])

day_of_year = datetime_obj.timetuple().tm_yday

print(f"Timezone: {timezone}")
print(f"Current DateTime: {datetime_obj}")
print(f"Day of the Year: {day_of_year}")
