from django.shortcuts import render
from django.http import HttpResponse as res

def login(request):
    return res('Login')
def signup(request):
    return res("Sign Up")
def  logout(request):
    pass
def reset(request):
    pass
def token(request):
    pass