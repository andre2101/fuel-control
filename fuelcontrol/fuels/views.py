# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from cars.models import CarMaker, Car
from decimal import Decimal
from php_simplex import get_fuel

@render_to('index.html')
def index(request):
   	marcas = CarMaker.objects.all()
   	marca = request.GET.get('fabricante')
   	carros = Car.objects.all()   	
   	
   	if request.POST:
		preco_alcool = float(request.POST.get('alcool'))	
		preco_gasolina = float(request.POST.get('gasolina'))	
		
		modelo = request.POST.get('modelo')	
		print modelo
		modelo = Car.objects.get(pk=modelo)
		print modelo
		tanque = 50
		urbano = get_fuel(preco_alcool, preco_gasolina, modelo.alc_urban, modelo.gas_urban, 325, tanque)
		rodoviario = get_fuel(preco_alcool, preco_gasolina, modelo.alc_road, modelo.gas_road, 650, tanque)
		print rodoviario
		TEMPLATE='results.html'
	return locals()
