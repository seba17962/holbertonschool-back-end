#!/usr/bin/python3
"""
Summary : Api requesting employee information
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Module for Asking apis info"""
    employee_id = argv[1]
    url_t = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url_u = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url_t)
    responseuser = requests.get(url_u)
    sum = 0

    if response.status_code >= 400 and responseuser.status_code >= 400:
        print("Error fetching data")
        exit()

    employee = response.json()
    employeeinfo = responseuser.json()
    name = employeeinfo['name']
    for task in employee:
        if task['completed'] is True:
            sum += 1
    print(f"Employee {name} is done with tasks({sum}/{len(employee)}):")
    for task in employee:
        if task['completed'] is True:
            print(f"\t {task['title']}")