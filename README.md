# Instructions

## Setup

1. Install django
2. Install pillow
3. Install django-rest-framework

## Run

1. Run `python manage.py migrate`
2. Run `python manage.py createsupersuser
3. Run `python manage.py runserver`
4. Go to `http://localhost:8000/admin` and login with the superuser credentials

## API

1. POST to `http://localhost:8000/api/v1/auth/login/ to login and aquire session cookie
2. POST to `http://localhost:8000/api/v1/images/upload/` to upload an image
3. GET to `http://localhost:8000/api/v1/images/view/` to get a list of images
4. GET to `http://localhost:8000/api/v1/images/view/link/<id>/` to get a specific image link/path

