from django.db import models
from django.contrib import admin

class LotoTirage(models.Model):
    tl_id = models.AutoField(primary_key=True,db_column="id")
    tl_jour = models.CharField(max_length=300,db_column="Jour")
    tl_tirage = models.CharField(max_length=300,db_column="Tirages")

    @admin.display(ordering='-tl_id')

    def __str__ (self):
        return self.tl_tirage + self.tl_jour

class EuromillionTirage(models.Model):
    te_id = models.AutoField(primary_key=True,db_column="id")
    te_jour = models.CharField(max_length=300,db_column="Jour")
    te_tirage = models.CharField(max_length=300,db_column="Tirages")

    @admin.display(ordering='-te_id')

    def __str__ (self):
        return self.te_tirage + self.te_jour
