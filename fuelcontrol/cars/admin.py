from django.contrib import admin

from cars.models import Car, CarMaker
from fuels.models import Fuel


class CarMakerAdmin(admin.ModelAdmin):
    fieldsets = [
           ('Fabricante',               {'fields': ['name']}),
    ]

    
    list_display = ('name',)



class CarAdmin(admin.ModelAdmin):
    fieldsets = [
           ('Carro',               {'fields': ['name','car_maker','alc_usage','gas_usage']}),
    ]

    
    list_display = ('name','car_maker',)



#admin.site.register(CarAdmin, CarAdmin)
#admin.site.register(CarMakerAdmin, CarMaker)
