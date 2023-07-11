import gspread
from google.oauth2.service_account import Credentials

import colorama

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
                "3. Search a product in the database", "4. Print patient database", "5. Search patient file")

search_menu = ("1. Search by Name:", "2. Search by ailment")


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
    price = float(input("Input the price value: "))
    application = input("Does it need a difuser(Yes/No): ")
    score = price / 100 + (0 if application == "yes" else 1)

    my_oil.eo_catalogue(name, ailment, price, application, score)
    print(f"You added {my_oil.name} to the database")
    print(my_oil)
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

    for oil in all_oils:
        print("Here is a list of all your stored oils:")
        print(oil)
        print()
        print("Do you want to select another option from the main menu?")
        print()


def find_store_oils():
    """
    Find multiple oils in the database.
    """
    def search_menu(search_options):
        print("Search Menu:")
        for option in search_options:
            print(option)
        while True:
            selected_option = input(
                "What do you want to do? Add the number of your option without any other characters:")
            if selected_option.isdigit() and 1 <= int(selected_option) <= 2:
                return selected_option
            else:
                print(
                    "You haven`t selected a valid option. Please select a value from 1 to 2 based on the options menu list.")

    worksheet_id = "master"
    worksheet = SHEET.worksheet(worksheet_id)
    all_oils = worksheet.get_all_records()

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
        for oil in matching_oils:
            print(oil)

        worksheet_id_two = "search_history"
        worksheet_two = SHEET.worksheet(worksheet_id_two)
        next_search = len(worksheet.get_all_values()) - 2
        for oil in matching_oils:
            oil_data = [oil['Oil Name'], oil['Ailment'], oil['Price'], oil['Application'], oil['Score']]
            worksheet_two.insert_row(oil_data, next_search)
            next_search += 1
        print("Your search was added to your search history")

    else:
        print("we couldn`t find any result matching your search criteria.")


def list_patient():
    """
    List your patient records.
    """


def find_patient():
    """
    Find a patient.
    """


selected_option = list_menu(program_menu)
print("The option you have selected:", selected_option)

if selected_option == "1":
    my_oil = add_oil()
    if my_oil is not None:
        data = [my_oil.name, my_oil.ailment, my_oil.price,
                my_oil.application, my_oil.score]
        update_oils_worksheet(data, "master")
elif selected_option == "2":
    list_oils()
elif selected_option == "3":
    find_store_oils()
elif selected_option == "4":
    list_patient()
elif selected_option == "5":
    find_patient()
else:
    print("The option you have selected:", selected_option)
