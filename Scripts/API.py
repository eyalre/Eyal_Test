# Example: Simple API script in Python that retrieves data from a public API

import requests

# URL of the API endpoint (example: JSONPlaceholder)
url = "https://data.gov.au"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Retrieved data:")
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")b  