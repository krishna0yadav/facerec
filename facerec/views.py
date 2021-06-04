from django.shortcuts import render,redirect
import requests
from . import methods

def home_view(request):
	if request.method=='POST':
		print(request)
	return render(request, 'home.html')

def save_licence_view(request):
	if request.method=='POST':
		s=request.POST['licencepic']
		methods.getI420FromBase64(s,'lpic')
		return redirect('/verify/')
	return redirect(request, '/')

def verify_view(request):
	if request.method=='POST':
		s=request.POST['verifypic']
		methods.getI420FromBase64(s,'vpic')
		context=methods.match_faces()
		print(context)
		return render(request, 'verify.html', context)
	context={'results':False,'face_distances':0, 'status':''}
	print(context)
	return render(request, 'verify.html', context)

# def capture(request):
# 	return render(request, 'home.html', {'data':data})