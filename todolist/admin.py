# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from . import models


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title","content" ,"created", "due_date", "category")

    list_filter = ('title', 'created', 'due_date', 'category')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.TodoList, TodoListAdmin)


admin.site.register(models.Category, CategoryAdmin)


# @admin.register()
# class ViewAdmin(ImportExportModelAdmin):
#     pass
