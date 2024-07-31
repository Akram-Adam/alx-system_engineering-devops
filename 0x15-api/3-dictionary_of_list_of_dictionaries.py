#!/usr/bin/python3
"""Exports data in the JSON format"""

import requests
import json

def fetch_all_employees():
    try:
        employees_url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(employees_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching employees: {e}")
        return []

def fetch_all_todos():
    try:
        todos_url = 'https://jsonplaceholder.typicode.com/todos'
        response = requests.get(todos_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching todos: {e}")
        return []

def export_todos_to_json(employees, todos):
    json_data = {}
    
    for employee in employees:
        user_id = employee['id']
        employee_name = employee['name']
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        
        json_data[str(user_id)] = [{
            "username": employee_name,
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in user_todos]
    
    json_file = 'todo_all_employees.json'
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)
    
    print(f"Data exported to {json_file}")

def main():
    employees = fetch_all_employees()
    todos = fetch_all_todos()
    if employees and todos:
        export_todos_to_json(employees, todos)

if __name__ == "__main__":
    main()
