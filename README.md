# Document Management system
create an django virtual environment
```bash
Windows:py -m venv environment_name
Unix/MacOS/Linux: python3 -m environment_name
Then you have to activate the environment, by typing this command:
Windows:environment_name\Scripts\activate.bat
Unix/MacOS/Linux: source environment_name/bin/activate
```


## Getting Started

First, install  development.text file for all packages:
command: pip install -r development.text
Second , Makemigrations:
Unix/MacOS/Linux command: python manage.py makemigrations
Windows: py manage.py makemigrations
Then Migrate:
Unix/MacOS/Linux command: python manage.py migrate
Windows: py manage.py migrate
Finally run server
Unix/MacOS/Linux command: python manage.py runserver
Windows: py manage.py runserver
```bash
create superuser
Unix/MacOS/Linux command: python manage.py createsuperuser

Windows: py manage.py createsuperuser
```

Open [http://localhost:8000](127.0.0.1:8000) with your browser to see the result.

## Document PDF
![Report.pdf](https://github.com/tasim313/Document-Management/files/12078343/Report.pdf)

## requirement/development.text
```bash 
Django==4.2.2
djangorestframework     
django-filter
drf-yasg
drf-spectacular
django-versatileimagefield
django-autoslug==1.9.9
django-debug-toolbar
django-health-check
django-import-export
django-jazzmin
django-cors-headers==4.0.0
docx2pdf==0.1.8
markdown 

```

