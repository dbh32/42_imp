from application.db.data import employees


def calculate_salary():
    sum_salary = 0
    for employee in employees:
        sum_salary += employee['salary']
    print(f'Суммарная зарплата в месяц: {sum_salary} рублей')
