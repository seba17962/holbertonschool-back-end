#!/usr/bin/python3
"""_summary_
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """_summary_
    """
    employee_id = argv[1]

    url_t = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url_u = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    response_t = requests.get(url_t)
    response_u = requests.get(url_u)
    sum = 0

    if response_t.status_code >= 400 and response_u.status_code >= 400:
        print("Error fetching data")
        exit()

    response_t_jn = response_t.json()
    response_u_jn = response_u.json()

    username = response_u_jn['username']
    user_id = response_u_jn['id']

    json_filename = f"{user_id}.json"
    
    json_data = {
    user_id: [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in response_t_jn
    ]
}
    with open(json_filename, 'w') as file:
        json.dump(json_data, file, indent=2)
        
