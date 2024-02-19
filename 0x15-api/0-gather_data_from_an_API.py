#!/usr/bin/python3
"""
Module that returns information about an employees TODO list.
"""

import requests
import sys


def get_data(employee_id):
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={employee_id}")
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    done_tasks = []
    for task in tasks.json():
        if task.get('completed'):
            done_tasks.append(task)

    return (user.json()[0], tasks.json(), done_tasks)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee ID>")
    e_id = sys.argv[1]

    user, tasks, done = get_data(e_id)
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(done), len(tasks)))
    for task in done:
        print(f"\t {task.get('title')}")
