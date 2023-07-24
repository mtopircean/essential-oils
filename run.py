import gspread
from google.oauth2.service_account import Credentials

import colorama
from tabulate import tabulate

"""
General setup information done in accordance to LoveSandwiches project and it`s instructions.
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('EssentialOils')

program_menu = ("1. Add a product to the database", "2. List oils database",
                "3. Search a product in the database", "4. List patients database", "5. Search patient in the database")


def list_menu(menu_options):

    """
    Function set in order to display to the user a main menu option.
    It starts a while loop which runs until user selects an option.
    Option is validated as an integer between 1 and 5 including, and validates the selection.
    Print messages are set to handle alll scenarios: selected option, wrong type of parameter selected.
    """

    print(colorama.Fore.BLUE  + colorama.Style.BRIGHT + "Options Menu:")
    for option in menu_options:
        print(option)
    while True:
        print()
        selected_option = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE +
            "What do you want to do? Add the number of your option without any other characters:")
        if selected_option.isdigit() and 1 <= int(selected_option) <= 5:
            return selected_option
        else:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You haven`t selected a valid option.")
            print()
            print(colorama.Style.RESET_ALL + colorama.Fore.BLUE +
                  "Please select a value from 1 to 5 based on the options menu list.")


class Oils:
    """
    Creates a class related to our oil and sets it`s properties. It uses 2 functions to:
        - eo_catalogue: creates the object related to our oils and sets it`s relevant properties
        - str self: which defines in which way the added poil is returned, 
        - as a string with each line one under the other
    There are a series of attributes that are defined in order to set the main properties of this objects which are:
    it`s name, the ailment that it addresses, the oil price, it if needs a difuser to apply it and 
    then a calculated score based on a basic calculation.
    """

    def eo_catalogue(self, name, ailment, price, application, score):
        self.name = name
        self.ailment = ailment
        self.price = price
        self.application = application
        self.score = score

    def __str__(self):
        return f"Oil name: {self.name}\nAilment: {self.ailment}\nPrice: {self.price}\nNeeds difuser: {self.application}\nScore: {self.score}"


def add_oil():

    """
    Function with main functionality to add oils to the database. This is done by:
        - requesting through inputs to add the name, ailment, diffuser application, price; note, score is calculated automatically
        - validates the data provided for application(as yes or no, ignoring upper/lower) and for price(number only with . as a separator)
    Function allows to run a loop in order for user to keep adding oils if he chooses through a simple yes or no input.
    If user doesn`t want to add another product, the loop will trigger the option to return to main menu, with a yes or no selection.
    Each oil added is populated into the "master" sheet in the google sheets called EssentialOils.
    """


    my_oil = Oils()

    """
    Section of code to related to input takes for the different properties needed to be defined by the user.
    """


    print()
    name = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Input the name of the oil: ")
    print()
    ailment = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
        "Input the ailments the oil addresses. We recommend a format in which, if multiple ailments, separate them by comma and space. For example: headace, toothache. Please provide input: ")
    while True:
        try:
            print()
            price = float(input(colorama.Style.RESET_ALL +
                                colorama.Fore.BLUE + "Input the price value: "))
            break
        except ValueError:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not entered a number value. Please write resubmit your answer. Do not use a ',' to separate the decimals, use instead a '.'.")

    while True:
        print()
        application = input(colorama.Style.RESET_ALL +
                            colorama.Fore.BLUE + "Does it need a difuser(Yes/No): ")
        if application.lower() == "yes" or application.lower() == "no":
            break
        else:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")

    score = price / 100 + (0 if application == "yes" else 1)

    """
    Adds the oil and updates the master sheet.
    It uses an outside function called update_oils_worksheet.
    """
    
    my_oil.eo_catalogue(name, ailment, price, application, score)
    print()
    print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + f"You added {my_oil.name} to the database")
    print()
    print(my_oil)

    data = [my_oil.name, my_oil.ailment, my_oil.price,
            my_oil.application, my_oil.score]
    update_oils_worksheet(data, "master")

    """
    Loop created to add the user an option to keep adding oils before returning to main menu.
    It also does a basic validation of their choices, limited to a yes or no option.
    """

    while True:
        print()
        re_run = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
            "Do you want to add another product to the database? Type Yes or No: ")
        if re_run.lower() == "no":
            print()
            main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                "Do you want to exit to main menu? Type Yes if you want to return to main. Otherwise type No to exit program:")
            print()
            if main_menu.lower() == "yes":
                main()
            elif main_menu.lower() == "no":
                print()
                print(colorama.Fore.RED + colorama.Style.BRIGHT +"Now exiting program!")
                exit()
            else:
                print()
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")
        elif re_run.lower() == "yes":
            add_oil()
        else:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")


def update_oils_worksheet(data, worksheet):
    """
    Function created to update the sheet named master in the EssentialOils google sheet.
    Function:
        - informs on updates being made to the sheet
        - sets the area where the data is transfered to the master sheet, always being the next line by reading it`s row length and adding the data
        to the next unocupied line
        - offers confirmation that the update was completed

    """
    print()
    print(colorama.Style.RESET_ALL +
          colorama.Fore.BLUE + f"Updating {worksheet}.")
    worksheet_master = SHEET.worksheet(worksheet)
    following_row = len(worksheet_master.get_all_values()) + 1

    worksheet_master.insert_row(data, following_row)
    print()
    print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + f"{worksheet} updated.")
    print()


def list_oils():
    """
    Function defined in order to pull the data from the master worksheet and return it into a table format for the user.
    Function:
        - pulls the data using all_oils and appends it to a new list called oils_table
        - using tabulate it then prints the result into a grid table format
    As all functions, it then gives the user an option to jump to main menu.

    Note: Tabulate how to install and use is using inspiration from: https://pypi.org/project/tabulate/.
    """
    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    oils_table = []
    for oil in all_oils:
        oils_table.append([oil['Oil Name'], oil['Ailment'],
                          oil['Price'], oil['Application'], oil['Score']])

    print()
    print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Here is a list of all your stored oils:")
    print()
    print(tabulate(oils_table, headers=[
          "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))

    print()
    main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
        "Do you want to exit to main menu? Type Yes if you want to return to main. Otherwise type No to exit program:")
    print()
    if main_menu.lower() == "yes":
        main()
    elif main_menu.lower() == "no":
        print()
        print(colorama.Fore.RED + colorama.Style.BRIGHT +"Now exiting program!")
        exit()
    else:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")
        print()

def find_store_oils():
    """
    Function created to allow user to search over the database and retrieve an oil based on either a name or ailment.
    It is designed so it allows even partial parts of the words, so it gives flexibility and allows the user to limit
    their mistakes to a minimum.
    It also gives the option to store search under a patient to offer the search history in a different function.
    Function:
        - retrieves stored data
        - allows user to search by either name of ailment
        - validates and returns a result if it exists, else it prints that no record exists
        - give the option to run a new search
        - gives the option to create a patient record of the search or not through a yes / no validation
        - appends the data to an existing patient, if patient already exists or creates a new one
        - once user stops it`s search activity can always return to main menu

    """

    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    """
    Search related code section with tabulate styling for returned result.
    """

    while True:
        print()
        search_criteria = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
            "Input the name of the oil or the ailment you need to address: ")

        matching_oils = []
        for oil in all_oils:
            if 'Oil Name' in oil and search_criteria.lower() in oil['Oil Name'].lower():
                matching_oils.append(oil)
            elif 'Ailment' in oil and search_criteria.lower() in oil['Ailment'].lower():
                matching_oils.append(oil)

        if matching_oils:
            print()
            print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Please find bellow your search result:")
            search_table = []
            for oil in matching_oils:
                search_table.append([oil['Oil Name'], oil['Ailment'],
                                     oil['Price'], oil['Application'], oil['Score']])
            print()
            print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Here is your search result:")
            print()
            print(tabulate(search_table, headers=[
                "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))

            """
            Code allows user to save search under patient name.
            Uses a series of validations for user inputs.
            It also validates presence of the patient in the data base and takes an action to either create new or append.
            """

            add_patient = None
            while add_patient not in ["yes", "no"]:
                print()
                add_patient = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                    "Do you want to save your search connected to a patient name? Type Yes/No: ").lower()

                if add_patient not in ["yes", "no"]:
                    print()
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")

            if add_patient.lower() == "yes":
                print()
                sheet_name = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                    "List patient`s name:")
                patients_sheet = SHEET.worksheet("patients_list")
                patients_data = patients_sheet.get_all_records()
                patients_names = [patient['Patient Name']
                                  for patient in patients_data]

                if sheet_name in patients_names:
                    print()
                    print(
                        colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Patient already has a record. Your new search will be appended to the existing one.")
                    patient_index = patients_names.index(sheet_name)
                    next_search = len(patients_data[patient_index]) + 1
                    patients_sheet.insert_row([], next_search)

                else:
                    print()
                    print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Adding a new patient to your list.")
                    patients_sheet.append_row([sheet_name])

                """
                Appends the sheet patient_list in the google sheet EssentialOils.
                """

                for oil in matching_oils:
                    oil_data = [sheet_name, oil['Oil Name'], oil['Ailment'],
                                oil['Price'], oil['Application'], oil['Score']]
                    patients_sheet.append_row(oil_data)
                print()
                print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Your search was added to your search history")

        else:
            print()
            print(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                "We couldn`t find any result matching your search criteria. Please search again")
        print()
        new_search = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Do you want to run a new search? Type Yes/No: ")
        while new_search.lower() not in ["yes", "no"]:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")
            print()
            new_search = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                "Do you want to run a new search? Type Yes/No: ")
        """
        Standard functionality across the code to allow the user to return to the main menu.
        """
        if new_search.lower() != "yes":
            print()
            main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                "Do you want to exit to main menu? Type Yes if you want to return to main. Otherwise type No to exit program:")
            if main_menu.lower() == "yes":
                main()
            elif main_menu.lower() == "no":
                print()
                print(colorama.Fore.RED + colorama.Style.BRIGHT +"Now exiting program!")
                exit()
            else:
                print()
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")


def list_patients():
    """
    Function created in order to allow user to list their patients database.
    Function:
        - pulls all records
        - presents data in a table format using tabulate
    Offers again the option to exit to main menu.
    """
    worksheet_id = "patients_list"
    worksheet = SHEET.worksheet(worksheet_id)
    all_patients = worksheet.get_all_records()

    """
    Creates a list and stores the results in patients_table
    """
    
    patients_table = []
    for patient in all_patients:
        patients_table.append([patient['Patient Name'], patient['Oil Name'],
                              patient['Ailment'], patient['Price'], patient['Application'], patient['Score']])
    print()
    print(colorama.Style.RESET_ALL + colorama.Fore.BLUE +
          "Here is a list of all your stored patients:")
    print()
    print(tabulate(patients_table, headers=[
          "Patient Name", "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))
    print()

    """
    Returns to main menu.
    """

    main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
        "Do you want to exit to main menu? Type Yes if you want to return to main. Otherwise type No to exit program:")
    if main_menu.lower() == "yes":
        main()
    elif main_menu.lower() == "no":
        print()
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "Now exiting program!")
        exit()
    else:
        print()
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")


def search_patient():
    """
    Functions allows the user to search for a patient in the database, in the patients_list sheet.
    Function:
        - pulls the data in patients_list
        - takes input from user(takes partial input, partial name for example) and returns the result in a table format
        - provides through print lines notifications of different actions happening in the program
        - allows the user to re-run new searches once one is complete
        - validates input choices and limits the amount of errors for simple decissions: yes or no
    Provides as normal, the option to return to the main menu
    """
    while True:
        worksheet_id = "patients_list"
        worksheet = SHEET.worksheet(worksheet_id)
        all_patients = worksheet.get_all_records()
        print()

        """
        Main input section to allow the user to perform a search and return a result in table format using tabulate.
        Allows the user to re-run searches if desired.
        """
        search_criteria = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
            "Input the name of the patient on a First Name Second Name format. For example John Doe. Please check to make sure spelling is correct before hitting ENTER: ")
        matching_patient = []
        for patient in all_patients:
            if 'Patient Name' in patient and search_criteria.lower() in patient['Patient Name'].lower():
                matching_patient.append(patient)

        if matching_patient:
            patients_table = []
            for patient in matching_patient:
                patients_table.append([patient['Patient Name'], patient['Oil Name'],
                                    patient['Ailment'], patient['Price'], patient['Application'], patient['Score']])
            print()
            print(colorama.Style.RESET_ALL + colorama.Fore.BLUE +
                "Here is a list of entries for the patient searched:")
            print()
            print(tabulate(patients_table, headers=[
                "Patient Name", "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))

        else:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                "Your search hasn`t returned any result. Please check that the name is spelled correctly and search again.")
        print()
        new_search = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + "Do you want to run a new search? Type Yes/No: ")
        while new_search.lower() not in ["yes", "no"]:
            print()
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                    "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")
            print()
            new_search = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                    "Do you want to run a new search? Type Yes/No: ")
        if new_search.lower() != "yes":
            print()

            """ Offers user the option to return to main menu"""

            main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.BLUE + 
                "Do you want to exit to main menu? Type Yes if you want to return to main. Otherwise type No to exit program:")
            if main_menu.lower() == "yes":
                main()
            elif  main_menu.lower() == "no":
                print()
                print(colorama.Fore.RED + colorama.Style.BRIGHT +"Now exiting program!")
                exit()
            else:
                print()
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                    "You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")


def main():

    """
    Main function called at the end of each section in order to allow users to return and perform the various
    function/interactions in the program.
    Uses an infinite loop to allow the program to run until terminated.
    Through selected_option it takes the input from user in order to identify and return the function the user
    wants to acess

    """

    while True:

        selected_option = list_menu(program_menu)
        print()
        print(colorama.Style.RESET_ALL + colorama.Fore.BLUE +
              "The option you have selected:", selected_option)

        if selected_option == "1":
            add_oil()
        elif selected_option == "2":
            list_oils()
        elif selected_option == "3":
            find_store_oils()
        elif selected_option == "4":
            list_patients()
        elif selected_option == "5":
            search_patient()
        else:
            print()
            print("The option you have selected:", selected_option)


"""
Bellow code set in order to sensure the main functions runs not only when called inside a function, but also 
when the python script is run  python3 run.py.
Took inspiration from:https://realpython.com/if-name-main-python/
"""

if __name__ == "__main__":
    main()