




Project Name --- API
To start the project, type the command--django-admin startproject api
After doing this step, it will automatically create the necessary python files :
	__init__

	settings---website management

	urls---used for url resolver

	wsgi


App name --- Company
To make the app, type the command--django-admin startapp Company
The app include the database of Employee in backend.
To set up the project----
Create one virtual environment machine by command –
python -m venv api-app-virtual
Then, activate the virtual env by command---
.\api-app-virtual\Scripts\activate
Then,.\api-app-vitrtual\Scripts\activate--- install the requirements text document--- 
pip install -r requirements.txt (it contain all the packages which required in the project)
Then make the necessary migrations-- 
						python manage.py makemigrations
						python manage.py migrate
						python manage.runserver
