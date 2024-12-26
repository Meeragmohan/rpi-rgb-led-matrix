
import urllib.parse
import urllib.request

listofids = "KBNA,KMCI,KORD,KBOS"
def get_metar_data(listofids):
    url = f"https://aviationweather.gov/api/data/metar?ids={urllib.parse.quote(listofids)}"
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    results = data.split('\n')
    return '  --  '.join(results)

print(get_metar_data(listofids))