#!/usr/bin/python3
"""
 task
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    """_summary_
    """
    employee_ID = argv[1]

    url_todos = \
        f"https://jsonplaceholder.typicode.com/users/{employee_ID}/todos"
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"

    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)
    count = 0

    if response_todos.status_code >= 400 and response_user.status_code >= 400:
        print("Error fetching data")
        exit()

    response_todos_json = response_todos.json()
    response_user_json = response_user.json()

    name = response_user_json['name']

    for task in response_todos_json:
        if task['completed'] is True:
            count += 1

    print(f"Employee {name} is\
 done with tasks({count}/{len(response_todos_json)}):")

    for task in response_todos_json:
        if task['completed'] is True:
            print(f"\t {task['title']}")
