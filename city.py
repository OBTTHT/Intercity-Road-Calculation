from geopy.geocoders import Nominatim
import requests
import json

url = "http://router.project-osrm.org/route/v1/car/"

geolocator = Nominatim(user_agent="geoapiExercises")
city1 = input("Şehir 1:")
city2 = input("Şehir 2:")
l1 = geolocator.geocode(city1)
l2 = geolocator.geocode(city2)
p1 = (l1.longitude, l1.latitude)
p2 = (l2.longitude, l2.latitude)

url += f"{p1[0]},{p1[1]};{p2[0]},{p2[1]}?overview=false"

r = requests.get(url)
routes = json.loads(r.content)
km = routes.get("routes")[0]["distance"]

print("İki şehir arasındaki uzaklık:", round((km/1000), 2))

