from django.urls import path
from . import views
app_name='shell'
urlpatterns = [
    path('', views.home, name='home'),
    path('en-us/about',views.about, name='about')
]
