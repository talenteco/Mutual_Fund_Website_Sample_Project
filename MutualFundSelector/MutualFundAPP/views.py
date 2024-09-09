from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, You are getting a response!")


