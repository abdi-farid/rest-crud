# rest-crud
basic rest crud api using django rest_framework

---

Here are the steps to create a REST API using the django framework 

- ## ***Create project***

```python
django-admin startproject myproject
```

- ## ***Create application***

```python
cd myproject 
python manage.py startapp myapp
```
- ## ***Add my app in project settings***
Add 'rest_framework' application with myapp
```
INSTALLED_APPS = [
    ....
    'rest_framework',  # Added ....
    'myapp'  # Added ....
]
```

- ## ***Add url.py file in **myapp*****
