
# Django Job Portal

This repository contains a Django-based job portal project created while learning Django. It includes views, templates, and course content related to building a job portal website using Django.

## Badges
[![HTML](https://img.shields.io/badge/HTML-5-red)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-3-blue)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4-purple)](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
[![Django](https://img.shields.io/badge/Django-3.0-green)](https://docs.djangoproject.com/en/3.0/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue)](https://www.sqlite.org/docs.html)

## Tech Stack

Django 

HTML

CSS

JAVASCRIPT


# Features
## Job Listing Web App
This is a web application for listing job postings, built with Django.  

### Job Listings

- Displaying a list of job posts on the home page (`index.html`).
- Each job post includes details such as title, location, salary, and job type.

### Job Detail View

- Viewing detailed information about a specific job post (`jobdetail.html`).
- Displaying job title, location, salary, job type, and description.

### Subscription Form

- Allowing users to subscribe for updates (`subscribe.html`).
- Users can submit their email address through a form for subscribing to updates.

### Views and URL Routing

- Handling different views for rendering templates and processing form submissions (`views.py`).
- Utilizing Django's URL routing to map URLs to view functions (`urls.py` assumed to exist).

### Database Interaction

- Fetching job posts and subscription data from the database using Django's ORM (`views.py`).

### Template Inheritance and Templating

- Using template inheritance to create reusable templates 
- Dynamically rendering data in templates using Django's template language (`{{ }}` syntax).

### Form Handling

- Rendering and processing subscription forms using Django's form handling capabilities (`subscribe.html` and related view function in `views.py`).

### Redirects

- Redirecting users to the home page if they attempt to view job details for a non-existent job or with an invalid ID (jobdetail view function in `views.py`).

### Dynamic URL Routing

- Generating dynamic URLs for viewing job details based on job IDs (`index.html`).
 
## Run Locally

Clone the project

```bash
  git clone https://github.com/MohammedKaif037/JobApp
```

Go to the project directory

```bash
  cd JobApp
```

Install dependencies

```bash
  pip install django
```

Start the server

```bash
  python manage.py runserver

```


## Usage/Examples

```bash
    -Creating your own URLs and views to serve user requests from the browser
    -Using the Django Template Language to create dynamic templates
    -Learning filters in the Django template language
    -Database migrations and multiple models
    -Writing queries to fetch data using Querysets
    -Working with the Django Admin Panel to manage/customize the website
    -Using Forms and ModelForms to accept information from users
    -Managing static files like HTML, CSS, and JS on the server
```


## Screenshots

![App Screenshot]( https://github.com/MohammedKaif037/JobApp/blob/main/screenshots/Screenshot%202024-05-08%20at%2003-01-34%20Employment%20Edge%20Home.png)
![App Screenshot](  https://github.com/MohammedKaif037/JobApp/blob/main/screenshots/Screenshot%202024-05-08%20at%2003-01-15%20Employment%20Edge%20Python%20Developer.png)
![App Screenshot](https://github.com/MohammedKaif037/JobApp/blob/main/screenshots/Screenshot%202024-05-08%20at%2003-01-49%20Employment%20Edge%20Subscribe.png))
![App Screenshot]( https://github.com/MohammedKaif037/JobApp/blob/main/screenshots/toadminjobappgithub.png))





## Authors

- [@Mohammed Kaif](https://github.com/MohammedKaif037)

