#!/usr/bin/python3
""" Takes in a letter, sends a POST request, and displays the response """
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    response = requests.post(url, data=data)
    try:
        result = response.json()
        if result:
            print(f"[{result['id']}] {result['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
