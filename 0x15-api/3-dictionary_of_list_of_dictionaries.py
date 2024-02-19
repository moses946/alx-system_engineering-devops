"""
Module that lists all tasks from all employees.
"""
import json
import requests


def get_data():
    employees = requests.get(
        f"https://jsonplaceholder.typicode.com/users").json()
    user_ids = []
    users_todos = []
    for employee in employees:
        e_id = employee.get('id')
        user_ids.append(e_id)
        tasks = requests.get(
            f"http://jsonplaceholder.typicode.com/todos?userId={e_id}"
        ).json()
        user_todo = []
        for task in tasks:
            a = {
                "username": employee.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_todo.append(a)
        users_todos.append(user_todo)

    return (user_ids, users_todos)


if __name__ == "__main__":
    user_ids, users_todos = get_data()
    data = dict(zip(user_ids, users_todos))

    with open("todo_all_employees.json", "w")as f:
        f.write(json.dumps(data))
