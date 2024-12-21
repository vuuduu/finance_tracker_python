import os

CHOICE = "choice"
QUIT = "quit"

class YearsData:

    def __init__(self, base_path: str):
        self.years = self.__get_years(base_path)

    # Very if it's either create or retrieve
    # - Create: 
    # --- create a new folder with a new year name
    # --- create 3 new json file (expense, income, payoff)
    # --- ensure the new year doesn't exist yet
    # --- return an object {"action": "create", "year": "<year_created>", "data": None}
    # - Retreive:
    # --- get a list of data expense, income, & payoff
    # --- return an object 
    '''
        {"class_name": "DisplayYear",
            "action": "get", 
            "year": "<year_selected>", 
            "data": None || 
                    {"expense": [], 
                    "income": [], 
                    "payoff": []}
        }
    '''
    def run(self):
        print("\nSelect the possible option(s) below")

        while True:
            self.__display_years(self.years)

            # Get input
            inputs = self.__get_input(len(self.years))
            if inputs[QUIT]:
                print("\nInputs objects:", inputs)
                print(f"Self.years: {self.years}\n")
                return self.__process_year_input(input=inputs)
            print("\n Must enter a valid choice(s)!\n")
            print(inputs)

### HELPER FUNCTION - Processing years display info ###

    def __display_years(self, years: list) -> None:
        for i in range(len(years)):
            print(f"{i+1}. {years[i]}")
        
        print(f"{len(years)+1}. Create a new year trackers")

    def __get_years(self, base_path: str) -> list:
        years = []
        for data in os.listdir(base_path):
            if os.path.isdir(os.path.join(base_path, data)):
                years.append(data)
        return years

    def __get_input(self, possible_choices: int) -> dict:
        choice = 0
        quit = False
        try:
            choice = input("Enter a valid choice (q to quit): ")
            
            # Verify the inputs
            if choice in ['q', 'quit', 'Q']:
                quit = True
            else:
                quit = self.__verify_choice(int(choice), possible_choices)
        except ValueError:
            print("\n Choices CANNOT be a non-numeric value", end=' ')

        return {"choice": choice, "quit": quit}

    def __verify_choice(self, choice: int, possible_choices: int) -> bool:
        if 1 <= choice <= possible_choices + 1:
            return True
        return False


### HELPER FUNCTION - Process input after user pick the correct available option(s) ###

    def __process_year_input(self, input: dict):
        choice = input[CHOICE]

        # check if it's quit
        if choice in ['q', 'quit', 'Q']:
            return self.__return_year_action(action=choice)
        # check if it's create new year
        elif int(input[CHOICE]) == (len(self.years) + 1):
            return self.__create_new_year()
        
        return self.__retrieve_year_data(self.years[int(input[CHOICE]) - 1])

    def __create_new_year(self):
        # Ask for year input
        # Verify the year already exist
        # If yes => ask again or quit
        # If no => create a directory of that year 
        ##### along with 3 empty json data (expense, income, payoff).
        return {"create_new_year": "test"}

    def __retrieve_year_data(self, year: str):
        print(f"\nRetrieve year: {year}")
        return {"retrieve_year": "test"}

    def __return_year_action(self, action: str, year: str=None, data: dict=None):
        return {
            "action": action,
            "year": year,
            "data": data
        }