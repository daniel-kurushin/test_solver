from django.shortcuts import render_to_response
from denotat.models import *
def denotat(request):
	denotat=Sort.objects.all()
	return render_to_response('poisk.html', locals())
