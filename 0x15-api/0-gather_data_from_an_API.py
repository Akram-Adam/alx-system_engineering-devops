#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""


import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch employee details
        employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        response = requests.get(employee_url)
        response.raise_for_status()
        employee = response.json()
        
        # Fetch TODO list for the employee
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        response = requests.get(todos_url)
        response.raise_for_status()
        todos = response.json()

        # Extract relevant data
        employee_name = employee['name']
        total_tasks = len(todos)
        done_tasks = [task for task in todos if task['completed']]
        number_of_done_tasks = len(done_tasks)

        # Display TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
    except requests.RequestException as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid employee ID")
    except KeyError:
        print("Error processing data")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
