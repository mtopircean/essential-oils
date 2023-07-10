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


def list_menu(menu_options):
    print("Options Menu:")
    for option in menu_options:
        print(option)
    select_option = input(
        "What do you want to do? Add the number of your option without any other characters:")
    return select_option


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
    print("You added {name} to the database")
    print(my_oil)


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


selected_option = list_menu(program_menu)
print("The option you have selected:", selected_option)

if selected_option == "1":
    add_oil()
elif selected_option == "2":
    pass
elif selected_option == "3":
    pass
elif selected_option == "4":
    pass
elif selected_option == "5":
    pass
else:
    print("You haven`t selected any of the options available. Please try again one of the options listed above.")
    return selected_option


data = [my_oil.name, my_oil.ailment, my_oil.price,
        my_oil.application, my_oil.score]
update_oils_worksheet(data, "master")
