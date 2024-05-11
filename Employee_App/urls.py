from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name="index"),
    path("number/",number,name="number"),
    path("Result/",final_data,name="final_data"),
]