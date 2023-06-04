from application.db import people

def calculate_salary(name):
    worker = people.get_employees(name)
    if worker != 'No match':
        salary = worker['hours_cost'] * worker['hours']
        print(salary)
    else:
        print('NO MATCH')
    