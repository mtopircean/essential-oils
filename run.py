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

my_oil = Oils()

name = input("Input the name of the oil: ")
ailment = input("Input the ailments the oil addresses by using a , to separate them without a space: ")
price = float(input("Input the price value: "))
application = input("Does it need a difuser(Yes/No): ")
score = price / 100 + (0 if application == "yes" else 1)

my_oil.eo_catalogue(name, ailment, price, application, score)

print(my_oil)