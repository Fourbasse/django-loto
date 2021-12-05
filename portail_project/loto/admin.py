from django.contrib import admin
from .models import LotoTirage


class LotoTirageAdmin(admin.ModelAdmin):
    list_display = ('t_id','t_jour','t_tirage')

admin.site.register(LotoTirage,LotoTirageAdmin)
