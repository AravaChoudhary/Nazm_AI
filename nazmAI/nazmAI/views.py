from django.http import HttpResponse

def home(request) :
    return HttpResponse('<h1>Welcome tot the Nazm AI it is Just Starting : HOME PAGE</h1>')

def about(request) :
    return HttpResponse('<h1>Hi this is the ABOUT PAGE for the Nazm AI</h1>')

def contact(request) : 
    return HttpResponse('<h1>This is the contacts page for the Nazm AI It is Created by ARAVA CHOUDHARY</h1')