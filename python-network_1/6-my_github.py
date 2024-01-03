#!/usr/bin/python3
""" Uses the GitHub API to display user id """
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    try:
        result = response.json()
        print(result.get("id"))
    except ValueError:
        print("None")
