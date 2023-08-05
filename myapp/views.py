from django.http import HttpResponse
from datetime import datetime

API_KEY = "12345"

def authenticate_api_key(func):
    def wrapper(request, *args, **kwargs):
        if 'x-api-key' not in request.headers:
            return HttpResponse("Missing API key", status=401)

        api_key = request.headers['x-api-key']
        if api_key != API_KEY:
            return HttpResponse("Invalid API key", status=403)

        return func(request, *args, **kwargs)

    return wrapper

@authenticate_api_key
def hi(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    response = f"Hi! Good {get_day_time(current_time)}"
    return HttpResponse(response)

@authenticate_api_key
def hello(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    response = f"Hello! Good {get_day_time(current_time)}"
    return HttpResponse(response)

def get_day_time(current_time):
    hour = int(current_time.split(":")[0])
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Evening"
