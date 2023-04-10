#!/usr/bin/python3
''' Python script that, using REST API, for a given employee ID,
    returns information about his/her TODO list progress '''

import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if int(sys.argv[1]):
            user_id = int(sys.argv[1])
        else:
            exit
        emp = requests.get('https://jsonplaceholder.typicode.com/users/'
                           + str(user_id))
        emp_name = emp.json()['name']

        emp = requests.get('https://jsonplaceholder.typicode.com/todos')
        todos = [elem['title'] for elem in emp.json()
                 if elem['userId'] == user_id and not elem['completed']]

        print(f"Employee {emp_name} is done with tasks({len(todos)}/20):")
        for elem in todos:
            print(f"\t {elem}")
