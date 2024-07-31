#!/usr/bin/python3
"""Exports data in the CSV format"""

import requests
import sys
import csv

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

        # Prepare data for CSV
        csv_data = []
        for task in todos:
            csv_data.append([user_id, employee_name, task['completed'], task['title']])
        
        # Write data to CSV
        csv_file = f"{user_id}.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(csv_data)
        
        print(f"Data exported to {csv_file}")
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
