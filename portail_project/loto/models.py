from django.db import models
from django.contrib import admin

class LotoTirage(models.Model):
    t_id = models.AutoField(primary_key=True,db_column="id")
    t_jour = models.CharField(max_length=300,db_column="Jour")
    t_tirage = models.CharField(max_length=300,db_column="Tirages")

    @admin.display(ordering='-t_id')

    def __str__ (self):
        return self.t_tirage + self.t_jour
