#!/usr/bin/python3
''' Python script that, using REST API, for a given employee ID,
    returns information about his/her TODO list progress '''

import requests
import sys
import json
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if int(sys.argv[1]):
            user_id = int(sys.argv[1])
        else:
            exit
        emp = requests.get('https://jsonplaceholder.typicode.com/users/' +
                           str(user_id))
        emp_name = emp.json()['name']
        emp_todo = requests.get('https://jsonplaceholder.typicode.com/todos')

        dict_emp = {user_id: [{"task": elem['title'],
                               "completed": elem['completed'],
                               "username": emp.json()['username']}
                              for elem in emp_todo.json()
                              if elem['userId'] == user_id]}

        with open(f'{user_id}.json', 'w') as f:
            json.dump(dict_emp, f)
