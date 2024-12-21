from src.years_data import YearsData


if __name__ == '__main__':
    json_data_path = 'data/json'
    # test_data_path = 'data/csv'

    # Display welcome screen
    print('\n#####################################')
    print('Welcome to Expenses & Incomes Tracker')
    print('#####################################\n')

    display_year = YearsData('data/json')
    result = display_year.run()

    print(f"\nResult in main.py {result}\n")


