
📄 README.txt — Django DRF Project (Task Tracker API)
----------------------------------------------------
🌐 PROJECT: Django DRF — Task Tracker API (No Auth)
----------------------------------------------------

This project is a simple Project & Task Tracker built using Django and Django REST Framework (DRF).
It uses ModelViewSet for all CRUD operations and contains a Dashboard API for summarized data.
This version does not use authentication — all data is public.

📌 FEATURES

Create & list Projects

Create & list Tasks

Dashboard summary with ORM aggregations

Model-level validation (priority & due_date rule)

NO authentication (owner is stored as a simple string)

Full DRF-based API with ModelViewSets

Create a virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3) Install dependencies
pip install -r requirements.txt


(If no requirements file is provided, manually install)

pip install django djangorestframework

 Apply migrations
python manage.py makemigrations
python manage.py migrate

 Start the development server
python manage.py runserver


Server available at:

http://127.0.0.1:8000/

📘 API ENDPOINTS (NO AUTHENTICATION REQUIRED)
PROJECT APIs
Create Project (POST)
/projects/

List Projects (GET)
/projects/


Optional filters:

/projects/?owner=Rahul
/projects/?search=demo

TASK APIs
Create Task (POST)
/tasks/

List Tasks (GET)
/tasks/


Filters:

?status=todo
?project_id=1
?due_before=2025-02-01

DASHBOARD API
/dashboard/?owner=<owner_name>


Returns:

Total projects

Total tasks

Task count grouped by status

Top 5 upcoming tasks OR "No upcoming tasks!"

🧪 VALIDATION RULES
Project:

A user (owner string) cannot have two projects with the same name.

Task:

Priority must be 1 to 5

If status is done, due_date cannot be in the future

📄 POSTMAN DOCUMENTATION

You can create documentation manually or import a JSON collection.

Recommended structure:

Task Tracker API
    ├── Create Project
    ├── List Projects
    ├── Create Task
    ├── List Tasks
    ├── Dashboard


Use Body → raw → JSON for POST requests.

🏗 TECHNOLOGIES USED

Python 3

Django

Django REST Framework

SQLite (default, can change to PostgreSQL)

🙋 Support

If you need:

Postman Collection JSON

Swagger/OpenAPI schema

GitHub-friendly README.md
just ask.

✅ END OF README.txt