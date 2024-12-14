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
                print("Inputs objects:", inputs)
                print("Self.years:", self.years)
                break
            print("\n Must enter a valid choice(s)!")
            print(inputs)


    def __get_input(self, possible_choices: int):
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
            print("\n Choices CANNOT be a non-numeric value")

        return {"choice": choice, "quit": quit}

    def __verify_choice(self, choice: int, possible_choices: int) -> bool:
        if 1 <= choice <= possible_choices + 1:
            return True
        return False

    def __get_years(self, base_path: str) -> list:
        years = []
        for data in os.listdir(base_path):
            if os.path.isdir(os.path.join(base_path, data)):
                years.append(data)
        return years
    
    def __display_years(self, years: list):
        for i in range(len(years)):
            print(f"{i+1}. {years[i]}")
        
        print(f"{len(years)+1}. Create a new year trackers")
