from django.http import HttpResponse


def index(request):
    """First view"""
    return HttpResponse("Hello, world!")
