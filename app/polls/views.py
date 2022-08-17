from django.http import HttpResponse


def index(request):
    return HttpResponse("Update to test dynamic config per app")