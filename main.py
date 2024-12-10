import os

def display_available_year(data_path: str) -> int:
    years = sorted(os.listdir(data_path), reverse=True)

    if len(years) > 0:
        print('Select the year you want to view your expenses')
        for i in range(len(years)):
            print(f"{i+1}. {years[i]}")
    else:
        print('You have no available year trackers!')
    
    print(f"{len(years) + 1}. Create a new year directory")
    return len(years) + 1


def verify_choices(possible_choices: int, choice: int) -> bool:
    if possible_choices <= choice <= 1:
        return True
    
    return False


if __name__ == '__main__':
    json_data_path = 'data/json'
    # test_data_path = 'data/csv'

    # Display welcome screen
    print('\n#####################################')
    print('Welcome to Expenses & Incomes Tracker')
    print('#####################################\n')

    # Display available year
    possible_choices = display_available_year(json_data_path)
    print(f"\nPosisble choices = {possible_choices}")
