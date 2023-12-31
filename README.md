# AdoptMe – Django Application
AdoptMe is a Django-based application that enables users to browse adoptable animals and offers 
various services related to animal healthcare.
## Introduction
AdoptMe is a Django-powered web application designed to facilitate the adoption of animals and 
provide healthcare-related services for pets. It allows users to explore profiles of adoptable animals, 
submit adoption applications, and access various pet healthcare services.
## Features
- User Registration and Login: Users can create accounts and log in to the application.
- Animal Profiles: Detailed profiles of adoptable animals, including images, descriptions.
- Adoption Applications: Users can submit adoption applications for animals they are interested in.
- Pet Healthcare Services: Access to a range of services related to pet healthcare.
- Donation Support: Users have the option to make monetary donations to support animals in need.
## Installation
To run AdoptMe locally, follow these steps:
1. Clone the repository:
```
git clone https://github.com/PYT70FinalProjectGroup1/Pet_Adoption.git
```
2. Create a Python virtual environment and activate it:
```
python -m venv venv
```
3. Run virtual environment
```
venv/Scripts/activate
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Perform database migrations:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
6. Load data to Database
```
python manage.py loaddata output.json
```
Four user created: 

- admin, password admin

- Monic, password admin123#

- Dima, password admin123#

- Tester, password admin123#

7. Start the development server:
```
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000/

## Configuration
To configure AdoptMe, create a .env file in the project's root directory and customize it according to 
your needs. Here's an example .env file:
```
DEBUG=True
ALLOWED_HOSTS=localhost
SECRET_KEY=my_secret_key
```

## Usage Examples
To Be Added
## Requirements
The AdoptMe application has the following dependencies:
- Python,
- Django,
- Other dependencies are listed in the `requirements.txt` file.
## Support and Contact
If you have any questions, feedback, or encounter issues with the AdoptMe application, please 
don't hesitate to contact us at email@example.com.
## TEST
To run the test, cd into the directory where manage.py is:
```
python manage.py test
```
