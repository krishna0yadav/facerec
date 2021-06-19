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
		methods.getI420FromBase64(licencepic,'lpic')
		methods.getI420FromBase64(userpic,'vpic')
		return redirect('/verify/')
	return redirect(request, '/')

def verify_view(request):
	context=methods.match_faces()
	print(context)
	return render(request, 'verify.html', context)

# def capture(request):
# 	return render(request, 'home.html', {'data':data})