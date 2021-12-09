from django.contrib import admin
from .models import LotoTirage,EuromillionTirage


class LotoTirageAdmin(admin.ModelAdmin):
    list_display = ('tl_id','tl_jour','tl_tirage')



class EuromillionTirageAdmin(admin.ModelAdmin):
    list_display = ('te_id','te_jour','te_numeros','te_numeros_comp')


admin.site.register(LotoTirage,LotoTirageAdmin),
admin.site.register(EuromillionTirage,EuromillionTirageAdmin)
