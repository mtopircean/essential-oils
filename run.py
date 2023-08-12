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
    Option is validated as an integer between 1 and 6,
    including 6, and validates the selection.
    Print messages are set to handle all scenarios:
    selected option, wrong type of parameter selected, etc.
    """

    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + "\nOptions Menu:\n")
    for option in menu_options:
        print(option)
    while True:
        selected_option = input(colorama.Style.RESET_ALL +
                                colorama.Fore.WHITE +
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
    Creates a class related to our oils and sets it`s properties.
    It uses 2 functions:
    - eo_catalogue: creates the object related
    to our oils and sets it`s relevant properties
    - str self: which defines in which way
    the added oil is returned, as a string,
    with each line one under the other.
    There are a series of attributes that
    are defined in order to set the main properties
    of this object, which are:
    it`s name, the ailment that it addresses,
    the oil price, if it needs a diffuser to apply it, and
    then a calculated score based on a specific formula.
    """

    def eo_catalogue(self, name, ailment, price, application, score):
        self.name = name
        self.ailment = ailment
        self.price = price
        self.application = application
        self.score = score

    def __str__(self):
        return (f"Oil name: {self.name}"
                f"\nAilment: {self.ailment}"
                f"\nPrice: {self.price}"
                f"\nCan it be used with a Diffuser: {self.application}"
                f"\nScore: {self.score}")


def add_oil():
    """
    It`s main functionality is to add oils to the database.
    This is done by:
    - requesting through inputs to add the name,
    ailment, diffuser application, price;
    note, score is calculated automatically
    - function validates if the oil exists or not,
    and if it exists, recommends to use the modify_oil function
    - validates the data provided for application
    (as yes or no, ignoring upper/lower) and for price
    (number only with . as a separator)
    Function allows to run a loop in order for user to keep
    adding oils if he chooses, through a simple yes or no input.
    If user doesn`t want to add another product, the loop will
    trigger the option to return to main menu,
    with a yes or no selection.
    Each oil added is populated into the "master"
    sheet in the google sheets called EssentialOils.
    """

    my_oil = Oils()

    while True:
        name = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                     "\nInput the name of the oil: \n").strip()
        if name:
            break
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not entered a valid name. "
                  "Please provide a name for the oil. "
                  "Please make sure you are not leaving the field empty.\n")
    try:
        worksheet_id = "master"
        worksheet = SHEET.worksheet(worksheet_id)
        all_oils = worksheet.get_all_records()
    except Exception as e:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "\nAn error occurred while connecting to the database. "
              "Please contact the administrator related "
              "to following function: \n", str(e))
        main()
        return

    """
    Section dedicated to checks if oil already exists in database
    or not.
    """

    for oil in all_oils:
        if oil["Oil Name"].lower().strip() == name.lower().strip():
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nThe oil already exists in the database. "
                  "If you want to modify the oil, "
                  "use the Modify oil data function.")
            ailment = oil["Ailment"]
            price = oil["Eur Price"]
            application = oil["Diffuser suitable"]
            score = oil["Score"]
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE + "\n" +
                  (f"Oil name: {name}"
                   f"\nAilment: {ailment}"
                   f"\nPrice: {price}"
                   f"\nCan it be used with a diffuser: {application}"
                   f"\nScore: {score}"))
            while True:
                re_run = input(colorama.Style.RESET_ALL +
                               colorama.Fore.WHITE +
                               "\nDo you want to add another "
                               "product to the database? "
                               "Type Yes or No: \n")
                if re_run.lower() == "no":
                    while True:
                        main_menu = input(colorama.Style.RESET_ALL +
                                          colorama.Fore.WHITE +
                                          "\nDo you want to exit "
                                          "to main menu? "
                                          "Type Yes if you want "
                                          "to return to main. "
                                          "Otherwise type No "
                                          "to exit program: \n")
                        if main_menu.lower() == "yes":
                            main()
                        elif main_menu.lower() == "no":
                            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                                  "\nNow exiting program!\n")
                            exit()
                        else:
                            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                                  "\nYou have not selected a valid option. "
                                  "Your answer should "
                                  "be either 'Yes' or 'No'. "
                                  "Please resubmit your answer.\n")
                elif re_run.lower() == "yes":
                    add_oil()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not selected a valid option. "
                          "Your answer should be either 'Yes' or 'No'. "
                          "Please resubmit your answer.\n")
    while True:
        ailment = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                        "\nInput the ailments the oil addresses. "
                        "We recommend a format in which, "
                        "if multiple ailments, "
                        "separate them by ',' and space. "
                        "For example: headache, toothache. "
                        "Please provide your input: \n").strip()
        if ailment:
            break
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not entered a valid name. "
                  "Please provide a name for the oil. "
                  "Please make sure you are not leaving the field empty.\n")
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
                            "\nCan it be used "
                            "with a Diffuser?(Yes/No): \n").strip()
        if application.lower() == "yes" or application.lower() == "no":
            break
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")
    score = round(price / 10 * 0.30 +
                  float(10 if application.lower() == "yes" else 0), 2)
    """
    Adds the oil to database and updates the master sheet.
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
    Loop created to give the user an option to keep adding oils
    before returning to main menu.
    It also does a basic validation of their choices,
    limiting user to a yes or no option.
    """
    while True:
        re_run = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                       "\nDo you want to add another product to the database? "
                       "Type Yes or No: \n")
        if re_run.lower() == "no":
            while True:
                main_menu = input(colorama.Style.RESET_ALL +
                                  colorama.Fore.WHITE +
                                  "\nDo you want to exit to main menu? "
                                  "Type Yes if you want to return to main. "
                                  "Otherwise type No to exit program: \n")
                if main_menu.lower() == "yes":
                    main()
                elif main_menu.lower() == "no":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nNow exiting program!\n")
                    exit()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not selected a valid option. "
                          "Your answer should be either 'Yes' or 'No'. "
                          "Please resubmit your answer.\n")
                    continue
        elif re_run.lower() == "yes":
            add_oil()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")


