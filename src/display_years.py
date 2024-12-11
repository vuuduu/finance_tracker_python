import os

class DisplayYear:

    def __init__(self, base_path: str):
        self.years = self.__get_years(base_path)

    def run(self):
        print("\nSelect the possible option(s) below")
        while True:
            self.__display_years(self.years)
            # Get input
            # Verify if input is correct 
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


            # choice = input("Enter an input")
            # if choice == 'q' or self.__verify_choice(int(choice), len(.years) + 1):
                

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

    def __verify_choice(self, choice: int, possible_choices: int) -> bool:
        if 1 <= choice <= possible_choices:
            return True
        return False
    
    def __return_object(self, choice):
        return {}
