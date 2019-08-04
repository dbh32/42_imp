from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    print('1 - показать список сотрудников')
    print('2 - показать суммарную ЗП')
    while True:
        user_input = input()
        if user_input == '1':
            get_employees()
        elif user_input == '2':
            calculate_salary()


if __name__ == '__main__':
    main()
