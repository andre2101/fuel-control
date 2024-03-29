#coding: utf-8
import re
from decimal import Decimal
from splinter.browser import Browser
from BeautifulSoup import BeautifulSoup

def get_fuel(preco_alcool, preco_gasolina, 
			 consumo_alcool, consumo_gasolina, kilometragem, tanque):
	"Faz o srap do resultado do simplex no phpsimplex.com"
	
	browser = Browser('zope.testbrowser')
	URL = """http://www.phpsimplex.com/simplex/page2.php?objetivo=min&Submit=Continuar&restricciones=3&variables=2&l=es&x1=%(preco_alcool)f&x2=%(preco_gasolina)f&r11=%(consumo_alcool)f&r12=%(consumo_gasolina)f&desigualdad1=1&y1=%(kilometragem)f&r21=1&r22=1&desigualdad2=-1&y2=%(tanque)f&r31=-0.2&r32=1&desigualdad3=1&y3=0"""
	print URL % locals()
	browser.visit(URL % locals())
	browser.click_link_by_partial_href('solucion2.php')
	html = BeautifulSoup(browser.html)
	text = ""
	
	try:
		text = html.findAll('p')[2].getText()
		
		
		#rgx = re.compile('\\d+\\.*\\d*')
		#rgx = re.compile('\\d+(?:\\.\\d*)*')
		#results = rgx.findall(text)
		
		if text.count('X1 = 0'):
			print 'X1=0'
			#rgx = re.compile('\\d+\\.\\d+')
			rgx = re.compile('\\d+\\.*\\d*')
	
			results = rgx.findall(text)
			return {
				'custo_total': 	Decimal(results[0]),
				'vol_alcool': 	0,
				'vol_gasolina':	Decimal(results[1]),}
	
		elif text.count('X2 = 0'):
			print 'X2=0'
			rgx = re.compile('\\d+\\.\\d+')
			results = rgx.findall(text)
			return {
				'custo_total': 	Decimal(results[0]),
				'vol_alcool': 	Decimal(results[1]),
				'vol_gasolina':	0}
	
		else:
			rgx = re.compile('\\d+\\.\\d+')
			results = rgx.findall(text)
			return {
				'custo_total': 	Decimal(results[0]),
				'vol_alcool': 	Decimal(results[1]),
				'vol_gasolina':	Decimal(results[2]),}		
	except IndexError:
		vol_alcool = 0
		vol_gasolina = kilometragem / consumo_gasolina
		custo_total = vol_gasolina * Decimal(preco_gasolina)
		print "fuuuu" 
		return {
				'custo_total': 	Decimal(custo_total),
				'vol_alcool': 	Decimal(vol_alcool),
				'vol_gasolina':	Decimal(vol_gasolina),}		




params = {
	'preco_alcool': 1.87,
	'preco_gasolina': 2.61,
	'consumo_alcool': 10.4,
	'consumo_gasolina': 14.1,
	'kilometragem': 650,
	'tanque': 50,
}
#print get_fuel(**params)