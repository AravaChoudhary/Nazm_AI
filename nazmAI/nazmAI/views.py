from django.http import HttpResponse
from django.shortcuts import render

def home(request) :
    return render(request,'index.html')

def about(request) :
    return HttpResponse('<h1>Hi this is the ABOUT PAGE for the Nazm AI</h1>')

def contact(request) : 
    return HttpResponse('<h1>This is the contacts page for the Nazm AI It is Created by ARAVA CHOUDHARY</h1')