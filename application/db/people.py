from application.db.data import employees


def get_employees():
    count = 0
    names = []
    for employee in employees:
        count += 1
        names.append(employee['name'])
    print(f'Всего {count} сотрудника(ов): {names}')
