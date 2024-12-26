import requests
import json


# ServiceNow API endpoint for knowledge base articles
servicenow_url = "https://your-servicenow-instance/api/now/table/kb_knowledge"

# Confluence API endpoint for creating pages
confluence_url = "https://your-confluence-instance/rest/api/content"

# Confluence space key where the pages will be created
confluence_space_key = "SPACE_KEY"

# Folder path to store the JSON files
json_folder_path = "snowarticles/"

# ServiceNow API request headers
servicenow_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_SERVICE_NOW_API_TOKEN"
}

# Confluence API request headers
confluence_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_CONFLUENCE_API_TOKEN"
}

# Get knowledge base articles from ServiceNow
response = requests.get(servicenow_url, headers=servicenow_headers)
articles = response.json().get("result", [])

# Create articles in Confluence
for article in articles:
    # Extract relevant information from the ServiceNow article
    title = article.get("short_description", "")
    content = article.get("text", "")

    # Create the page in Confluence
    confluence_payload = {
        "type": "page",
        "title": title,
        "space": {"key": confluence_space_key},
        "body": {"storage": {"value": content, "representation": "storage"}},
    }
    response = requests.post(confluence_url, headers=confluence_headers, json=confluence_payload)
    confluence_page_id = response.json().get("id", "")

    # Save a copy of the article as a JSON file
    json_file_path = f"{json_folder_path}/{title}.json"
    with open(json_file_path, "w") as json_file:
        json.dump(article, json_file)
        # Save the output as a JSON file in the "articles" folder
        output = {
            "title": title,
            "confluence_page_id": confluence_page_id,
            "json_file_path": json_file_path
        }
        output_file_path = f"articles/{title}.json"
        with open(output_file_path, "w") as output_file:
            json.dump(output, output_file)
    print(f"Article '{title}' created in Confluence with ID: {confluence_page_id}")
    print(f"JSON file saved at: {json_file_path}")