import requests
import xml.etree.ElementTree as ET

wotd=""

def fetchWordOfTheDay():
    url = "https://wordsmith.org/awad/rss1.xml"

    response = requests.get(url)
    xml_data = response.text

    root = ET.fromstring(xml_data)

    for item in root.findall(".//item"):
        title = item.find("title").text
        description = item.find("description").text
        wotd = "Word of the day: " + title + " - " + description
    return wotd

print (fetchWordOfTheDay())
