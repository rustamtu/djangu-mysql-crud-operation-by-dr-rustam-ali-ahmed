https://docs.djangoproject.com/en/4.2/intro/tutorial01/
Creating a project
django-admin startproject mysite

create a new repository on the command line
echo "# djangu-mysql-crud-operation-by-dr-rustam-ali-ahmed" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/rustamtu/djangu-mysql-crud-operation-by-dr-rustam-ali-ahmed.git
git push -u origin main


Create mysqldb admin
pip install mysqlclient
python manage.py runserver
python manage.py makemigrations
python manage.py migrate

 python .\manage.py createsuperuser
 python manage.py changepassword <username>
 http://127.0.0.1:8000/admin
 admin  admin

create new application
python manage.py startapp polls