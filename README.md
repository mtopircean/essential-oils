# EssentialOils

EssentialOils was born out of my wife`s necessity for a CRM - Client Relationship Management / Product Management system that would offer her support in her journey of understanding EssentialOils, and even more, in providing support to different people requiring guidance and support in finding natural and alternative solutions to different ailments.

## CONTENT
* [Scope](#scope)
* [User Stories](#user-stories)
* [Deployment](#deployment-and-local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Technologies used](#technologies-used)
    * [Programming Languages](#programming-languages)
    * [IDE](#ide)
    * [Other](#other)
* [Design](#design)
    * [FlowChart](#FlowChart)
    * [Theme](#theme)
    * [Colour Selection](#colour-selection)
    * [Features](#features)
* [Testing and Validation](#testing-and-validation)
    * [CI Linter](#ci-linter)
    * [Spellcheck](#spellcheck)
    * [Python](#python)
    * [Local functionality tests](#local-functionality-tests)
    * [Fixed bugs and known errors](#fixed-bugs-and-current-errors)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Other Credits](#other-credits)
* [About Author](#about-author)

## Scope
Essential oils application offers the user a simple Client Relationship Management and Product Management System.
Application allows the user to enter/pull through a basic Python interface data into/from a Google Spreadsheet, update product data and maintain a search history database based on customer name.
The true value of this application represents this exact functionality, the ability to store searches into a database, allocating them to a specific customer. This allows then the user to go back to their data and tailor their discussions in a way that maximizes the impact they can bring to address clients ailments.
The ability to store the search as it happens is what it brings more value compared to using a simple spreadsheet.


##  User Stories

CURRENT STATE:

Intention of the application is to allow the user to:
- access a main menu that will allow them to create, update and manipulate data
- create a database by having the ability to add the products into a database link to a google spreadsheet
- update an existing product
- list the product database into a table format
- search through the database in order to pull a specific product by using the product name or ailment, in a way that does not restrict the user to use fixed and accurate names of the oil and ailment; user can search by part of the word, using upper or lower case
- save the search under a patient name in order to be able to store the data in real time and be able to create a patient sheet that will later allow the user to take a very targeted approach with the customer
- search the patient database, again, without major limitations, similar to the search system for product
- access easily a patients file

FUTURE STATE:

Future plan for the application is to extend the level of data that can be stored, accessed and modified.
It should also offer the user the ability to have more flexibility in what they are using as search criteria, together with filtering options.
For patients listing, it will include more details on when the search has taken place and allow to store users personal data as the discussions/searches happen, data like date of birth, gender, contact details.

## Deployment and Local Development
Deployment of the website was done using HEROKU, and can be accessed here [ESSENTIALOILS](https://essential-oils-8a5b724d8c2a.herokuapp.com/).
To access the google sheet linked to this project, please use this link [EssentialOilsGoogle](https://tinyurl.com/yc7m7257).
The steps in deployment in Heroku where taken following the example of LoveSandwiches CI Project.

#### How to Fork
To fork the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mtopircean/essential-oils](https://github.com/mtopircean/essential-oils)
3. Click the Fork button in the top right corner.

#### How to Clone
To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mtopircean/essential-oils](https://github.com/mtopircean/essential-oils)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


## Technologies Used

#### Programming Languages:
1. Python


#### IDE:
1. GitHub: to store the source code.
2. GitPod: support to write majority of code, deploy via Heroku, and push data to store in GitHub. Gitpod was used also for debugging purposes.

#### Other:
1. HEROKU: to deploy application and act as the app interface
2. CI Python Linter: to validate code format.
3. draw.io: to create flow diagram.

## Design
Design is very basic and limited to Python/Heroku interfaces.
There was a separation of data based on their purpose and intention by using colorama.
The use of tabulate and font styles was done in order to structure the data in a manner easy to read and understand.

#### FlowChart
FlowChart was established at the beginning of the project as it was an absolute requirement in order to ensure that all of the different features and interconnections between different functionalities where executed.
It has supported in a few instances in identifying a lack of logic, or a dead end in a function.
![Alt text](/readme/images/flow-diagram.jpg)

[FLOWCHART PRESENT ALSO AT THIS LINK DUE TO IT`S LARGE SIZE AND COMPLEXITY:](https://github.com/mtopircean/essential-oils/blob/main/readme/images/flow%20-diagram.jpg)


#### Theme
Even with the interface limitations, I`ve tried to create and maintain a database theme by using tabulate in order to return the data in a more pleasant, easy to follow way.
The use of different colours and font highlight was done to create structure and an ease in understanding and reading the different messages returned by the app.
![Alt text](/readme/images/tabulate.jpg)


#### Colour Selection
- Red: alert
- Cyan: Menu
- White: for everything else in order to add a contrast to HEROKU background
![Alt text](/readme/images/color-scheme.jpg)


#### Features

A. External Features Implemented:

-  Tabulate add-on implemented in order to provide a more graphical representation of the database and allow user to easily read and understand data.

![Alt text](/readme/images/tabulate.jpg)

-  Colorama was used in highlighting key messages on the screen:
    *** Errors by using red
    *** Cyan for highlighting the menu
    *** White for standard information

![Alt text](/readme/images/color-scheme.jpg)

- Connection to google sheet created in order to pull and push data to the main database by accessing 2 sheets, "master" and "patients_list"

![Alt text](/readme/images/google-sheet.jpg)


B. Overall view on features present in the application:

* General:
Document is structured around a main menu that allows the user to navigate through the different functionalities of the program. Throughout the program, the user, after finishing running a feature, is allowed to return again to main menu.
This was thought in order to give the user a continuous loop through the code and improve it`s experience by removing unnecessary steps.

User is provided guidance throughout the program in order to make sure it is easy to understand and use.

* Maine menu:
The main menu is the centre point of the application connecting the various functions to a centre of command.
I`ve allowed for it to run automatically when the script is loaded, to again, limit the users effort in accessing the tools functionality. Functionality achieved through the use of the code bellow:

```python
if __name__ == "__main__":
    main()
```

I`ve also chose to separate it from the rest of the code visually by using CYAN colour, dedicated only to this section.

Main menu is providing access to 6 main function:
    1. Add a product to the database
    2. List oils database
    3. Search a product in the database
    4. Modify oil data
    5. List patients database
    6. Search patient in the database

1. Add a product to the database(``add_oil()``):
* Main functionality of this feature is to allow the user to add a product to the database by inputting specific parameters.
It also calculates a specific score which is returned in the same database in order to offer a comparison between the different products.
* If an oil already exists when trying to enter the product, the user will be prompted that the product is already present in the database, and it will recommend to use the Modify oil data function if the choice will be to modify it`s parameters.
* Throughout the function, the user is left with choices to jump through different functionalities, in order to make sure there aren`t any closed loops.
* Error checks are also present to ensure that parameters are entered, or that the correct parameters are entered, like for example:
    * No empty strings for oil name and ailment
    * Yes and No where required, and no other option; implemented considering validation ignoring lower/upper case use
    * Use of numeric only characters for price input
* Function, through a link to update_oils_worksheet() function will connect and update the relevant google sheet

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/add-oil-function.gif)