def update_oils_worksheet(data, worksheet):
    """
    Function created to update the sheet named master in
    the EssentialOils google sheet.
    Function:
    - informs on updates being made to the sheet
    - sets the area where the data is transferred to the master sheet,
    always being the next row, this is done by reading it`s row length
    and adding the data to the next unoccupied line
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
    - using tabulate it then prints the result into a grid table format
    As all functions, it then gives the user an option to jump to main menu.

    Note: Tabulate how to install and use
    is inspired from: https://pypi.org/project/tabulate/.
    """
    try:
        worksheet_id = "master"
        worksheet = SHEET.worksheet(worksheet_id)
        all_oils = worksheet.get_all_records()
    except Exception as e:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "\nAn error occurred while connecting to the database. "
              "Please contact the administrator related "
              "to following function: \n", str(e))
        main()
        return

    oils_table = []
    for oil in all_oils:
        oils_table.append([oil['Oil Name'],
                           oil['Ailment'],
                           oil['Eur Price'],
                           oil['Diffuser suitable'],
                           oil['Score']])

    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
          "Here is a list of all your stored oils: \n")
    print(tabulate(oils_table, headers=[
          "Oil Name",
          "Ailment",
          "Eur Price",
          "Diffuser suitable",
          "Score"],
        tablefmt="grid"))
    while True:
        main_menu = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                          "\nDo you want to exit to main menu? "
                          "Type Yes if you want to return to main. "
                          "Otherwise type No to exit program: \n")
        if main_menu.lower() == "yes":
            main()
        elif main_menu.lower() == "no":
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nNow exiting program!\n")
            exit()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")


