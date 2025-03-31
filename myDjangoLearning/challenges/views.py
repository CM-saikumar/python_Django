from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

japan_travel_challenges = {
    "january": {
        "place": "Sapporo, Hokkaido",
        "activities": [
            "Experience the Snow Festival (Yuki Matsuri)",
            "Try Hokkaido’s fresh seafood and miso ramen",
            "Go skiing or snowboarding in Niseko"
        ]
    },
    "february": {
        "place": "Hakone, Kanagawa",
        "activities": [
            "Relax in an onsen with views of Mt. Fuji",
            "Visit the Hakone Open-Air Museum",
            "Try a black egg from Owakudani"
        ]
    },
    "march": {
        "place": "Kyoto",
        "activities": [
            "Witness the cherry blossoms at Maruyama Park",
            "Explore Fushimi Inari Shrine",
            "Experience a traditional tea ceremony"
        ]
    },
    "april": {
        "place": "Takayama & Shirakawa-go, Gifu",
        "activities": [
            "Stroll through Takayama’s old town",
            "Explore the thatched-roof houses of Shirakawa-go",
            "Try Hida beef"
        ]
    },
    "may": {
        "place": "Okinawa",
        "activities": [
            "Relax on the beautiful beaches of Ishigaki or Miyakojima",
            "Visit Shurijo Castle",
            "Snorkel or dive in the Kerama Islands"
        ]
    },
    "june": {
        "place": "Nikko, Tochigi",
        "activities": [
            "Explore the Toshogu Shrine",
            "Hike around Lake Chuzenji and Kegon Falls",
            "Relax in Kinugawa Onsen"
        ]
    },
    "july": {
        "place": "Kamikochi, Nagano",
        "activities": [
            "Enjoy mountain hiking in the Japanese Alps",
            "Take in the views at Kappa Bridge",
            "Stay in a traditional ryokan by the river"
        ]
    },
    "august": {
        "place": "Aomori & Hirosaki",
        "activities": [
            "Witness the Nebuta Festival",
            "Visit Hirosaki Castle",
            "Try Aomori apples and fresh seafood"
        ]
    },
    "september": {
        "place": "Naoshima, Kagawa",
        "activities": [
            "Explore the art island (Benesse House, Chichu Art Museum)",
            "See the pumpkin sculpture by Yayoi Kusama",
            "Enjoy Seto Inland Sea views"
        ]
    },
    "october": {
        "place": "Fuji Five Lakes, Yamanashi",
        "activities": [
            "See Mt. Fuji framed by autumn foliage",
            "Row a boat or walk around Lake Kawaguchi",
            "Try Hoto noodles"
        ]
    },
    "november": {
        "place": "Hiroshima & Miyajima",
        "activities": [
            "Visit Hiroshima Peace Memorial Park",
            "See the floating torii gate at Itsukushima Shrine",
            "Try Hiroshima-style okonomiyaki"
        ]
    },
    "december": {
        "place": "Nagasaki",
        "activities": [
            "Visit Glover Garden",
            "Take in the night view from Mt. Inasa",
            "Try castella cake"
        ]
    }
}


def list_of_months(request):
    months = list(japan_travel_challenges.keys())

    response_data = render(
        request, "challenges/homePage.html", {"months": months})
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(japan_travel_challenges.keys())

    if month > len(months):
        raise Http404()
    redirect_month = months[month - 1]
    # /challenge/{month}
    redirect_url = reverse("montly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenges(request, month):
    if month in japan_travel_challenges:
        place = japan_travel_challenges[month]["place"]
        activities = japan_travel_challenges[month]["activities"]
        html_content = render_to_string("challenges/challenge.html", {
            "month": month,
            "place": place,
            "activities": activities
        })
        return HttpResponse(html_content)
    else:
        respose_data = render_to_string("404.html")
        return HttpResponseNotFound(respose_data)
