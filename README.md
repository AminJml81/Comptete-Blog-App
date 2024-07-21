# Final Project For Maktabkhooneh Django for Beginners Course
## _Blog Project_


Course Link: https://maktabkhooneh.org/course/%d8%a2%d9%85%d9%88%d8%b2%d8%b4-%d8%ac%d9%86%da%af%d9%88-mk623/

Instructor github: https://github.com/AliBigdeli/

Template Link: https://themewagon.com/themes/free-bootstrap-blogging-website-template-revolve/


## Project Descriptions:
- index page with pagintaion of 6 posts per page.(also posts with certain categories, tags, authors can be filterd in this page)
- single page which users can read the entire blog content and also add comments.
- contact page which users can send the message.
- about page
- manage account which users can Login/ Logout / Signup / Change and Reset Password through email
- admin which superuser can add post, approve comments add user, ...


## Technologies Used:
- Django 4.2.13
- allauth for authentication (login, logout, signup, password change and password reset views)
- django-muticaptcha-admin (recaptcha v2)
- messages framework for displaying popups
- sites fremework
- sitemaps framework
- robots framework
- tinymice for post content
- taggit & humanize for blog tags and time formatting
- postgresql for database(psycopg2 for driver)


## URLS
- /	
- /about/
- /contact/	
- /admin
- /blog/<int:pid>/

- /accounts/manage/
- /accounts/signup/
- /accounts/login/	
- /accounts/logout/	
- /accounts/password/change
- /accounts/password/reset	
	
- /feed/rss/
- /robots.txt
- /sitemap.xml


## Download & Setup Instructions

### Clone project

```sh
git clone https://github.com/AminJml81/Maktabkhooneh-django-for-beginners-course-final-project.git
```

### Create .env file and add your own Environment variables
```sh
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=
SITE_ID=
USER_EMAIL=
USER_PASSWORD=
EMAIL_PORT=
PROD_DB_ENGINE=
PROD_DB_NAME= 
PROD_DB_USER=
PROD_DB_PASSWORD=
PROD_DB_HOST= 
PROD_DB_PORT=
DEV_DB_ENGINE=
DEV_DB_NAME= 
DEV_DB_USER=
DEV_DB_PASSWORD=
DEV_DB_HOST= 
DEV_DB_PORT=
RECAPTCHA_PRIVATE_KEY=
RECAPTCHA_PUBLIC_KEY=
RECAPTCHA_REQUIRED_SCORE=
```

### Migrate

```sh
python manage.py migrate
```

### CreateSuperuser

```sh
python manage.py createsuperuser
```

### Running the server
```sh
python manage.py runserver
```

#### Note about setting 
in mange.py file the setting is
```sh
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.setting.dev")
```
for deployment change setting.dev to setting.prod
```sh
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.setting.prod")
```


## To Do
- Adding like feature which users can like posts
- Dockerize


## Project Model Schema
![Blog-Project-Model-Schema](https://github.com/user-attachments/assets/f2452fbb-8c7e-4149-96af-e3756a879793)
