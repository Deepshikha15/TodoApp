from tastypie.resources import ModelResource
from todolist.models import TodoList, Category


class TodoResource(ModelResource):
    class Meta:
        queryset = TodoList.objects.all()
        resource_name = 'Todo'
