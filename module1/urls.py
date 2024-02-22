# from django.contrib import admin
# from django.urls import path
# from .views import *
# from ..crudapp.views import *
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('klpoori', hi, name='hi'),
#     path('', newhomepage, name='newhomepage'),
#     path('travelpackage', travelpackage, name='travelpackage'),
#     path('t1', print_to_console, name='print_to_console'),
#     path('t2', print_to_web, name='print'),
#     # path('random', random123, name='random123'),
#     path('getdate',get_date,name='get_date'),
#     # path('p/', print1, name='print1'),
#     path('random',random12,name='random12'),
#     path('specificlocationtime',specificlocationtime,name='specificlocationtime'),
#     path('database',registerloginfunction,name='database'),
#     path('chatform',pie_chart,name='chart_form'),
#     path('carousel',carousel,name='carousel'),
#     path('weather',weatherlogic,name='weatherappinput'),
#     path('insert',insert_emp,name='insert_emp')
# ]

from django.contrib import admin
from django.urls import path
from .views import *


# from ..crudapp.views import insert_emp  # Adjust this import based on your project structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('klpoori/', hi, name='hi'),  # Assuming 'hi' is a valid view function
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('t1/', print_to_console, name='print_to_console'),
    path('t2/', print_to_web, name='print'),
    path('getdate/', get_date, name='get_date'),
    path('random/', random12, name='random12'),
    path('specificlocationtime/', specificlocationtime, name='specificlocationtime'),
    path('database/', registerloginfunction, name='database'),
    path('chatform/', pie_chart, name='chart_form'),
    path('carousel/', carousel, name='carousel'),
    path('weather/', weatherlogic, name='weatherappinput'),
    path('login1/', login1, name='login12'),
    path('login/', login, name='login'),


    path('logout1/',logout,name='logout12'),
    path('register/', signup, name='signup'),
    path('signup1/',signup1,name='signup12'),
    path('contact/', contactus, name='contact'),
    # path('insert/', insert_emp, name='insert_emp'),
]

