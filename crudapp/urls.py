from .views import *
from django.urls import path

urlpatterns = [
    path('', insert_emp, name='insert-emp'),
    path('show/', show_emp, name='show-emp'),
    path('edit/<int:pk>', edit_emp, name='edit-emp'),
    path('remove/<int:pk>', remove_emp, name='remove-emp'),

]