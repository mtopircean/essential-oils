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
Deployment of the website was done using HEROKU, and can be accessed here[ESSENTIALOILS](https://essential-oils-8a5b724d8c2a.herokuapp.com/)
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
z


#### Colour Selection
 - Red: alert
 - Cyan: Menu
 - White: for everything else in order to add a contrast to HEROKU background
![Alt text](/readme/images/color-scheme.jpg)


#### Features


## Testing and Validation

#### Spellcheck

#### CI Linter


#### Python


#### Local functionality tests
Link to full local functionality test: [TESTING.MD](https://github.com/mtopircean/essential-oils/blob/main/TESTING.md)

#### Fixed bugs and current errors


## Credits
#### Code Used:


#### Other


## About Author
Marius Topircean is an aspiring software-developer on a journey to develop and learn his place into the developer community.

My contact details are:

Email: mtopircean@yahoo.com

Phone: +353857642212

Slack: Marius Topircean

GitHub: mtopircean  

LinkedIn: [Marius Topircean](https://www.linkedin.com/in/marius-t-7b5592124)