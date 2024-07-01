import json
import requests
import os
import requests
import csv
from bs4 import BeautifulSoup
import csv
import datetime

def extract_url_contents(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Example usage
urls = [
    "https://nationaltoday.com/january-holidays/",
    "https://nationaltoday.com/february-holidays/",
    "https://nationaltoday.com/march-holidays/",
    "https://nationaltoday.com/april-holidays/",
    "https://nationaltoday.com/may-holidays/",
    "https://nationaltoday.com/june-holidays/",
    "https://nationaltoday.com/july-holidays/",
    "https://nationaltoday.com/august-holidays/",
    "https://nationaltoday.com/september-holidays/",
    "https://nationaltoday.com/october-holidays/",
    "https://nationaltoday.com/november-holidays/",
    "https://nationaltoday.com/december-holidays/"
]

today = datetime.date.today()

for url in urls:
    contents = ""
    contents = extract_url_contents(url)
    if contents:
        filename = os.path.join("nationaltoday", url.split("/")[-2] + ".txt")
        with open(filename, "w") as file:
            file.write(contents)
        print(f"Contents from URL {url} saved to file: {filename}")
    else:
        print(f"Failed to extract contents from the URL: {url}")

# Loop through each txt file
for url in urls:
    filemonth = os.path.join("nationaltoday", url.split("/")[-2])
    filename = filemonth + ".txt"
    print(f"Processing file: {filename}")
    # Read the contents of the txt file
    with open(filename, "r") as file:
        contents = file.read()

    # Parse the HTML contents using BeautifulSoup
    soup = BeautifulSoup(contents, "html.parser")

    # Find all tr tags with class "row-header row-days" and "row-data row-day"
    rows = soup.find_all("tr", class_=["row-header row-days", "row-data row-days"])
    #print(rows)


    #for each row
    #      if a span element with class "event-date" is present, extract its HTML value and set as the key for the dictionary
    #      for each td element in the row
    #      if a div element with class "img-container" is present, extract the background-image: url attribute value and set as the second value for the value object in the dictionary
    #      if a td element with class "title" is present, extract its HTML value and set as the first value for the value object in the dictionary


    # Create a list to store the dictionaries
    data = []
    event_date_key=""
    # Loop through each row
    for row in rows:
        # Create a dictionary to store the values
        row_data = {}
        event_title=""
        image_url_data=""
        img_container=""
        event_row_data = {}

        # Check if a span element with class "event-date" is present
        event_date = row.find("span", class_="event-date")
        if event_date:
            # Extract the HTML value and set as the key for the dictionary
            event_date_key = event_date.text.strip()
    
        # Loop through each td element in the row
        count=0
        for td in row.find_all("td"):
            count+=1
            # Check if a td element with class "title" is present
            if count<2:
                title = row.find("td", class_="title")
                if title:
                    # Extract its HTML value and set as the first value for the value object in the dictionary
                    event_title = title.text.strip()
                #print(event_title)
                # Check if a div element with class "img-container" is present
                #img_container = td.find("div", class_="img-container")
                if img_container:
                    # Extract the background-image: url attribute value and set as the second value for the value object in the dictionary
                    image_url_data = img_container["style"].split("url(")[-1].strip(");")
                if event_title:
                    event_row_data = {event_date_key: event_title}
                    #print(event_row_data)
                    # Append the dictionary to the list
                    data.append(event_row_data)

    # Print the list of dictionaries
    #for item in data:
        #print(item)

    # Write the data as a file under the nationaltoday folder
    output_filename = os.path.join(filemonth + ".json")
    with open(output_filename, "w") as file:
        file.write(json.dumps(data))

    print(f"Data saved to file: {output_filename}")

    # Get today's date

    # Format today's date as "MMM DD"
    today_formatted = today.strftime("%b %d")
    print (data)
    # Loop through each item in the data list
    for item in data:
        # Check if the key (event date) matches today's date
        if today_formatted in item.keys():
            # Print the item in the desired format
            print(f"{today_formatted}: {item[today_formatted]}")


