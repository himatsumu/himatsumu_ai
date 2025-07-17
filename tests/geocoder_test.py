import googlemaps
from config.settings import get_setting

settings = get_setting()

googleapikey = settings.GOOGLE_PLACE_KEY
gmaps = googlemaps.Client(key=googleapikey)


result = gmaps.geocode(address = "梅田" , language = "ja")
location = result[0]["geometry"]["location"]["lat"] , result[0]["geometry"]["location"]["lng"]
address = result[0]["formatted_address"]
print(f"場所{location[0]}\n住所{address}")
