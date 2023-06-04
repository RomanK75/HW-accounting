
worker_list = [
    {'name': 'Anna', 'hours_cost' : 500, 'hours': 120 },
    {'name': 'Vlad', 'hours_cost' : 800, 'hours': 140 },
    {'name': 'Alex', 'hours_cost' : 400, 'hours': 150 },
    {'name': 'Alena', 'hours_cost' : 1000, 'hours': 160 }
]

def get_employees(name):
    for worker in worker_list:
        if worker['name'] == name:
            return worker
    return 'No match'
