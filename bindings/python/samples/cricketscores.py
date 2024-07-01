import requests
import datetime

scores = ""
def get_cricket_scores():
    url = "https://api.cricapi.com/v1/series_info?apikey=04da3031-6e59-4f55-841c-6593dcd2697d&offset=0&id=e079ef23-b5e9-4802-93e9-dd2f27db0533"
    response = requests.get(url)
    score_json = response.json()

    scores = " *** " + score_json["data"]["info"]["name"] + " *** "
    matchlist = score_json["data"]["matchList"]

    formatted_date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    for match in matchlist:
        if match["date"] == formatted_date:
            match_name = match["name"]
            match_status = match["status"]
            scores += " *** " + match_name + " ---- " + match_status + " *** "
    # Do something with match_name and match_status
    return scores