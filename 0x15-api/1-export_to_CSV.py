#!/usr/bin/python3
"""
Module to export data in the CSV format.
"""
import csv
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
        print("Usage: 1-export_to_CSV.py <employee ID>")
    e_id = sys.argv[1]

    username, tasks = get_data(e_id)

    with open(f"{e_id}.csv", "w", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                [e_id, username, task.get("completed"), task.get("title")])