2. List oils database(``list_oils()``):
* Functionality relates to the option of a user to list all of the oils present in the database.
* By using tabulate, user is able to view the information in a manner easier to read and understand.
* Similar to the rest of the functions, in order to allow an open loop when running the function, user can then return to main menu.

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/list-oils.gif)

3. Search a product in the database(``find_store_oils()``):
* By using this function the user is able to search for a product in the database either by it`s product name or ailment. In order to improve user experience and allow the user to make less mistake, function will return a result even if the user will enter the name of the oil or ailment partially. For example, using "Laven" instead of "Lavender", will return a result for all the products including "Laven" in either the name or ailment.
* Search result is returned in a tabulate format.
* An extra functionality of the feature, which brings true value to the application vs. using a standard excel/worksheet solution, is the ability to save the search under a patient name. The search is then saved under the patients name in a specific sheet so it can be returned in the other functions which will search and list the patients. This allows the user to take real time snapshots of their discussion with a patient and be able to access the data later and reference in a new contact with the client. 
Patient list is separate by the actual name of the patient. This is done so it allows the user to better read the data with a clearer separation between patients:
![Alt text](/readme/images/patient-list.jpg)

* Similar to the other functions, checks are in place to validate the data entered.
* Similar to other functions, an open loop exists so that the user can return to the main menu.

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/search-oil.gif)

4. Modify oil data(``modify_oil()``):
* Function added later in the development with the goal to allow the user to update the existing data on an already present entry in the product database.
* It is applicable only to oils and does not allow updates on the patients database.
* User is allowed to search in the database, if an entry is found data is returned to the user so we have reference it when the parameters will be entered with the new data. Limitation here relates to the fact that the user has to re-enter each parameter. Upgrade in the future will be to enter a numeric option related to a list including all of the parameters.
* If the entry does not exist, user is asked if a new resubmit is needed and then the loop can be closed again with an exit program or return to main menu.
* Function then identifies the entry in the external worksheet and updates that entry
* Like the other functions, data validation is present here as well.
* The open loops are in place in order to allow the user to move with ease through the function

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/modify-oil.gif)

5. List patients database(``list_patients()``):
* Similar to the list_oils function, the list_patients function will return a list of all the patients existing in the patients_list sheet.
* Data is returned in a table format by using tabulate
* Open loop is existent also here in order to allow the user to return to main menu or terminate program
* Data validation also present, where required

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/list-patients.gif)

6. Search patient in the database(``search_patient()``)
* Similar to the function allowing to search for a product, this function allows the user to search a patient in the database
* Result is returned in table format using tabulate
* User can input partially the name of the patient and still be able to return the results containing it. This was chosen vs. a fixed and strict use of the exact name in order to allow more flexibility to the user and less room for error.

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/search-patient.gif)

## Testing and Validation

#### Spellcheck

Spellcheck was run using word spellcheck validation option.
All found spelling errors where corrected in order to give the user a clean experience when using the tool.

#### CI Linter

Code was tested by using the CI Linter web application.
No issues where identified except the ones bellow which where not addressed as they would have required for the code to be re-written. Due to the advanced state of the project and due to the fact that changing the code could have impacted the integrity and stability of the code/.

Linter test:

![Alt text](/readme/images/linter.jpg)

```python
if 'Patient Name' in patient and search_criteria.lower().strip() in patient['Patient Name'].lower().strip():
```

```python
elif 'Ailment' in oil and search_criteria.lower() in oil['Ailment'].lower():
```

```python
if 'Oil Name' in oil and search_criteria.lower().strip() in oil['Oil Name'].lower().strip():
```

```python
if patient_data['Patient Name'].lower() == sheet_name.lower():
```

```python
while insert_at_row - 2 < len(patients_data) and patients_data[insert_at_row - 2]['Patient Name'] == sheet_name:
```

I`ve decided to comment them out by using ``  # noqa``. This has been used with considerable caution and limitation since it is used in 5 instances only in over 890 lines of code.

