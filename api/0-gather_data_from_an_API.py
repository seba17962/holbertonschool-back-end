#!/usr/bin/python3
"""
 task
"""
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

    name = response_u_jn['name']

    for task in response_t_jn:
        if task['completed'] is True:
            sum += 1

    print(f"Employee {name} is done with tasks({sum}/{len(response_t_jn)}):")

    for task in response_t_jn:
        if task['completed'] is True:
            print(f"\t {task['title']}")
