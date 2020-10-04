from django.shortcuts import render

# Create your views here.


def home(request):
    import requests
    import json

    news_api_request = requests.get(
        "https://breakingbadapi.com/api/characters")
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})
