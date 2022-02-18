# Python-Django-Flask-Psql-Api-Crud

git clone https://github.com/sznitowski/Python-Django-Flask-Psql-Api-Crud.git

### Config Virtual env.
open with commandprom and ejecute python -m venv myenv
cd myenv/scripts/ and ejecute | activate | comamnd to enable virtuall env 

### Install Django / Flask in Virtual env.

# in proyect directory ejecute command | python -m pip install --upgrade pip |
# pip install django
# pip install djangorestframework
# pip install django-cors-headers
# django-admin startproject mysite

### Creating a new django App
# Python manage.py startapp appName

### Create a database in pg4admin
# pip install psycopg2
 confing settings in settings.py to connect with the database

 ### Migrations Commands
 * migrate, Which is responsible for applying and unapplying migrations.
 * makemigrations, Which is responsible for creating new migrations based on the changes you have made to your models.
 * sqlmigrate, Which display the SQL statements for a migrations.
 * showmigrations, Which lists a project's migrations and their status.

 ### Migrate:
  Make sure your virtual environment is activated and enter, python manage.py migrate

### Creating django Model
class  Countries(models.Model);
name = models.CharField(max_lenght=50, blank-False, default-'')
capital = models.CharField(max_lenght=50, blank-False, default-'')
class Meta:
            ordering =('id',)

### Creating new migrations
* python manage.py makemigrations countries

### Apply Migration
* python manage.py migrate countries

### Create Serialize file
* create serializers.py file in countries folder

### Running server
* Activate virtual environment and ejecute | python manage.py runserver |  | python manage.py runserver 8080 |

### Creating SuperUser admin
* python manage.py createsuperuser   check in 127.0.0.1:8080/admin


### Create and config views
* create file views.py in countries folder and config endpoints Get, Post, Put, Delete

### Urls config
* create urls.py file in countries and config 
* 127.0.0.1:8080/api/countries ---- |GET| |POST| --------- views.countries_list
* 127.0.0.1:8080/api/countries/id-- |GET| |PUT| |DELETE| - views.countries_detail
* 127.0.0.1:8080/api/admin -------- |GET| ---------------- admin.site.urls





