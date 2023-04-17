#!/usr/bin/python3
''' Python script that, using REST API, for a given employee ID,
    returns information about his/her TODO list progress '''

import json
import requests
import sys
if __name__ == "__main__":

    emp_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    emp_usr = requests.get('https://jsonplaceholder.typicode.com/users/')

    dict_emp = {usr['id']: [{"username": usr['username'],
                             "task": elem['title'],
                             "completed": elem['completed']}
                            for elem in emp_todo.json()
                            if elem['userId'] == usr['id']]
                for usr in emp_usr.json()}

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dict_emp, f)
