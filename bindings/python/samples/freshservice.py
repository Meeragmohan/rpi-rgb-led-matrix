import requests
import json


# API endpoint and parameters
url = "https://your-freshservice-domain.freshservice.com/api/v2/solutions/categories/{category_id}/articles"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your-api-key"
}
params = {
    "per_page": 100,  # Number of articles per page
    "page": 1  # Page number
}

# Send GET request to the API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the articles from the response
    articles = response.json()

    # Save articles as a JSON file
    with open("articles.json", "w") as file:
        json.dump(articles, file)

    # Print the articles
    print(json.dumps(articles, indent=4))
    # Save articles as a text file
    with open("articles.txt", "w") as file:
        file.write(json.dumps(articles, indent=4))
else:
    print("Failed to retrieve articles. Status code:", response.status_code)