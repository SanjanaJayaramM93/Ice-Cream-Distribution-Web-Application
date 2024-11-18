from django.contrib import admin
from .models import Store,Tub

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','store_name','store_location','store_email')

class TubAdmin(admin.ModelAdmin):
    list_display = ('id','tub_flavour','tub_size','store')
    

admin.site.register(Store,StoreAdmin)
admin.site.register(Tub,TubAdmin)

