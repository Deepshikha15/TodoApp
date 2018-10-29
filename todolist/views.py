# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet
from django.shortcuts import render

import csv, io
from django.shortcuts import render, redirect, HttpResponse

from todolist.models import TodoList
from .models import TodoList, Category

from django.http import JsonResponse
import datetime


def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
            return redirect("/")  # reloading the page

        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo





    return render(request, "index.html", {"todos": todos, "categories": categories})


def download(request):
    items = TodoList.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="TodoList.csv"'

    writer = csv.writer(response, delimiter=str(u';').encode('utf-8'))
    writer.writerow(['title', 'category', 'content'])

    for obj in items:
        writer.writerow([obj.title, obj.category, obj.content])

    return response




def adminView(request,is_superuser,TodoList):
    if is_superuser == 1:
        dos = TodoList.objects.filter('todo').update(title='completed')
        dos.save()
    else:
        pass
    return request