def find_store_oils():
    """
    Function created to allow user to search over
    the database and retrieve an oil based on either a name or ailment.
    It is designed so it accepts partial parts
    of the words, in order to give flexibility and allow the user to limit
    their mistakes to a minimum.
    It also gives the option to store the search under a patient name
    so it can then return the search history in search or list_patient
    function.
    Function:
    - retrieves stored data
    - allows user to search by either name of ailment
    - validates and returns a result if it exists,
    else it prints that no record exists
    - give the option to run a new search
    - gives the option to create a patient record
    of the search or not, through a yes / no validation
    - appends the data to an existing patient,
    if patient already exists or creates a new one
    - once user stops it`s search activity can always return to main menu
    """
    try:
        worksheet_id = "master"
        worksheet = SHEET.worksheet(worksheet_id)
        all_oils = worksheet.get_all_records()
    except Exception as e:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "\nAn error occurred while connecting to the database. "
              "Please contact the administrator related "
              "to following function: \n", str(e))
        main()
        return

    """
    Search related code section with tabulate styling for returned result.
    """

    while True:
        search_criteria = input(colorama.Style.RESET_ALL +
                                colorama.Fore.WHITE +
                                "\nInput the name of the oil "
                                "or the ailment you need to address: \n")
        if not search_criteria:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not entered a valid option. "
                  "Please make sure your field is not empty.\n")
            continue

        matching_oils = []
        for oil in all_oils:
            if 'Oil Name' in oil and search_criteria.lower().strip() in oil['Oil Name'].lower().strip():  # noqa
                matching_oils.append(oil)
            elif 'Ailment' in oil and search_criteria.lower() in oil['Ailment'].lower():  # noqa
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
                                    "\nDo you want to save your search "
                                    "connected to a patient name? "
                                    "Type Yes/No: \n").lower()

                if add_patient not in ["yes", "no"]:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not selected a valid option. "
                          "Your answer should be either 'Yes' or 'No'. "
                          "Please resubmit your answer.\n")

            if add_patient.lower() == "yes":
                sheet_name = input(colorama.Style.RESET_ALL +
                                   colorama.Fore.WHITE +
                                   "List patient`s name: \n").lower()
                if sheet_name == "":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not entered a valid name. "
                          "Please provide a patient name. "
                          "Please make sure you are not "
                          "leaving the field empty.\n")
                    continue
                patients_sheet = SHEET.worksheet("patients_list")
                patients_data = patients_sheet.get_all_records()
                patients_names = [patient['Patient Name'].lower()
                                  for patient in patients_data]

                if sheet_name.lower() in patients_names:
                    print(
                        colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                        "Patient already has a record. "
                        "Your new search will be appended "
                        "to the existing one.\n")
                    last_row_for_patient = None
                    for patient_row, patient_data in enumerate(patients_data):
                        if patient_data['Patient Name'].lower() == sheet_name.lower():  # noqa
                            last_row_for_patient = patient_row + 2
                    if last_row_for_patient is not None:
                        insert_at_row = last_row_for_patient + 1
                        while insert_at_row - 2 < len(patients_data) and patients_data[insert_at_row - 2]['Patient Name'] == sheet_name:  # noqa
                            insert_at_row += 1
                    for oil in matching_oils:
                        oil_data = [sheet_name, oil['Oil Name'],
                                    oil['Ailment'], oil['Eur Price'],
                                    oil['Diffuser suitable'], oil['Score']]
                        patients_sheet.insert_row(oil_data, insert_at_row)
                        insert_at_row += 1

                else:
                    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                          "Adding a new patient to your list.\n")
                    patients_sheet.append_row([sheet_name])

                    """
                    Appends the sheet patient_list
                    in the google sheet EssentialOils.
                    """

                    for oil in matching_oils:
                        oil_data = [sheet_name, oil['Oil Name'],
                                    oil['Ailment'],
                                    oil['Eur Price'],
                                    oil['Diffuser suitable'],
                                    oil['Score']]
                        patients_sheet.append_row(oil_data)
                    print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                          "\nYour search was added to your search history.\n")

        else:
            print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                  "We couldn`t find any result matching "
                  "your search criteria. Please search again.\n")
        new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                           "\nDo you want to run a new search? "
                           "Type Yes/No: \n")
        while True:
            if new_search.lower() not in ["yes", "no"]:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "\nYou have not selected a valid option. "
                      "Your answer should be either 'Yes' or 'No'. "
                      "Please resubmit your answer.\n")
                new_search = input(colorama.Style.RESET_ALL +
                                   colorama.Fore.WHITE +
                                   "\nDo you want to run a new search? "
                                   "Type Yes/No: \n")
            else:
                break
        """
        Standard functionality across the code
         to allow the user to return to the main menu.
        """
        while True:
            if new_search.lower() != "yes":
                main_menu = input(colorama.Style.RESET_ALL +
                                  colorama.Fore.WHITE +
                                  "\nDo you want to exit to main menu? "
                                  "Type Yes if you want to return to main. "
                                  "Otherwise type No to exit program: \n")
                if main_menu.lower() == "yes":
                    main()
                elif main_menu.lower() == "no":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nNow exiting program!\n")
                    exit()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not selected a valid option. "
                          "Your answer should be either 'Yes' or 'No'. "
                          "Please resubmit your answer.\n")
            else:
                break


