import requests
import json
import os


# ServiceNow API endpoint for knowledge base articles
snow_api_url = "https://your-servicenow-instance/api/now/table/kb_knowledge"

# Confluence API endpoint for creating pages
confluence_api_url = "https://your-confluence-instance/rest/api/content"

# Snow articles folder path
snow_articles_folder = "/Users/cidoni/github/thirdparty/rpi-rgb-led-matrix/bindings/python/samples/snowarticles"

# Confluence credentials
confluence_username = "your-confluence-username"
confluence_password = "your-confluence-password"

# ServiceNow API request headers
snow_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer your-servicenow-api-token"
}

# Confluence API request headers
confluence_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Get knowledge base articles from ServiceNow
response = requests.get(snow_api_url, headers=snow_headers)
articles = response.json().get("result", [])

# Create articles in Confluence and write JSON files
for article in articles:
    # Create article in Confluence
    confluence_data = {
        "type": "page",
        "title": article.get("title"),
        "space": {"key": "your-confluence-space-key"},
        "body": {"storage": {"value": article.get("content"), "representation": "storage"}}
    }
    response = requests.post(confluence_api_url, headers=confluence_headers, auth=(confluence_username, confluence_password), json=confluence_data)
    confluence_page_id = response.json().get("id")

    # Write article as JSON file
    article_file_path = os.path.join(snow_articles_folder, f"{article.get('number')}.json")
    with open(article_file_path, "w") as f:
        json.dump(article, f)

    print(f"Article '{article.get('title')}' created in Confluence with ID {confluence_page_id} and saved as JSON file.")

print("All articles created and JSON files saved.")