#!/usr/bin/python3
"""Exports data in the JSON format"""
import requests
import sys
import json

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
        user_id = employee['id']

        # Prepare data for JSON
        json_data = {
            str(user_id): []
        }
        for task in todos:
            json_data[str(user_id)].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            })
        
        # Write data to JSON file
        json_file = f"{user_id}.json"
        with open(json_file, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        print(f"Data exported to {json_file}")
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
