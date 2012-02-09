# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from cars.models import CarMaker, Car
from decimal import Decimal
from php_simplex import get_fuel

@render_to('index.html')
def index(request):
   	tanque = 50
   	marcas = CarMaker.objects.all()
   	marca = CarMaker.objects.filter(name=request.GET.get('fabricante', 'Fiat'))
   	carros = Car.objects.filter(car_maker=marca)   	
   	
   	if request.POST:
		preco_alcool = float(request.POST.get('alcool'))	
		preco_gasolina = float(request.POST.get('gasolina'))	
		
		modelo = request.POST.get('modelo')	
		modelo = Car.objects.get(pk=modelo)
		
		urbano = get_fuel(preco_alcool, preco_gasolina, modelo.alc_urban, modelo.gas_urban, 325, tanque)
		rodoviario = get_fuel(preco_alcool, preco_gasolina, modelo.alc_road, modelo.gas_road, 650, tanque)

		URBANO = {
			'km_alc': modelo.alc_urban * tanque,
			'total_alc': preco_alcool * tanque,
			
			'km_gas': modelo.gas_urban * tanque,
			'total_gas': preco_gasolina * tanque,}

		RODOVIARIO = {
			'km_alc': modelo.alc_road * tanque,
			'total_alc': preco_alcool * tanque,
			
			'km_gas': modelo.gas_road * tanque,
			'total_gas': preco_gasolina * tanque,}

		TEMPLATE='results.html'
	return locals()