def modify_oil():
    """
    Function to modify existing oil entry.
    It pull data from master sheet and identifies existing oil.
    It then returns the values stored under the oil name in
    order to give then the user an option to start changes in
    a controlled manner.
    Then returns again the new result and updates master on the
    specific line where the oil exists, by replacing the content
    of it`s parameters.
    If no oil is identified, user can run a new search or return
    to main menu.
    """
    try:
        worksheet_id = "master"
        worksheet = SHEET.worksheet(worksheet_id)
        all_oils = worksheet.get_all_records()
    except Exception as e:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "\nAn error occurred while connecting to the database. "
              "Please contact the administrator related "
              "to following function: \n", str(e))
        main()
        return
    oil_name = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                     "\nEnter the name of the oil "
                     "you want to modify: ").strip()
    existing_oil = None
    for index, oil in enumerate(all_oils, start=2):
        if oil["Oil Name"].lower() == oil_name.lower():
            existing_oil = oil
            existing_oil["row"] = index
    if existing_oil:
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              "\nFollowing entry was found:\n")
        print(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
              (f"Oil name: {existing_oil['Oil Name']}"
               f"\nAilment: {existing_oil['Ailment']}"
               f"\nPrice: {existing_oil['Eur Price']}"
               f"\nCan it be used with a diffuser: "
               f"{existing_oil['Diffuser suitable']}"
               f"\nScore: {existing_oil['Score']}\n"))
        ailment = input(colorama.Style.RESET_ALL +
                        colorama.Fore.WHITE +
                        "\nEnter the updated ailments "
                        "the oil addresses: \n").strip()
        while True:
            try:
                price = float(input(colorama.Style.RESET_ALL +
                                    colorama.Fore.WHITE +
                                    "\nEnter the updated Euro "
                                    "price value: \n"))
                break
            except ValueError:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "\nYou have not entered a numeric value. "
                      "Please enter a valid numeric value.\n")
        while True:
            application = input(colorama.Style.RESET_ALL +
                                colorama.Fore.WHITE +
                                "\nCan it be used with a diffuser? "
                                "(Yes/No): \n").strip().lower()
            if application == "yes" or application == "no":
                break
            else:
                print(colorama.Fore.RED + colorama.Style.BRIGHT +
                      "Invalid input. Please enter either 'Yes' or 'No'.")
        score = round(price / 10 * 0.30 +
                      float(10 if application.lower() == "yes" else 0), 2)
        """
        Updates master document with the new oil parameters
        """

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
              (f"Oil name: {existing_oil['Oil Name']}\n"
               f"Ailment: {existing_oil['Ailment']}"
               f"\nPrice: {existing_oil['Eur Price']}\n"
               f"Can it be used with a diffuser: "
               f"{existing_oil['Diffuser suitable']}"
               f"\nScore: {existing_oil['Score']}\n"))
    else:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "The oil was not found in the database. "
              "Ensure that you have typed the full correct name.\n")

    """
    Allows the user to run a new search or return to main menu
    """

    while True:
        re_search = input(colorama.Style.RESET_ALL +
                          colorama.Fore.WHITE +
                          "\nDo you want to modify another product. "
                          "Type in Yes or No: ").strip()
        if re_search.lower() == "yes":
            modify_oil()
        elif re_search.lower() == "no":
            while True:
                main_menu = input(colorama.Style.RESET_ALL +
                                  colorama.Fore.WHITE +
                                  "\nIf you want to return to main menu, "
                                  "type in Yes. Otherwise, "
                                  "type No to exit program: \n").strip()
                if main_menu.lower() == "yes":
                    main()
                elif main_menu.lower() == "no":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nNow exiting program!\n")
                    exit()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not selected a valid option. "
                          "Your answer should be either 'Yes' or 'No'. "
                          "Please resubmit your answer.\n")
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")


