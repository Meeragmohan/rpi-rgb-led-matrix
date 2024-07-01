import datetime

def get_current_datetime():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%b %d, %Y %I:%M %p")

    return formatted_datetime