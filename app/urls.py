from django.urls import path
from app import views
app_name='app'
urlpatterns=[
    path('h3/',views.h3,name='h3'),
]