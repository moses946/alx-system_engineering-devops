#!/usr/bin/python3
"""
Module that exports data to a json file.
"""
import json
import requests
import sys


def get_data(employee_id):
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={employee_id}")
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    username = user.json()[0].get("username")
    return (username, tasks.json())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 2-export_to_JSON.py <employee_id>")
    e_id = sys.argv[1]

    username, tasks = get_data(e_id)
    tasks_list = []
    for task in tasks:
        a = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
            }
        tasks_list.append(a)

    employee_tasks = {e_id: tasks_list}
    with open("USER_ID.json", "w") as f:
        f.write(json.dumps(employee_tasks))