Updated CI Linter test result:

![Alt text](/readme/images/linter-updated.jpg)


#### Python

I`ve used  the Python debugging tool available in GitPod to test my code in a high number of instances.
The use of print statements where also consistent across the development stage, and still present in order to prompt the user on different stages of the program instance, and also to validate correct code execution.


#### Local functionality tests
Link to full local functionality test: [TESTING.MD](https://github.com/mtopircean/essential-oils/blob/main/TESTING.md)

#### Fixed bugs and current errors

* FIXED BUGS:
Several issues where identified during development, but most common:
- while loops creating a continuous loop through a portion of the code
- validation criteria was not initially considering empty strings
- lower / upper case sensitivity was not consistently applied where needed
- indentation errors where numerous but fixed
- not in all situation, in case of validation issue, input was being retriggered
- challenges in running the main function within other functions, challenges which have lead to the current solution
- high difficulty in implementing the modify oil function around updates to specific fields in google sheet

SPECIFIC ERROR:
If a link to the google sheet is broken, program would break. I`ve tested this by changing the name of one of the sheets linked in the program and the error bellow was returned.
![Alt text](/readme/videos/google-sheet-broken-connection.gif)

Solution implemented in this case was a try / error update to the code communicating with the database, like the example bellow:

```python
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
```
EXAMPLE OF SOLUTION IMPLEMENTED:

![Alt text](/readme/videos/connection-error.gif)

* KNOWN ERRORS:

a. Although is not considered as an error, there is a best practice not implemented in the form of imperative commits to GitHub.
It was highlighted for my previous project, for project 2 that this should be implemented. Unfortunately, Project 2 feedback came very late, close to me finishing this project, so I was able to implemented it on a very limited number of commits, and probably still building the habit of doing this.

b. Due to size of screen in Heroku, when listing the patients database the score option moves to another row.
![Alt text](/readme/images/patient-list.jpg)

c. Again, not a specific error in code, but in several instances I`ve made general comments in my commit on "Updating Test file format". This was related to changes made to the structure in order for me to visualize it in the github reader format. Something I will correct in the future projects by using external tools to help me visualize the changes.

## Credits
#### Code Used:
* Took inspiration from LoveSandwiches for the code bellow:

```python
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
```

* Took inspiration from here in using tabulate: https://pypi.org/project/tabulate/

* Thanks to Joshua in CI Tutor team for guidance on how to update a spreadsheet by allowing to identify an elements position:
https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell

* Took inspiration in different validation methods from this link(ex. while not in):https://tutorial.eyehunts.com/python/while-loop-yes-or-no-python-example-code/

Generally, during development there was a lot of research done on different syntaxes to use, followed by a lot of trial and error.

#### Other Credits

* Deployment instructions in GitHub copied from kera-cudmore different repo and following the article written by her on how to write a readme.
* Inspiration on readme structure taken from kera-cudmore repo`s and following the article written by her on how to write a readme.

* Thanks to Graeme Taylor, my mentor for all his support during the development of the project.
* Thank you to the CI Tutor Team who supported in several instances by providing guidance on overcoming various challenges encountered during development:

    * Thanks to Jason also for guidance on how to format the code in order for meet the length criteria
    * Thanks to Joshua in CI Tutor team for guidance on how to update a spreadsheet by allowing to identify an elements position:
    https://docs.gspread.org/en/latest/user-guide.html#finding-a-cell
    * If I`m missing anyone, I am not ungrateful, just suffer from bad memory :)


## About Author
Marius Topircean is an aspiring software-developer on a journey to develop and learn his place into the developer community.

My contact details are:

Email: mtopircean@yahoo.com

Phone: +353857642212

Slack: Marius Topircean

GitHub: mtopircean  

LinkedIn: [Marius Topircean](https://www.linkedin.com/in/marius-t-7b5592124)