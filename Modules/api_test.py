# File Name: api_test.py
import requests  # Importing the downloaded external module

# Sending a request to a live website to get data
response = requests.get("https://api.github.com")

# Checking the HTTP Status Code (200 means Success)
print("Status Code:", response.status_code) 

# Printing the data format type
print("Content Type:", response.headers['content-type'])