def list_patients():
    """
    Function created in order to allow user to list the patients database.
    Function:
        - pulls all records
        - presents data in a table format using tabulate
    Offers again the option to exit to main menu.
    As all functions validates data input to limit error.
    """
    try:
        worksheet_id = "patients_list"
        worksheet = SHEET.worksheet(worksheet_id)
        all_patients = worksheet.get_all_records()
    except Exception as e:
        print(colorama.Fore.RED + colorama.Style.BRIGHT +
              "\nAn error occurred while connecting to the database. "
              "Please contact the administrator related "
              "to following function: \n", str(e))
        main()
        return

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
            print(colorama.Fore.RED +
                  colorama.Style.BRIGHT +
                  "\nNow exiting program!")
            exit()
        else:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
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
    for simple decisions: yes or no
    Provides as normal, the option to return to the main menu.
    """
    while True:
        try:
            worksheet_id = "patients_list"
            worksheet = SHEET.worksheet(worksheet_id)
            all_patients = worksheet.get_all_records()
        except Exception as e:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nAn error occurred while connecting to the database. "
                  "Please contact the administrator related "
                  "to following function: \n", str(e))
            main()
            return

        """
        Main input section to allow the user to perform a search
        and return a result in table format using tabulate.
        Allows the user to re-run searches if desired.
        """
        search_criteria = input(colorama.Style.RESET_ALL +
                                colorama.Fore.WHITE +
                                "\nInput the name of the patient "
                                "on a First Name "
                                "Second Name format. For example John Doe. "
                                "Please check to make sure "
                                "spelling is correct before hitting ENTER: \n")
        while search_criteria.strip() == "":
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not entered a valid option. "
                  "Please make sure your field is not empty.\n")
            search_criteria = input(colorama.Style.RESET_ALL +
                                    colorama.Fore.WHITE +
                                    "\nEnter the name again and hit enter: ")

        matching_patient = []
        for patient in all_patients:
            if 'Patient Name' in patient and search_criteria.lower().strip() in patient['Patient Name'].lower().strip():  # noqa
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
                  "\nYour search hasn`t returned any result. "
                  "Please check that the name is spelled "
                  "correctly and search again.\n")
        new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                           "\nDo you want to run a new search? "
                           "Type Yes/No: \n")
        while new_search.lower() not in ["yes", "no"]:
            print(colorama.Fore.RED + colorama.Style.BRIGHT +
                  "\nYou have not selected a valid option. "
                  "Your answer should be either 'Yes' or 'No'. "
                  "Please resubmit your answer.\n")
            new_search = input(colorama.Style.RESET_ALL + colorama.Fore.WHITE +
                               "\nDo you want to run a new search? "
                               "Type Yes/No: \n")
        if new_search.lower() != "yes":

            """ Offers user the option to return to main menu"""
            while True:
                main_menu = input(colorama.Style.RESET_ALL +
                                  colorama.Fore.WHITE +
                                  "\nDo you want to exit to main menu? "
                                  "Type Yes if you want to return to main. "
                                  "Otherwise type No to exit program: \n")
                if main_menu.lower() == "yes":
                    main()
                elif main_menu.lower() == "no":
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nNow exiting program!\n")
                    exit()
                else:
                    print(colorama.Fore.RED + colorama.Style.BRIGHT +
                          "\nYou have not selected a valid option. "
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
    wants to access.
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
Bellow code set in order to ensure the main functions runs
not only when called inside a function, but also
when the python script is run.
Took inspiration from: https://realpython.com/if-name-main-python/
"""

if __name__ == "__main__":
    main()
