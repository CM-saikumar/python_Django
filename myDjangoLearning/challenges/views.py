from django.shortcuts import render
from django.http import HttpResponse

def firstChallenge(request):
    return HttpResponse("this is challenges page")