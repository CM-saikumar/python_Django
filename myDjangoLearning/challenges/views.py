from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthlyChallenges(request, month):
    everyMonthInformation = None
    if month == "january":
        everyMonthInformation = "this is january month"
    elif month == "february":
        everyMonthInformation = "this is february month"
    else:
        return HttpResponseNotFound("not found")
    return HttpResponse(everyMonthInformation)
