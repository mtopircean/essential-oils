import gspread
from google.oauth2.service_account import Credentials

import colorama
from tabulate import tabulate

"""
General setup information done in accordance to
LoveSandwiches project and it`s instructions.
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

program_menu = ("1. Add a product to the database",
                "2. List oils database",
                "3. Search a product in the database",
                "4. Modify oil data",
                "5. List patients database",
                "6. Search patient in the database")


def list_menu(menu_options):
    """
    Function set in order to display to the user a main menu option.
    It starts a while loop which runs until user selects an option.
    Option is validated as an integer between 1 and 6 including,
    and validates the selection.
    Print messages are set to handle alll scenarios:
    selected option, wrong type of parameter selected.
    """

    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "\nOptions Menu:\n")
    for option in menu_options:
        print(option)
    while True:
        selected_option = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                "\nWhat do you want to do? "
                                "Add the number of your option "
                                "in numeric format: \n")
        if selected_option.isdigit() and 1 <= int(selected_option) <= 6:
            return selected_option
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou haven`t selected a valid option.\n")
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                  "Please select a value from 1 to 6 "
                  "based on the options menu list.\n")


class Oils:
    """
    Creates a class related to our oil and sets it`s properties.
    It uses 2 functions to:
        - eo_catalogue: creates the object related
        to our oils and sets it`s relevant properties
        - str self: which defines in which way
        the added poil is returned,
        - as a string with each line one under the other
    There are a series of attributes that
    are defined in order to set the main properties
    of this objects which are:
    it`s name, the ailment that it addresses,
    the oil price, it if needs a Diffuser to apply it and
    then a calculated score based on a basic calculation.
    """

    def eo_catalogue(self, name, ailment, price, application, score):
        self.name = name
        self.ailment = ailment
        self.price = price
        self.application = application
        self.score = score

    def __str__(self):
        return f"Oil name: {self.name}\nAilment: {self.ailment}\nPrice: {self.price}\nCan it be used with a Diffuser: {self.application}\nScore: {self.score}"


def add_oil():
    """
    Function with main functionality to add oils to the database.
    This is done by:
        - requesting through inputs to add the name,
        ailment, diffuser application, price;
        note, score is calculated automatically
        - validates the data provided for application
        (as yes or no, ignoring upper/lower) and for price
        (number only with . as a separator)
    Function allows to run a loop in order for user to keep
    adding oils if he chooses through a simple yes or no input.
    If user doesn`t want to add another product, the loop will
    trigger the option to return to main menu,
    with a yes or no selection.
    Each oil added is populated into the "master"
    sheet in the google sheets called EssentialOils.
    """


    my_oil = Oils()
    """
    Section of code to related to input takes for
    the different properties needed to be defined by the user.
    """
    name = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                 "Input the name of the oil: \n")

    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    for oil in all_oils:
        if oil["Oil Name"].lower().strip() == name.lower().strip():
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                "\nThe oil already exists in the database. "
                "If you want to modify the oil, use the Modify oil data function.")
            ailment=oil["Ailment"]
            price=oil["Eur Price"]
            application=oil["Diffuser suitable"]
            score=oil["Score"]
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE + "\n" +  f"Oil name: {name}\nAilment: {ailment}\nPrice: {price}\nCan it be used with a diffuser: {application}\nScore: {score}")
            while True:
                re_run = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                            "\nDo you want to add another product to the database? "
                            "Type Yes or No: \n")
                if re_run.lower() == "no":
                    while True:
                        main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                        "\nDo you want to exit to main menu? "
                                        "Type Yes if you want to return to main. "
                                        "Otherwise type No to exit program: \n")
                        if main_menu.lower() == "yes":
                            main()
                        elif main_menu.lower() == "no":
                            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                                "Now exiting program!\n")
                            exit()
                        else:
                            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                                "You have not selected a valid option. "
                                "Your answer should be either 'Yes' or 'No'. "
                                "Please resubmit your answer.\n")
                elif re_run.lower() == "yes":
                    add_oil()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                        "You have not selected a valid option. "
                        "Your answer should be either 'Yes' or 'No'. "
                        "Please resubmit your answer.\n")

    ailment = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                    "\nInput the ailments the oil addresses. "
                    "We recommend a format in which, if multiple ailments, "
                    "separate them by ',' and space. "
                    "For example: headace, toothache. "
                    "Please provide your input: \n")
    while True:
        try:
            price = float(input(colorama.Style.RESET_ALL +
                                colorama.Fore.WHITE +
                                "\nInput the Euro price value. "
                                "Use a '.' decimal format, ex 3.1 . "
                                "Provide your input: \n"))
            break
        except ValueError:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not entered a numeric value. "
                  "Please resubmit your answer. "
                  "Do not use a ',' to separate the decimals, "
                  "use instead a '.'.\n")
    while True:
        application = input(colorama.Style.RESET_ALL +
                            colorama.Fore.WHITE +
                            "\nCan it be used with a Diffuser?(Yes/No): \n").strip()
        if application.lower() == "yes" or application.lower() == "no":
            break
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")
    score = price / 10 * 0.30 + float(10 if application == "yes" else 0)
    """
    Adds the oil and updates the master sheet.
    It uses an outside function called update_oils_worksheet.
    """

    my_oil.eo_catalogue(name, ailment, price, application, score)
    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
          f"You added {my_oil.name} to the database\n")
    print(my_oil)
    data = [my_oil.name, my_oil.ailment, my_oil.price,
            my_oil.application, my_oil.score]
    update_oils_worksheet(data, "master")
    """
    Loop created to add the user an option to keep adding oils
    before returning to main menu.
    It also does a basic validation of their choices,
    limited to a yes or no option.
    """
    while True:
        re_run = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                       "Do you want to add another product to the database? "
                       "Type Yes or No: \n")
        if re_run.lower() == "no":
            main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                              "\nDo you want to exit to main menu? "
                              "Type Yes if you want to return to main. "
                              "Otherwise type No to exit program: \n")
            if main_menu.lower() == "yes":
                main()
            elif main_menu.lower() == "no":
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "Now exiting program!\n")
                exit()
            else:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "You have not selected a valid option. "
                      "Your answer should be either 'Yes' or 'No'. "
                      "Please resubmit your answer.\n")
        elif re_run.lower() == "yes":
            add_oil()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")



def update_oils_worksheet(data, worksheet):
    """
    Function created to update the sheet named master in
    the EssentialOils google sheet.
    Function:
        - informs on updates being made to the sheet
        - sets the area where the data is transfered to the master sheet,
        always being the next line by reading it`s row length
        and adding the data
        to the next unocupied line
        - offers confirmation that the update was completed

    """
    print(colorama.Style.RESET_ALL +
          colorama.Fore.WHITE + f"Updating {worksheet}.")
    worksheet_master = SHEET.worksheet(worksheet)
    following_row = len(worksheet_master.get_all_values()) + 1

    worksheet_master.insert_row(data, following_row)
    print(colorama.Style.RESET_ALL +
          colorama.Fore.WHITE + f"{worksheet} updated.\n")


def list_oils():
    """
    Function defined in order to pull the data from the master worksheet
    and return it into a table format for the user.
    Function:
        - pulls the data using all_oils and appends it to
        a new list called oils_table
        - using tabulate it then prints the
        result into a grid table format
    As all functions, it then gives the user an option to jump to main menu.

    Note: Tabulate how to install and use
    is using inspiration from: https://pypi.org/project/tabulate/.
    """
    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    oils_table = []
    for oil in all_oils:
        oils_table.append([oil['Oil Name'], oil['Ailment'],
                          oil['Eur Price'], oil['Diffuser suitable'], oil['Score']])

    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
          "Here is a list of all your stored oils: \n")
    print(tabulate(oils_table, headers=[
          "Oil Name", "Ailment", "Eur Price", "Diffuser suitable", "Score"], tablefmt="grid"))
    while True:
        main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                        "\nDo you want to exit to main menu? "
                        "Type Yes if you want to return to main. "
                        "Otherwise type No to exit program: \n")
        if main_menu.lower() == "yes":
            main()
        elif main_menu.lower() == "no":
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                "Now exiting program!\n")
            exit()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                "You have not selected a valid option. "
                "Your answer should be either 'Yes' or 'No'. "
                "Please resubmit your answer.\n")


def find_store_oils():
    """
    Function created to allow user to search over
    the database and retrieve an oil based on either a name or ailment.
    It is designed so it allows even partial parts
    of the words, so it gives flexibility and allows the user to limit
    their mistakes to a minimum.
    It also gives the option to store search
    under a patient to offer the search history in a different function.
    Function:
        - retrieves stored data
        - allows user to search by either name of ailment
        - validates and returns a result if it exists,
        else it prints that no record exists
        - give the option to run a new search
        - gives the option to create a patient record
        of the search or not through a yes / no validation
        - appends the data to an existing patient,
        if patient already exists or creates a new one
        - once user stops it`s search activity can always return to main menu

    """

    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    """
    Search related code section with tabulate styling for returned result.
    """

    while True:
        search_criteria = input(colorama.Style.RESET_ALL +
                                colorama.Fore.WHITE +
                                "Input the name of the oil "
                                "or the ailment you need to address: \n")
        if not search_criteria:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "You have not entered a valid option. "
              "Please make sure your field is not empty.")
            continue

        matching_oils = []
        for oil in all_oils:
            if 'Oil Name' in oil and search_criteria.lower().strip() in oil['Oil Name'].lower().strip():
                matching_oils.append(oil)
            elif 'Ailment' in oil and search_criteria.lower() in oil['Ailment'].lower():
                matching_oils.append(oil)

        if matching_oils:
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                  "Please find bellow your search result: \n")
            search_table = []
            for oil in matching_oils:
                search_table.append(
                    [oil['Oil Name'], oil['Ailment'],
                     oil['Eur Price'], oil['Diffuser suitable'],
                     oil['Score']])
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                  "Here is your search result: \n")
            print(tabulate(search_table, headers=[
                "Oil Name", "Ailment",
                "Eur Price", "Diffuser suitable", "Score"], tablefmt="grid"))

            """
            Code allows user to save search under patient name.
            Uses a series of validations for user inputs.
            It also validates presence of the patient
            in the data base and takes an action
            to either create new or append.
            """

            add_patient = None
            while add_patient not in ["yes", "no"]:
                add_patient = input(colorama.Style.RESET_ALL +
                                    colorama.Fore.WHITE +
                                    "Do you want to save your search "
                                    "connected to a patient name? "
                                    "Type Yes/No: \n").lower()

                if add_patient not in ["yes", "no"]:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "You have not selected a valid option. "
                          "Your answer should be either 'Yes' or 'No'. "
                          "Please resubmit your answer.\n")

            if add_patient.lower() == "yes":
                sheet_name = input(colorama.Style.RESET_ALL +
                                   colorama.Fore.WHITE +
                                   "List patient`s name: \n")
                patients_sheet = SHEET.worksheet("patients_list")
                patients_data = patients_sheet.get_all_records()
                patients_names = [patient['Patient Name']
                                  for patient in patients_data]

                if sheet_name in patients_names:
                    print(
                        colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                        "Patient already has a record. "
                        "Your new search will be appended "
                        "to the existing one.\n")
                    patient_index = patients_names.index(sheet_name)
                    next_search = len(patients_data[patient_index]) + 1
                    patients_sheet.insert_row([], next_search)

                else:
                    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                          "Adding a new patient to your list.\n")
                    patients_sheet.append_row([sheet_name])

                """
                Appends the sheet patient_list
                in the google sheet EssentialOils.
                """

                for oil in matching_oils:
                    oil_data = [sheet_name, oil['Oil Name'], oil['Ailment'],
                                oil['Eur Price'], oil['Diffuser suitable'], oil['Score']]
                    patients_sheet.append_row(oil_data)
                print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                      "Your search was added to your search history.\n")

        else:
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                  "We couldn`t find any result matching "
                  "your search criteria. Please search again.\n")
        new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                           "Do you want to run a new search? Type Yes/No: \n")
        while True:
            if new_search.lower() not in ["yes", "no"]:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                    "You have not selected a valid option. "
                    "Your answer should be either 'Yes' or 'No'. "
                    "Please resubmit your answer.\n")
                new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                "Do you want to run a new search? "
                                "Type Yes/No: \n")
            else:
                break
        """
        Standard functionality across the code
         to allow the user to return to the main menu.
        """
        while True:
            if new_search.lower() != "yes":
                main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                "\nDo you want to exit to main menu? "
                                "Type Yes if you want to return to main. "
                                "Otherwise type No to exit program: \n")
                if main_menu.lower() == "yes":
                    main()
                elif main_menu.lower() == "no":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                        "Now exiting program!\n")
                    exit()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                        "You have not selected a valid option. "
                        "Your answer should be either 'Yes' or 'No'. "
                        "Please resubmit your answer.\n")
            else:
                break

def modify_oil():
    """
    Function to modify existing oil entry.
    """

    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    oil_name = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                     "Enter the name of the oil you want to modify: ").strip()

    existing_oil = None
    for index, oil in enumerate(all_oils, start=2):
        if oil["Oil Name"].lower() == oil_name.lower():
            existing_oil = oil
            existing_oil["row"] = index

    if existing_oil:
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              "\nFollowing entry was found:\n")
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              f"Oil name: {existing_oil['Oil Name']}\nAilment: {existing_oil['Ailment']}"
              f"\nPrice: {existing_oil['Eur Price']}\nCan it be used with a diffuser: {existing_oil['Diffuser suitable']}"
              f"\nScore: {existing_oil['Score']}\n")

        ailment = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                        "Enter the updated ailments the oil addresses: ").strip()
        while True:
            try:
                price = float(input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                    "Enter the updated Euro price value: "))
                break
            except ValueError:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "You have not entered a numeric value. "
                      "Please enter a valid numeric value.")
        while True:
            application = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                "Can it be used with a diffuser? (Yes/No): ").strip().lower()
            if application == "yes" or application == "no":
                break
            else:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "Invalid input. Please enter either 'Yes' or 'No'.")
        score = price / 10 * 0.30 + float(10 if application == "yes" else 0)

        existing_oil["Ailment"] = ailment
        existing_oil["Eur Price"] = price
        existing_oil["Diffuser suitable"] = application
        existing_oil["Score"] = score

        worksheet.update_cell(existing_oil["row"], 2, ailment)
        worksheet.update_cell(existing_oil["row"], 3, price)
        worksheet.update_cell(existing_oil["row"], 4, application)
        worksheet.update_cell(existing_oil["row"], 5, score)

        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              "Oil entry updated successfully:\n")
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              f"Oil name: {existing_oil['Oil Name']}\nAilment: {existing_oil['Ailment']}"
              f"\nPrice: {existing_oil['Eur Price']}\nCan it be used with a diffuser: {existing_oil['Diffuser suitable']}"
              f"\nScore: {existing_oil['Score']}\n")
    else:
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              "The oil was not found in the database.\n")

    main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                      "\nDo you want to return to the main menu? (Yes/No): ").strip()
    if main_menu.lower() == "yes":
        main()
    else:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "Now exiting program!\n")
        exit()


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
        patients_table.append(
            [patient['Patient Name'], patient['Oil Name'],
             patient['Ailment'], patient['Eur Price'],
             patient['Diffuser suitable'], patient['Score']])
    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
          "Here is a list of all your stored patients: \n")
    print(tabulate(patients_table, headers=[
          "Patient Name", "Oil Name",
          "Ailment", "Eur Price",
          "Diffuser suitable", "Score"], tablefmt="grid"))

    """
    Returns to main menu.
    """
    while True:
        main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                        "\nDo you want to exit to main menu? "
                        "Type Yes if you want to return to main. "
                        "Otherwise type No to exit program: \n")
        if main_menu.lower() == "yes":
            main()
        elif main_menu.lower() == "no":
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                "Now exiting program!")
            exit()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                "You have not selected a valid option. "
                "Your answer should be either 'Yes' or 'No'. "
                "Please resubmit your answer.\n")


def search_patient():
    """
    Functions allows the user to search for a patient in the database,
    in the patients_list sheet.
    Function:
        - pulls the data in patients_list
        - takes input from user(takes partial input,
        partial name for example) and returns the result in a table format
        - provides through print lines notifications of different actions
        happening in the program
        - allows the user to re-run new searches once one is complete
        - validates input choices and limits the amount of errors
        for simple decissions: yes or no
    Provides as normal, the option to return to the main menu
    """
    while True:
        worksheet_id = "patients_list"
        worksheet = SHEET.worksheet(worksheet_id)
        all_patients = worksheet.get_all_records()

        """
        Main input section to allow the user to perform a search
        and return a result in table format using tabulate.
        Allows the user to re-run searches if desired.
        """
        search_criteria = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                "Input the name of the patient "
                                "on a First Name "
                                "Second Name format. For example John Doe. "
                                "Please check to make sure "
                                "spelling is correct before hitting ENTER: \n")
        while search_criteria.strip() == "":
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not entered a valid option. "
                  "Please make sure your field is not empty.")
            search_criteria = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                    "Enter the name again and hit enter: ")

        matching_patient = []
        for patient in all_patients:
            if 'Patient Name' in patient and search_criteria.lower().strip() in patient['Patient Name'].lower().strip():
                matching_patient.append(patient)

        if matching_patient:
            patients_table = []
            for patient in matching_patient:
                patients_table.append(
                    [patient['Patient Name'], patient['Oil Name'],
                     patient['Ailment'], patient['Eur Price'],
                     patient['Diffuser suitable'], patient['Score']])
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                  "Here is a list of entries for the patient searched: \n")
            print(tabulate(patients_table, headers=[
                "Patient Name", "Oil Name", "Ailment",
                "Eur Price", "Diffuser suitable", "Score"], tablefmt="grid"))

        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "Your search hasn`t returned any result. "
                  "Please check that the name is spelled "
                  "correctly and search again.\n")
        new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                           "Do you want to run a new search? Type Yes/No: \n")
        while new_search.lower() not in ["yes", "no"]:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "You have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")
            new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                               "Do you want to run a new search? "
                               "Type Yes/No: \n")
        if new_search.lower() != "yes":

            """ Offers user the option to return to main menu"""
            while True:
                main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                                "\nDo you want to exit to main menu? "
                                "Type Yes if you want to return to main. "
                                "Otherwise type No to exit program: \n")
                if main_menu.lower() == "yes":
                    main()
                elif main_menu.lower() == "no":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                        "Now exiting program!\n")
                    exit()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                        "You have not selected a valid option. "
                        "Your answer should be either 'Yes' or 'No'. "
                        "Please resubmit your answer.\n")


def main():
    """
    Main function called at the end of each section
    in order to allow users to return and perform the various
    function/interactions in the program.
    Uses an infinite loop to allow the program to run until terminated.
    Through selected_option it takes the input from user
    in order to identify and return the function the user
    wants to acess

    """

    while True:

        selected_option = list_menu(program_menu)
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              colorama.Style.BRIGHT +
              "\nThe option you have selected: ", selected_option + "\n")

        if selected_option == "1":
            add_oil()
        elif selected_option == "2":
            list_oils()
        elif selected_option == "3":
            find_store_oils()
        elif selected_option == "4":
            modify_oil()
        elif selected_option == "5":
            list_patients()
        elif selected_option == "6":
            search_patient()
        else:
            print(colorama.Style.BRIGHT +
                  "\nThe option you have selected:", selected_option + "\n")


"""
Bellow code set in order to sensure the main functions runs
not only when called inside a function, but also
when the python script is run  python3 run.py.
Took inspiration from:https://realpython.com/if-name-main-python/
"""

if __name__ == "__main__":
    main()
