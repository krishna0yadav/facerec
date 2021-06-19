from django.shortcuts import render,redirect
import requests
from . import methods

def home_view(request):
	if request.method=='POST':
		print(request)
	return render(request, 'home.html')

def save_licence_view(request):
	if request.method=='POST':
		licencepic=request.POST['licencepic']
		userpic=request.POST['userpic']
		lpic=open('lpic.url','w')
		lpic.write(licencepic)
		lpic.close()
		vpic=open('vpic.url','w')
		vpic.write(userpic)
		vpic.close()
		methods.getI420FromBase64(licencepic,'lpic')
		methods.getI420FromBase64(userpic,'vpic')
		return redirect('/verify/')
	return redirect(request, '/')

def verify_view(request):
	context=methods.match_faces()
	licencepic=""
	userpic=""
	with open('lpic.url','r') as f:
		licencepic=f.read()
	with open('vpic.url','r') as f:
		userpic=f.read()
	context['licencepic']=licencepic
	context['userpic']=userpic
	return render(request, 'verify.html', context)