from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.home, name="index"),
    path('index/loto_update',views.LotoUpdate, name="index"),
    path('index/euromillion_update',views.EuromillionBdd, name="index"),
    path('index/loto_simulation',views.Simulation,name="simulation"),
    path('index/loto_datatable',views.LotoDatatable,name="loto_data")
]
