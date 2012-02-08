from django.db import models

class Fuel(models.Model):
    "A Fuel"
    name = models.CharField(u"Nome",max_length=80)
    
    def __unicode__(self):
        return self.name
    
class FuelUsage(models.Model):
    "Represents the usage of some kind of fuel"
    fuel = models.ForeignKey(Fuel)
    urban = DecimalField(u"Consumo em Ambiente Urbano",max_digits=10, decimal_places=2)
    road = DecimalField(u"Consumo em Ambiente De Estrada",max_digits=10, decimal_places=2)