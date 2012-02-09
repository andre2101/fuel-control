# -*- coding: utf-8 -*-
from annoying.decorators import render_to

@render_to('index.html')
def index(request):
   	if request.POST:
		TEMPLATE='results.html'
	return locals()