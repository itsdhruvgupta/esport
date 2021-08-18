from django.contrib import admin 
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index, name = "home"),
    path("contact-us",views.contact, name = "contact"),
    path("about-us",views.about, name = "about"),
    path("registration-page",views.registration_page, name= "registration-page"),
    path("registration",views.registration, name= "registration"),
    path("winners",views.winners_page, name="winners")


]