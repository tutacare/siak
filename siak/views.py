from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home_page(request):
        return HttpResponseRedirect('http://127.0.0.7:8000/admin')