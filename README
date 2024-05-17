# Python API

## Description

Python API is a simple project that performs basic CRUD (Create, Read, Update, Delete) operations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/therealcraiggazimbi/_launch.git
   ```

2. Navigate to the project directory:

   ```bash
   cd _launch
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install Django and Django REST Framework:

   ```bash
   pip3 install django djangorestframework
   ```

## Running Tests

To run unit tests, execute the following command:

```bash
python manage.py test
```

The tests include:

1. Deleting an applicant
1. Partially updating an applicant
1. Retrieving an applicant
1. Updating an applicant
1. Creating a skill for an applicant
1. Retrieving all applicants

## Starting the Server

To start the server, run:

```bash
python manage.py runserver
```

## Endpoints:

Here are all the endpoints with the provided updates:

- **Create/List Applicants:**

  - **POST** `/api/applicants/`
    - Include JSON data:
      ```json
      {
        "name": "Craig Gazimbi"
      }
      ```
  - **GET** `/api/applicants/`

- **Retrieve/Update/Delete Applicant:**

  - **GET** `/api/applicant/<int:pk>/`
  - **PUT** `/api/applicant/<int:pk>/`
    - Include JSON data:
      ```json
      {
        "name": "Craig David"
      }
      ```
  - **DELETE** `/api/applicant/<int:pk>/`

- **Create Skill for Applicant:**
  - **POST** `/api/applicant/<int:pk>/skill/`
    - Include JSON data:
      ```json
      {
        "name": "Python"
      }
      ```
