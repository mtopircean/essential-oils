import gspread
from google.oauth2.service_account import Credentials

import colorama
from tabulate import tabulate

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
    print("Options Menu:")
    for option in menu_options:
        print(option)
    while True:
        selected_option = input(
            "What do you want to do? Add the number of your option without any other characters:")
        if selected_option.isdigit() and 1 <= int(selected_option) <= 5:
            return selected_option
        else:
            print("You haven`t selected a valid option. Please select a value from 1 to 5 based on the options menu list.")


class Oils:
    """
    Oils class
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
    my_oil = Oils()
    name = input("Input the name of the oil: ")
    ailment = input(
        "Input the ailments the oil addresses by using a , to separate them without a space: ")
    while True:
        try:
            price = float(input("Input the price value: "))
            break
        except ValueError:
            print("You have not entered a number value. Please write resubmit your answer. Do not use a ',' to separate the decimals, use instead a '.'.")

    while True:
        application = input("Does it need a difuser(Yes/No): ")
        if application.lower() == "yes" or application.lower() == "no":
            break
        else:
            print("You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")

    score = price / 100 + (0 if application == "yes" else 1)

    my_oil.eo_catalogue(name, ailment, price, application, score)
    print(f"You added {my_oil.name} to the database")
    print(my_oil)

    data = [my_oil.name, my_oil.ailment, my_oil.price,
                my_oil.application, my_oil.score]
    update_oils_worksheet(data, "master")

    while True:
        return_menu = input(
            "Do you want to return to the main menu? Type Yes or No. If you type No, you will completley exit the program.")
        if return_menu.lower() == "no":
            print("Program is now exiting!")
            return my_oil
        else:
            option_selection = list_menu(program_menu)
            break
        return my_oil


def update_oils_worksheet(data, worksheet):
    """
    Update excel sheet tab named master.
    """
    print(f"Updating {worksheet}.")
    worksheet_master = SHEET.worksheet(worksheet)
    following_row = len(worksheet_master.get_all_values()) + 1

    oil_data = [data[0], data[1], data[2], data[3], data[4]]
    worksheet_master.insert_row(oil_data, following_row)

    print(f"{worksheet} updated.")


def list_oils():
    """
    Pull database of oils from worksheet.
    """
    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    oils_table = []
    for oil in all_oils:
        oils_table.append([oil['Oil Name'], oil['Ailment'],
                          oil['Price'], oil['Application'], oil['Score']])

    print("Here is a list of all your stored oils:")
    print(tabulate(oils_table, headers=[
          "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))

    return_menu = input(
        "Do you want to return to the main menu? Type Yes or No. If you type No, you will completley exit the program.")
    if return_menu == "Yes":
        list_menu(program_menu)

        return list_oils


def find_store_oils():
    """
    Find multiple oils in the database.
    """

    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

    while True:
        search_criteria = input(
            "Input the name of the oil or the ailment you need to address: ")

        matching_oils = []
        for oil in all_oils:
            if 'Oil Name' in oil and search_criteria.lower() in oil['Oil Name'].lower():
                matching_oils.append(oil)
            elif 'Ailment' in oil and search_criteria.lower() in oil['Ailment'].lower():
                matching_oils.append(oil)

        if matching_oils:
            print("Please find bellow your search result:")
            search_table = []
            for oil in matching_oils:
                search_table.append([oil['Oil Name'], oil['Ailment'],
                                     oil['Price'], oil['Application'], oil['Score']])

            print("Here is your search result:")
            print(tabulate(search_table, headers=[
                "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))
            
            add_patient = None
            while add_patient not in ["yes", "no"]:
                add_patient = input("Do you want to save your search connected to a patient name? Type Yes/No: ").lower()

                if add_patient not in ["yes", "no"]:
                    print("You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")
            
            if add_patient.lower() == "yes":

                sheet_name = input(
                    "List patient`s name:")
                patients_sheet = SHEET.worksheet("patients_list")
                patients_data = patients_sheet.get_all_records()
                patients_names = [patient['Patient Name']
                                  for patient in patients_data]

                if sheet_name in patients_names:
                    print(
                        "Patient already has a record. Your new search will be appended to the existing one.")
                    patient_index = patients_names.index(sheet_name)
                    next_search = len(patients_data[patient_index]) + 1
                    patients_sheet.insert_row([], next_search)

                else:
                    print("Adding a new patient to your list.")
                    patients_sheet.append_row([sheet_name])

                for oil in matching_oils:
                    oil_data = [sheet_name, oil['Oil Name'], oil['Ailment'],
                                oil['Price'], oil['Application'], oil['Score']]
                    patients_sheet.append_row(oil_data)
                print("Your search was added to your search history")

        else:
            print(
                "We couldn`t find any result matching your search criteria. Please search again")
        
        new_search = input("Do you want to run a new search? Type Yes/No: ")
        while new_search.lower() not in ["yes", "no"]:
            print("You have not selected a valid option. Your answer should be either 'Yes' or 'No'. Please resubmit your answer.")
            new_search = input("Do you want to run a new search? Type Yes/No: ")
        if new_search.lower() != "yes":
            break


def list_patients():
    """
    Search a patient.
    """
    worksheet_id = "patients_list"
    worksheet = SHEET.worksheet(worksheet_id)
    all_patients = worksheet.get_all_records()

    patients_table = []
    for patient in all_patients:
        patients_table.append([patient['Patient Name'], patient['Oil Name'],
                              patient['Ailment'], patient['Price'], patient['Application'], patient['Score']])

    print("Here is a list of all your stored patients:")
    print(tabulate(patients_table, headers=[
          "Patient Name", "Oil Name", "Ailment", "Price", "Application", "Score"], tablefmt="grid"))


def search_patient():
    """
    Search a patient.
    """
    worksheet_id = "patients_list"
    worksheet = SHEET.worksheet(worksheet_id)
    all_patients = worksheet.get_all_records()

    search_criteria = input(
        "Input the name of the patient on a First Name Second Name format. For example John Doe. Please check to make sure spelling is correct before hitting ENTER: ")
    matching_patient = []
    found_patient = False
    for patient in all_patients:
        if 'Patient Name' in patient and search_criteria.lower() in patient['Patient Name'].lower():
            matching_patient.append(patient)
            found_patient = True
        else:
            pass
    if found_patient:
        for patient in matching_patient:
            print(patient, end="\n")
    else:
        print("Your search hasn`t returned any result. Please check that the name is spelled correctly and search again.")


selected_option = list_menu(program_menu)
print("The option you have selected:", selected_option)

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
    print("The option you have selected:", selected_option)
