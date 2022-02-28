
# Contacts Manager Application

A simple web application for managing contacts based on a particular user developed using Django and Next.js.



## Installation and instruction for running backend

Run __contact_application__ with python virtual environment

* Requirements:
    - python3.8
    - venv
    - psycopg2

* Create a virtual environment
```bash
    $ python3 -m venv venv
```

* Activate virtual environment (Windows and Linux)

__Windows__
```bash
    > venv\Scripts\activate
```

__Linux__
```bash
    $ source venv/bin/activate
```

* Install all packages from `requirements.txt` file

```bash
    $ pip install -r requirements.txt
```

* Migrate models to Database

```bash
    $ python manage.py migrate
```

* Running application locally

```bash
    $ python manage.py runserver
```

* By default, application will be accessible on `http://127.0.0.1:8000/`