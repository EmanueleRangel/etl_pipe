# Importing libraries
import pandas as pd
import requests
import json

# Importing libraries

df = pd.read_csv('./python_dio.txt')
task_ids = df['TaskID'].tolist()

# Reading task IDs

print('Task IDs:')
print(task_ids)

api_url = 'https://localhost:44315/api'

# Defining get_task function

def get_task(id):
    # Sending GET request to the '/Tarefas' endpoint
    response = requests.get(f'{api_url}/Tarefas')

    # Checking if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Retrieving tasks

print('Retrieving tasks:')

tasks = [get_task(id) for id in task_ids]

if tasks:
    print(json.dumps(tasks, indent=2))

# Printing request body and headers

print('Request body:')
print(response.request.body)

print('Response headers:')
print(response.headers)