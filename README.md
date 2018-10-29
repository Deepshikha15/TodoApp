# TodoApp

created title,content,default created dateTime and setTime .

No user Login & Authentication 
admin login .

App handles all the CRUD operations

Created Django admin interface for this so that an admin user can login and add the entries by superuser login.

search and filtering with required fields in the admin interface using search and filter queries in admin.py

The entry deleted from non-admin interface should be still visible for the Admin by defining update function 

Admin should be able to download the bulk entries of todo list in csv format from Django Admin Interface.
                to check it : localhost/download
Created an API to list all the to do items as well as individual item without using class view based .
                to check it : localhost/todolist/Todo

