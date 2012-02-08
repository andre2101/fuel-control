# -*- coding: utf-8 -*-
from django.db import models
from fuels.models import FuelUsage


    
class CarMaker(models.Model):
    "Represents the one that fabric the car"
    name = models.CharField(u"Nome",max_length=80)
    
    def __unicode__(self):
        return self.name
    
    
class Car(models.Model):
    "Represents the information of a car"
    name = models.CharField(u"Nome",max_length=80)
    car_maker = models.ForeignKey(CarMaker)
    
    alc_usage = models.ForeignKey(FuelUsage,related_name="car_alc_usage_set")
    gas_usage = models.ForeignKey(FuelUsage,related_name="car_gas_usage_set")
    
    def __unicode__(self):
        return "%s - %s" % (self.name, self.car_maker)
    