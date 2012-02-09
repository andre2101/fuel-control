# -*- coding: utf-8 -*-
from django.db import models


    
class CarMaker(models.Model):
    "Represents the one that fabric the car"
    name = models.CharField(u"Nome",max_length=80)
    
    def __unicode__(self):
        return self.name
    
    
class Car(models.Model):
    "Represents the information of a car"
    name = models.CharField(u"Nome",max_length=80)
    car_maker = models.ForeignKey(CarMaker)
    
    gas_urban = models.DecimalField(u"Consumo Gasolina em Ambiente Urbano",max_digits=10, decimal_places=2)
    gas_road = models.DecimalField(u"Consumo Gasolina em Ambiente De Estrada",max_digits=10, decimal_places=2)
    alc_urban = models.DecimalField(u"Consumo Alcool em Ambiente Urbano",max_digits=10, decimal_places=2)
    alc_road = models.DecimalField(u"Consumo Alcool em Ambiente De Estrada",max_digits=10, decimal_places=2)    
    
    def __unicode__(self):
        return "%s - %s" % (self.name, self.car_maker)
    









