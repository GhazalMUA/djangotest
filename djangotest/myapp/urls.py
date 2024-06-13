from django.urls import path
from . import views
app_name='myapp'
urlpatterns=[
    path('home/' , views.HomeView.as_view() , name='home'),
    path('about/<str:username>/' , views.AboutView.as_view() , name='about'),
    
]