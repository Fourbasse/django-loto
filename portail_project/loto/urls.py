from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.home, name="index"),
    path('index/',views.EuromillionBdd, name="index"),
    path('index/simulation',views.Simulation,name="simulation"),
    path('index/loto_datatable',views.LotoDatatable,name="loto_data")
]
