import datetime
import json


def get_today_event():

    today_days = ""

    # Get today's date
    today = datetime.date.today()
    # Get today's month in lowercase
    today_month = today.strftime("%B").lower()

    # Read the contents of the JSON file
    with open('/home/cyclops/Projects/rpi-rgb-led-matrix/bindings/python/samples/nationaltoday/' + today_month +'-holidays.json') as file:
        data = json.load(file)

    # Format today's date as "MMM DD"
    today_formatted = today.strftime("%b %d")

    # Loop through each item in the data list
    for item in data:
        # Check if the key (event date) matches today's date
        #print(list(item.keys())[0] + "-" + today_formatted)
        if today_formatted == list(item.keys())[0]:
            # Print the item in the desired format
            today_days += f"{item[today_formatted]}, "
    
    today_days = "Today " + today_formatted + " is " + today_days[:-2]
    return today_days

if __name__ == "__main__":
    print(get_today_event())