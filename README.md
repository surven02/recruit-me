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


