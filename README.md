# recruit-me
Allows developers and users to list potential coding project ideas to recruit other developers with a specific skill-set  
Please ensure you have PostgreSQL installed with the following steps:  

```
pip install psycopg2-binary
```

Then create an RDS database in your AWS account (or natively use Postgre SQL).  

Modify the databases under the settings page in settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'masteruser',
        'PASSWORD': '12345678',
        'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}
```
Name: Name of database made in AWS, defaults to 'postgres'  
Host: Endpoint link found in RDS dashboard  
Port: Port found in RDS Dashboard  

Then, make migrations  
```
py manage.py migrate
```
```
py manage.py runserver
```

And load it in your browser: 127.0.0.1:8000/  

**Signup Page**
<img width="1510" alt="SignUpPage" src="https://github.com/surven02/recruit-me/assets/63677596/565d77d4-1cef-45d1-a69e-d9ac76cf59ff">

**Login Page**
<img width="1510" alt="LoginPage" src="https://github.com/surven02/recruit-me/assets/63677596/9ee360e8-673e-4e0b-8a5b-844e5c6b89fa">

**Home Page**
<img width="1916" alt="HomePage" src="https://github.com/surven02/recruit-me/assets/63677596/969ca3a2-c5d5-44be-9612-da7e95ae39da">

**Browse Page**
<img width="1916" alt="BrowsePage" src="https://github.com/surven02/recruit-me/assets/63677596/639ab22a-6bb7-494a-a9f5-976cf1c2d087">

**Project Listing**
<img width="1916" alt="ProjectListing" src="https://github.com/surven02/recruit-me/assets/63677596/8e4f8683-92da-4893-b8b2-47ecd097b7cf">

**Conversation**
<img width="1916" alt="Conversation" src="https://github.com/surven02/recruit-me/assets/63677596/374136c1-be88-4e66-bb38-da71c71eced5">

**User Inbox**
<img width="1918" alt="UserInbox" src="https://github.com/surven02/recruit-me/assets/63677596/9e7144d2-0100-4d63-9d51-6a4e62ae1b2c">

**Conversation Thread**
<img width="1918" alt="ConversationThread" src="https://github.com/surven02/recruit-me/assets/63677596/4c0e882e-09a3-4345-a961-4791b2919c99">



