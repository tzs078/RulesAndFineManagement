
from django.urls import path
from fineApp.views import *

urlpatterns = [
    path('',register_view , name='register_view'),
    path('login_view/',login_view,name='login_view'),
    path('logout_view/',logout_view,name='logout_view'),
    path('homepage_view/',homepage_view,name='homepage_view'),

    
    path('student_show/',student_show,name='student_show'),
    path('student_add/',student_add, name='student_add'),
    path('student_update/<str:id>/',student_update,name='student_update'),
    path('student_delete/<str:id>/',student_delete,name='student_delete'),

    path('fine_view/',fine_view,name='fine_view'),
    path('fine_add_view/',fine_add_view,name='fine_add_view'),
    path('fine_update_view/<str:id>/',fine_update_view,name='fine_update_view'),
    path('fine_delete/<str:id>/',fine_delete,name='fine_delete'),

    path('actionPage/',actionPage,name = 'actionPage'),
    path('action_delete/<str:id>/',action_delete,name='action_delete'),

]
