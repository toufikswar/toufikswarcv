
from django.urls import path, include
from . import views

# needed for include function to work in mycv/url.py for the namespace
app_name = "cv"

urlpatterns = [
    #path('<int:id>/view/', views.home, name="home"),
    #path('<int:id>/view/', views.home, name="home"),
    #path('<int:id>/edit/<str:section>/',views.edit , name="edit"),
    path('',views.home , name="home"),
    path('cv/', views.cv, name="mycv"),
]
