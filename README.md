# EssentialOils

EssentialOils was born out of my wife`s necessity for a CRM - Client Relationship Management / Product Management system that would offer her support in her journey of understanding EssentialOils, and even more, in providing support to different people requiring guidance and support in finding natural and alternative solutions to different ailments.

## CONTENT
* [Scope](#scope)
* [User Stories](#user-stories)
* [Deployment](#deployment-and-local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Technologies](#technologies)
    * [Programming Languages](#programming-languages)
    * [IDE](#ide)
    * [Other](#other)
* [Design](#design)
    * [Theme](#theme)
    * [Colour Selection](#colour-selection)
    * [Features](#features)
* [Testing and Validation](#testing-and-validation)
    * [CI Linter](#ci-linter)
    * [Spellcheck](#spellcheck)
    * [Python](#javascript)
    * [Local functionality tests](#local-functionality-tests)
    * [Fixed bugs](#fixed-bugs-and-current-errors)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Other](#other)
* [About Author](#about-author)

## Scope
Essential oils application offers the user a simple Client Relationship Management and Product Management System.
Application allows the user to enter/pull through a basic Python interface data into/from a Google Spraedsheet, update product data and maintain a search history database based on customer name.
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
- access easiley a patients file

FUTURE STATE:

Future plan for the application is to extend the level of data that can be stored, accessed and modified.
It should also offer the user the ability to have more flexibility in what they are using as search criteria, together with filtering options.
For patients listing, it will include more details on when the search has taken place and allow to store users personal data as the discussions/searches happen, data like date of birth, gender, contact details.

## Deployment and Local Development
Deployment of the website was done using HEROKU, and can be accessed here [ESSENTIALOILS](https://essential-oils-8a5b724d8c2a.herokuapp.com/)
The steps in deployment where taken following the example of LoveSandwiches CI Project.

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


## Technologies

#### Programming Languages:
1. Python


#### IDE:
1. GitHub: to store the source code.
2. GitPod: support to write majority of code, deploy via Heroku, and push data to store in GitHub. Gitpod was used also for debugging pourposes.

#### Other:
1. HEROKU: to deploy application and act as the app interface
2. CI Python Linter: to validate code format.

## Design
Design is very basic and limited to Python/Heroku interfaces.
There was a separation of data based on their pourpose and intention by using colorama.
The use of tabulate and font styles was done in order to structure the data in a manner easy to read and understand.


#### Theme
Even with the interface limitations, I`ve tried to create and maintain a database theme by using tabulate in order to return the data in a more pleasent, easy to follow way.
The use of different colors and font highlight was done to create structure and an ease in understanding and reading the different messages returned by the app.
![Alt text](/readme/images/tabulate.jpg)


#### Colour Selection
- Red: alert
- Cyan: Menu
- White: for everything else in order to add a contrast to HEROKU background
![Alt text](/readme/images/color-scheme.jpg)


#### Features

A. External Features Implemented:

-  Tabulate add-on implemented in order to provide a more graphical representation of the database and allow user to easiley read and understand data.
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
This was thought in order to give the user a continous loop through the code and improve it`s experince by removing unnecesarry steps.

User is provided guidance throughout the program in order to make sure it is easy to understand and use.

* Maine menu:
The main menu is the center point of the application connecting the various functions to a center of command.
I`ve allowed for it to run automatically when the script is loaded, to again, limit the users effort in accessing the tools functionality. Functionality achieved through the use of the code bellow:

```python
if __name__ == "__main__":
    main()
```

I`ve also chose to separate it from the rest of the code visually by using CYAN color, dedicated only to this section.

Main menu is providing access to 6 main function:
    1. Add a product to the database
    2. List oils database
    3. Search a product in the database
    4. Modify oil data
    5. List patients database
    6. Search patient in the database

1. Add a product to the database(add_oil()):
* Main functionality of this feature is to allow the user to add a product to the database by inputing specific parameters.
It also calculates a specific score which is returned in the same database in order to offer a comparison between the different products.
* If an oil already exists when trying to enter the product, the user will be prompted that the product is already present in the databse, and it will recommand to use the Modify oil data function if the choice will be to modify it`s parameters.
* Throughouth the function, the user is left with choices to jump through different functionalities, in order to make sure there aren`t any closed loops.
* Error checks are also present to ensure that parameters are entered, or that the correct parameters are entered, like for example:
    * No empty strings for oil name and ailment
    * Yes and No where required, and no other optionl; implemented considering validation ignoring lower/upper case use
    * Use of numeric only characters for price input
* Function, through a link to update_oils_worksheet() function will connect and update the relevant google sheet

EXAMPLE OF FUNCTION RUNNING:
![Alt text](/readme/videos/add-oil-function.gif)

2. List oils database:
Functionality relates to the option of a user to list all of the oils present in the database.
By using tabulate, user is able to view the information in a manner easier to read and understand.
Similar to the rest of the functions, in order to allow an open loop when running the function, user can then return to main menu.
![Alt text](/readme/videos/list-oils.gif)

## Testing and Validation

#### Spellcheck

Spellcheck was run using word spellcheck validation option.
All found spelling errors where corrected in order to give the user a clean experience when ussing the tool.

#### CI Linter

Code was tested by using the CI Linter web application.
No issues where identified except the ones bellow which where not addressed as they would have required for the code to be re-written. Due to the advanced state of the project and due to the fact that changing the code could have impacted the integrity and stability of the code, I`ve decided to document them only at this moment.

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


#### Python

I`ve used  the Python debugging tool available in GitPod to test my code in a high number of instances.
The use of print statements where also consistent across the development stage, and still present in order to prompt the user on different stages of the program instance, and also to validate correct code execution.


#### Local functionality tests
Link to full local functionality test: [TESTING.MD](https://github.com/mtopircean/essential-oils/blob/main/TESTING.md)

#### Fixed bugs and current errors

* KNOWN ERRORS:

a. Althoug is not considered as an error, there is a best practice not implemented in the form of imperative commits to GitHub.
It was highlighted for my previous project, for project 2 that this should be implemented. Unfortunatley, Project 2 feedback came very late, close to me finishing this project, so I was able to implemented it on a very limited number of commits.

b. If a link to the google sheet is broken, program will break. I`ve tested this by changed the name of one of the sheets linked in the program and the error bellow was returned. Due to time constraints, I was unable to further progress in creating a fix, however, the user is not left access in the program in order to change the master data, and although not done, the file will be locked to the user so main data will not be able to be altered.
![Alt text](/readme/videos/google-sheet-broken-connection.gif)


## Credits
#### Code Used:


#### Other

Thanks to Graeme Taylor, my mentor for all his support during the development of the project.
Thank you to the CI Tutor Team who supported in several instances by providing guidance on overcoming various challenges encountered during development.


## About Author
Marius Topircean is an aspiring software-developer on a journey to develop and learn his place into the developer community.

My contact details are:

Email: mtopircean@yahoo.com

Phone: +353857642212

Slack: Marius Topircean

GitHub: mtopircean  

LinkedIn: [Marius Topircean](https://www.linkedin.com/in/marius-t-7b5592124)